import json
import pandas as pd
from helper_functions import _get_files_with, _get_subdirectories


def _extract_meta_information(filename, columns):
    meta_infos = pd.DataFrame(columns=columns)
    with open(filename, 'r') as f:
        data = json.load(f)
    robots = data['robots']
    for robot in robots:
        meta_infos = pd.concat([meta_infos, pd.Series({'name':robot['name'],'n_robots':len(robot['urdf']), 'variant': "original" if robot['variant'] is None else robot['variant']}).to_frame().T], ignore_index=True)
    return meta_infos

def _extract_source_information(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['source']

dataframe_columns = ['source','n_robots','variant']
sources_n_robots = pd.DataFrame(columns=dataframe_columns)

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
        sources_n_robots = pd.concat([sources_n_robots, meta_infos], ignore_index=True)
        

sorted_sources = ["ros-industrial","matlab","robotics-toolbox","drake","oems","random"]
variants = sources_n_robots[['source','variant']]


sources_n_robots = sources_n_robots[['source','n_robots','variant']].groupby(by='source').count()
sources_n_robots = sources_n_robots.reset_index().rename({'index':'source','variant': 'n_variants'}, axis='columns')
for src in sorted_sources:
    n_variants = len(variants[(variants['source'] == src) & (variants['variant'] != 'original')])
    sources_n_robots.loc[sources_n_robots['source'] == src,'n_variants'] = n_variants


sources_n_robots.to_csv("table_ii_sources_n_robots.csv", index=False)
