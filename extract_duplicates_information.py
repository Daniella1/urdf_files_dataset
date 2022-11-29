import json
import pandas as pd
import os
from pathlib import Path
import subprocess

# Helper functions 
def _get_subdirectories(dir):
    subdirectories = [f.path for f in os.scandir(dir) if f.is_dir()]
    return subdirectories

def _get_files_with(dir, files):
    list_of_file_paths = []

    # Check that path exists
    if not Path(dir).exists():
        print(f"Warning, the path {dir} doesn't exist.")
        return list_of_file_paths

    for path in Path(dir).rglob(files):
        list_of_file_paths.append(path)

    if len(list_of_file_paths) == 0:
        print(f"Warning, no files found when searching for {files} in {dir}.")
    return list_of_file_paths


def _extract_meta_information(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    meta_info = {'name':data['name'], 'type': data['type'], 'manufacturer':data['manufacturer']}
    return meta_info

def _extract_source_information(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['source']


## initialise parser
def check_urdf(filename):
    res = subprocess.run(f'check_urdf {filename}', shell=True, capture_output=True, text=True)
    if res.returncode == 0: # success
        return res.stdout
    else:
        return None

####

dataframe_columns = ['name','n_sources','n_urdfs_parsed','type','manufacturer']
duplicate_information = pd.DataFrame(columns=dataframe_columns)
sources_parsing_urdf_dataframe = pd.DataFrame(columns=['name','sources_passed','sources_failed', 'failed_files'])
source_n_duplicates_dataframe = pd.DataFrame(columns=['source','n_robots', 'robots'])

meta_info_filename = "meta-information.json"
source_info_filename = "source-information.json"

dir = "./duplicates"
subdirs = _get_subdirectories(dir)



for d in subdirs:
    list_of_meta_file_paths = _get_files_with(d, meta_info_filename)
    list_of_source_file_paths = _get_files_with(d, source_info_filename)
    assert len(list_of_source_file_paths) > 1, f"Error, expecting mre than one source information file in the duplicate folder, but found either less or none: {list_of_source_file_paths}"
    assert len(list_of_meta_file_paths) == 1, f"Error, expecting one meta information file in subdataset, but found either more or none: {list_of_meta_file_paths}"

    meta_info = _extract_meta_information(list_of_meta_file_paths[0])
    n_sources = len(list_of_source_file_paths)
    
    sources_passing = {'name':meta_info['name'],'sources_passed': [], 'sources_failed':[], 'failed_files': []}
    for file in list_of_source_file_paths:
        source_urdf_path = os.path.dirname(file)
        urdf_files = _get_files_with(source_urdf_path, "*.urdf")
        source_info = _extract_source_information(file)
        for urdf_file in urdf_files:
            res = check_urdf(str(urdf_file))
            if res is not None:
                sources_passing['sources_passed'].append(source_info)
            else:
                sources_passing['sources_failed'].append(source_info)
                sources_passing['failed_files'].append(urdf_file)

        if (source_n_duplicates_dataframe.source == source_info).any():
            row_cur_source_robot = source_n_duplicates_dataframe.loc[source_n_duplicates_dataframe['source'] == source_info, 'robots']
            row_cur_source_robot.iloc[0].append(meta_info['name'])
            cur_source_robots = row_cur_source_robot.iloc[0]
            row_cur_source_n_robots = source_n_duplicates_dataframe.loc[source_n_duplicates_dataframe['source'] == source_info, 'n_robots']
            cur_source_n_robots = row_cur_source_n_robots.iloc[0] + 1

            source_n_duplicates_dataframe.loc[source_n_duplicates_dataframe['source'] == source_info, 'n_robots'] = cur_source_n_robots
        else:
            source_n_duplicate_info = pd.Series({'source': source_info, 'robots': [meta_info['name']], 'n_robots': 1})  

            source_n_duplicates_dataframe = pd.concat([source_n_duplicates_dataframe, source_n_duplicate_info.to_frame().T], ignore_index=True)

    sources_parsing_urdf_dataframe = pd.concat([sources_parsing_urdf_dataframe, pd.Series(sources_passing).to_frame().T], ignore_index=True)
    duplicate_infos = pd.Series({'name':meta_info['name'], 'n_sources':n_sources, 'n_urdfs_parsed': len(sources_passing['sources_passed']), 'type':meta_info['type'], 'manufacturer':meta_info['manufacturer']}).to_frame().T
    duplicate_information = pd.concat([duplicate_information, duplicate_infos], ignore_index=True)


# Save information on parsing, and duplicates
# duplicate_information.to_csv("duplicates_parsing_information.csv", index=False)
# sources_parsing_urdf_dataframe.to_csv("sources_parsing_information.csv", index=False)
# source_n_duplicates_dataframe.to_csv("source_n_duplicates_information.csv", index=False)


for sourceA in source_n_duplicates_dataframe.source:
    for robot in source_n_duplicates_dataframe.loc[source_n_duplicates_dataframe.source == sourceA].robots:
        source_n_duplicates_dataframe.loc[robot in source_n_duplicates_dataframe.robots]