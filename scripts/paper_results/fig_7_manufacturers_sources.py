import json
import pandas as pd
from helper_functions import _get_files_with, _get_subdirectories
import numpy as np
import os
from pathlib import Path

GENERATE_CSVS = True
GENERATE_PLOTS = False


def _extract_meta_information(filename, columns):
    meta_infos = pd.DataFrame(columns=columns)
    with open(filename, 'r') as f:
        data = json.load(f)
    robots = data['robots']
    urdf_path = os.path.dirname(filename)
    for robot in robots:
        meta_infos = pd.concat([meta_infos, pd.Series({'name':robot['name'], 'manufacturer':robot['manufacturer']}).to_frame().T], ignore_index=True)
    return meta_infos

def _extract_source_information(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['source']

####

dataframe_columns = ['manufacturer','source']
manufacturer_information = pd.DataFrame(columns=dataframe_columns)

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
        manufacturer_information = pd.concat([manufacturer_information, meta_infos], ignore_index=True)
        

manufacturers_n_source_information = pd.DataFrame(manufacturer_information.groupby(['manufacturer','source']).count())
manufacturers_n_source_information = manufacturers_n_source_information.reset_index().rename({'name':'count'},axis='columns')
manufacturer_n_robots = manufacturer_information['manufacturer'].value_counts()
manufacturer_n_robots = manufacturer_n_robots.reset_index().rename({'index':'manufacturer', 'manufacturer':'count'}, axis = 'columns')

manufacturer_n_robots.to_csv("manufacturer_n_robots.csv",index=False)
manufacturers_n_source_information.to_csv("fig_7_manufacturers_n_source_information.csv",index=False)