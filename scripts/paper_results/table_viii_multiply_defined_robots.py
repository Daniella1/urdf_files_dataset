import os
import re
import json
import shutil
import subprocess
import numpy as np
import pandas as pd
from pathlib import Path
from itertools import combinations_with_replacement
from helper_functions import _get_files_with, _get_subdirectories
from urdf_analyzer import api


def _find_issue_and_description_rosparser(output_string, issue_word):
    issue_indices = [m.start() for m in re.finditer(issue_word, output_string.lower())]
    issues = set()
    for idx in issue_indices:
        issue = output_string[idx:output_string.find("\n",idx)]
        issue = str(issue.lower().replace(f"{issue_word}:","")).lstrip()
        issues.add(issue)
    return issues

## initialise parser
def check_urdf(filename):
    res = subprocess.run(f'check_urdf {filename}', shell=True, capture_output=True, text=True)
    if res.returncode == 0: # success
        return 0
    else:
        errors = _find_issue_and_description_rosparser(res.stderr, 'error')
        if len(errors) > 0:
            return -1
        else:
            return 0

def _extract_meta_information(filename, columns):
    meta_infos = pd.DataFrame(columns=columns)
    with open(filename, 'r') as f:
        data = json.load(f)
    robots = data['robots']
    urdf_path = os.path.dirname(filename)
    for robot in robots:
        meta_infos = pd.concat([meta_infos, pd.Series({'name':robot['name'], 'variant': robot['variant'], 'urdf_path': str([Path(urdf_path,p) for p in robot['urdf']]), 'n_urdfs':len(robot['urdf'])}).to_frame().T], ignore_index=True)
    return meta_infos

def _extract_source_information(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['source']

####

dataframe_columns = ['name','variant','urdf_path', 'n_urdfs']
dataset_information = pd.DataFrame(columns=dataframe_columns)

meta_info_filename = "meta-information.json"
source_info_filename = "source-information.json"

dir = "urdf_files"
subdirs = _get_subdirectories(dir)

for d in subdirs:
    list_of_meta_file_paths = _get_files_with(d, meta_info_filename)
    list_of_source_file_paths = _get_files_with(d, source_info_filename)
    assert len(list_of_source_file_paths) == 1, f"Error, expecting one source information file in subdataset, but found either more or none: {list_of_source_file_paths}"
    for file in list_of_meta_file_paths:
        meta_infos = _extract_meta_information(file, dataframe_columns)
        meta_infos['source'] = _extract_source_information(list_of_source_file_paths[0])
        dataset_information = pd.concat([dataset_information, meta_infos], ignore_index=True)

original_robots = dataset_information[dataset_information['variant'].isna()]
varianted_robots = dataset_information[dataset_information['variant'].notna()]
multiply_defined_original_robots = (original_robots.groupby('name').filter(lambda g: len(g) > 1).drop_duplicates(subset=['name', 'source'], keep="first")).sort_values(by=['name'])
multiply_defined_original_robots = (multiply_defined_original_robots.groupby('name').filter(lambda g: len(g) > 1).drop_duplicates(subset=['name', 'source'], keep="first")).sort_values(by=['name']) # to make sure it is only the duplicate robots)
multiply_defined_variant_robots = (varianted_robots.groupby('name').filter(lambda g: len(g) > 1).drop_duplicates(subset=['name', 'source'], keep="first")).sort_values(by=['name'])
multiply_defined_variant_robots = (multiply_defined_variant_robots.groupby('name').filter(lambda g: len(g) > 1).drop_duplicates(subset=['name', 'source'], keep="first")).sort_values(by=['name'])
multiply_defined_robots = pd.concat([multiply_defined_original_robots,multiply_defined_variant_robots])
n_multiply_defined_robots = (multiply_defined_robots['name'].value_counts()).reset_index().rename({'index': 'name','name':'n_mulitiply_defined'}, axis='columns')


multiply_defined_robots = multiply_defined_robots.replace(np.nan, 'original')
multiply_defined_robots = multiply_defined_robots.groupby(['name','variant'])['source','urdf_path'].apply(lambda x: x.to_dict('r')).reset_index(name='data') 

sources = ["ros-industrial","matlab","robotics-toolbox","drake","oems","random"]
cols = sources.copy()
cols.append("erroneous robots")
multiply_defined_robots_df = pd.DataFrame(index=sources,columns=cols)
multiply_defined_robots_df = multiply_defined_robots_df.fillna(0)

for index, row in multiply_defined_robots.iterrows():
    robot_sources = [d["source"] for d in row["data"]]
    robot_sources = sorted(robot_sources,key=sources.index,reverse=True)

    for combo in combinations_with_replacement(robot_sources,2):
        multiply_defined_robots_df.loc[combo[0],combo[1]] += 1

    urdf_paths = [d["urdf_path"].strip("[WindowsPath('").strip("')]") for d in row["data"]]
    for urdf_file in urdf_paths:
        res = check_urdf(str(urdf_file))
        if res == -1:
            src = urdf_file.split("/")[1]
            multiply_defined_robots_df.loc[src,"erroneous robots"] += 1


multiply_defined_robots_df.to_csv("table_viii_multiply_defined_robots.csv")

# duplicate_robots.to_csv("duplicate_robots.csv",index=False)
# n_multiply_defined_robots.to_csv("n_multiply_defined_robots.csv",index=False)


meta_info_columns = ["name","variant"]
duplicates_information_columns = meta_info_columns + ["source","n_urdf_files","n_joints","n_links","visual_meshes","collision_meshes","n_lines"]
duplicates_comparisons_columns = meta_info_columns + ["sources","joints_diff","links_diff","mesh_diff","fk_diff","n_lines_diff","urdf_files"]
duplicates_information = pd.DataFrame(columns=duplicates_information_columns)
duplicates_comparisons = pd.DataFrame(columns=duplicates_comparisons_columns)

# TODO fix this so that we don't need to create a file and read it
d = multiply_defined_robots.groupby('name')['variant','data'].apply(lambda x: x.set_index('variant')['data'].to_dict()).to_json().replace("\\","")
with open("duplicates.json", 'w') as f:
    json.dump(eval(d), f)
duplicates_filename = "duplicates.json" 
with open(duplicates_filename, 'r') as f:
    duplicates = json.load(f)

duplicates_information, duplicates_comparisons = api._get_duplicates_information(duplicates, ".", duplicates_information, duplicates_comparisons, None)

# delete created json file and results
os.remove(duplicates_filename)
shutil.rmtree("results")


multiply_defined_robots_feature_differences = pd.DataFrame(index=["n_joints","n_links","cad_file_type","forward_kin","n_lines"],columns=["n_robots"])
multiply_defined_robots_feature_differences = multiply_defined_robots_feature_differences.fillna(0)

multiply_defined_robots_feature_differences.loc["n_joints"] = duplicates_comparisons['joints_diff'].value_counts()[True]
multiply_defined_robots_feature_differences.loc["n_links"] = duplicates_comparisons['links_diff'].value_counts()[True]
multiply_defined_robots_feature_differences.loc["cad_file_type"] = duplicates_comparisons['mesh_diff'].value_counts()[True]
multiply_defined_robots_feature_differences.loc["forward_kin"] = duplicates_comparisons['fk_diff'].value_counts()[True]
multiply_defined_robots_feature_differences.loc["n_lines"] = duplicates_comparisons['n_lines_diff'].value_counts()[True]

multiply_defined_robots_feature_differences.to_csv("table_ix_multiply_defined_robots_feature_differences.csv")

# duplicates_information.to_csv("duplicates_information.csv")
# duplicates_comparisons.to_csv("duplicates_comparisons.csv")