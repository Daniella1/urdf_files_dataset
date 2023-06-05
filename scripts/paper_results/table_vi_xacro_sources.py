# To check if a file is generated using the xacro preprocessor, 
# we check if the word 'xacro' exists in the file.
# Defining a file was manually xacro generated is done 
# using information from the meta-information.json file.
import json
import pandas as pd
import os
from helper_functions import _get_subdirectories, _get_files_with

import warnings
warnings.filterwarnings("ignore")

def _count_word_in_urdf_file(word, urdf_file):
    with open(urdf_file) as f:
        return int(f.read().count(word))

def _get_word_information(words, file):
    for word in list(words.keys()):
        words[word] = words[word] + 1 if _count_word_in_urdf_file(word, file) > 0 else words[word]
    return words

def _extract_meta_information(filename, columns):
    meta_infos = pd.DataFrame(columns=columns)
    with open(filename, 'r') as f:
        data = json.load(f)
    robots = data['robots']
    for robot in robots:
        meta_infos = pd.concat([meta_infos, pd.Series({'xacro-generated': robot['xacro-generated']}).to_frame().T], ignore_index=True)
    return meta_infos

def _extract_source_information(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['source']


def _increment_value_df(df, value, info_type, row):
    n_value_generated = df.loc[df[info_type] == row[info_type], value]
    n_value_generated = n_value_generated.iloc[0] + 1

    df.loc[df[info_type] ==  row[info_type], value] = n_value_generated
    return df


def _xacro_generated_info(xacro_information, row, info_type, xacro_in_file):
    if (xacro_information[info_type] == row[info_type]).any():
        if row['xacro-generated']:
            xacro_information = _increment_value_df(xacro_information, 'MANUALLY generated WITH xacro', info_type, row)
        # else:
        #     xacro_information = _increment_value_df(xacro_information, 'non-xacro', info_type, row)

        if xacro_in_file and not row['xacro-generated']:
            xacro_information = _increment_value_df(xacro_information, 'ORIGINALLY generated WITH xacro', info_type, row)
        elif not xacro_in_file and not row['xacro-generated']:
            xacro_information = _increment_value_df(xacro_information, 'ORIGINALLY generated WITHOUT xacro', info_type, row)
    else:
        if row['xacro-generated']:
            xacro_generation_info = {info_type: row[info_type], 'MANUALLY generated WITH xacro': 1}
        else:
            xacro_generation_info = {info_type: row[info_type], 'MANUALLY generated WITH xacro': 0}
        if xacro_in_file and not row['xacro-generated']:
            xacro_generation_info.update({'ORIGINALLY generated WITH xacro': 1, 'ORIGINALLY generated WITHOUT xacro': 0})
            xacro_generation_info = pd.Series(xacro_generation_info)
        elif not xacro_in_file and not row['xacro-generated']:
            xacro_generation_info.update({'ORIGINALLY generated WITH xacro': 0, 'ORIGINALLY generated WITHOUT xacro': 1})
            xacro_generation_info = pd.Series(xacro_generation_info)
        else:
            xacro_generation_info.update({'ORIGINALLY generated WITH xacro': 0, 'ORIGINALLY generated WITHOUT xacro': 0})
            xacro_generation_info = pd.Series(xacro_generation_info)

        xacro_information = pd.concat([xacro_information, xacro_generation_info.to_frame().T], ignore_index=True)
    return xacro_information





source_xacro_columns = ['source','MANUALLY generated WITH xacro','ORIGINALLY generated WITH xacro','ORIGINALLY generated WITHOUT xacro']
source_xacro_information = pd.DataFrame(columns=source_xacro_columns)

meta_info_filename = "meta-information.json"
source_info_filename = "source-information.json"

dir = "urdf_files"
subdirs = _get_subdirectories(dir)


for d in subdirs:
    list_of_meta_file_paths = _get_files_with(d, meta_info_filename)
    list_of_source_file_paths = _get_files_with(d, source_info_filename)
    assert len(list_of_source_file_paths) == 1, f"Error, expecting one source information file in subdataset, but found either more or none: {list_of_source_file_paths}"

    

    for file in list_of_meta_file_paths:
        meta_infos = _extract_meta_information(file, ['xacro-generated'])
        meta_infos['source'] = _extract_source_information(list_of_source_file_paths[0])

        # assuming all the urdf files within a directory are either ALL manually xacro-generated or not, 
        # we can go through the URDF files in the directory and check if they are xacro generated, 
        # and add that information to the robots
        pathname = os.path.dirname(file)
        urdf_files = _get_files_with(pathname, "*.urdf")
        n_urdf_files = len(urdf_files)
        words = {'xacro': 0}
        for file in urdf_files:
            words = _get_word_information(words, file)
        # check if assumption is correct. If not, files need to be analysed manually and added to results.
        if words['xacro'] > 0:
            if words['xacro'] != n_urdf_files:
                print(f"ERROR: n_urdf_files: {n_urdf_files}, words['xacro']: {words['xacro']}, urdf_files: {urdf_files}.\nNeeds manual analysis")
                continue
            else:
                xacro_in_file = True
        else:
            xacro_in_file = False

        for index, row in meta_infos.iterrows():
            source_xacro_information = _xacro_generated_info(source_xacro_information, row, 'source', xacro_in_file)


source_xacro_information.to_csv("source_xacro_information.csv",index=False)


