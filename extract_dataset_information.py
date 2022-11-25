import json
import pandas as pd
import os
from pathlib import Path


GENERATE_CSVS = False
GENERATE_PLOTS = False

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


def _extract_meta_information(filename, columns):
    meta_infos = pd.DataFrame(columns=columns)
    with open(filename, 'r') as f:
        data = json.load(f)
    robots = data['robots']
    for robot in robots:
        meta_infos = pd.concat([meta_infos, pd.Series({'name':robot['name'], 'type': robot['type'], 'manufacturer':robot['manufacturer']}).to_frame().T], ignore_index=True)
    return meta_infos

def _extract_source_information(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['source']

####

dataframe_columns = ['name','type','manufacturer']
dataset_information = pd.DataFrame(columns=dataframe_columns)

meta_info_filename = "meta-information.json"
source_info_filename = "source-information.json"

dir = "./urdf_files"
subdirs = _get_subdirectories(dir)

for d in subdirs:
    list_of_meta_file_paths = _get_files_with(d, meta_info_filename)
    list_of_source_file_paths = _get_files_with(d, source_info_filename)
    assert len(list_of_source_file_paths) == 1, f"Error, expecting one source information file in subdataset, but found either more or none: {list_of_source_file_paths}"
    for file in list_of_meta_file_paths:
        meta_infos = _extract_meta_information(file, dataframe_columns)
        meta_infos['source'] = _extract_source_information(list_of_source_file_paths[0])
        dataset_information = pd.concat([dataset_information, meta_infos], ignore_index=True)
        

dataset_sources_n_robots = dataset_information.groupby(by='source').count()
dataset_sources_n_robots = dataset_sources_n_robots.reset_index().rename({'index':'source','name':'n_robots'}, axis='columns')

types_information = dataset_information['type'].value_counts()
types_information = types_information.reset_index().rename({'index':'type', 'type':'count'}, axis = 'columns')
manufacturers_information = dataset_information['manufacturer'].value_counts()
manufacturers_information = manufacturers_information.reset_index().rename({'index':'manufacturer', 'manufacturer':'count'}, axis = 'columns')
robots_information = dataset_information['name'].value_counts()
robots_information = robots_information.reset_index().rename({'index':'name', 'name':'count'}, axis = 'columns')


s = robots_information.loc[robots_information['name'].str.contains(" - ", case=False)]
mutated_robots = {}
for name,count in zip(list(s['name']), list(s['count'])):
    # extract everything before ' -'
    robot_name = name.split(' -')[0]
    if robot_name in mutated_robots:
        mutated_robots[robot_name] += count
    else:
        mutated_robots[robot_name] = count


# get n robots with flavours, and get n robots without flavours, and get n robots with and without flavours
robots_w_wo_mutation = {}
for robot in mutated_robots.keys():
    robots_w_wo_mutation[robot] = robots_information.loc[robots_information['name'].str.contains(robot, case=False)].sum()['count']



mutated_robots = pd.Series(mutated_robots)
mutated_robots = mutated_robots.reset_index().rename({'index':'name', 0:'count'}, axis = 'columns')
robots_w_wo_mutation = pd.Series(robots_w_wo_mutation)
robots_w_wo_mutation = robots_w_wo_mutation.reset_index().rename({'index':'name', 0:'count'}, axis = 'columns')


def _generate_plots():
    import matplotlib.pyplot as plt
    import numpy as np

    # for manufacturers
    # manufacturers = list(manufacturers_information['manufacturer'])
    # n_manufacturers = list(manufacturers_information['count'])

    # plt.rcdefaults()
    # fig, ax = plt.subplots()    
    # width = 0.75 # the width of the bars 
    # ind = np.arange(len(n_manufacturers))  # the x locations for the groups
    # bars = ax.barh(ind, n_manufacturers, width, color="blue")
    # ax.bar_label(bars)
    # ax.set_yticks(ind)
    # ax.set_yticklabels(manufacturers, minor=False)
    # plt.title('Distribution of robots from different manufacturers in dataset')
    # plt.xlabel('number of robots from manufacturer in dataset')
    # plt.savefig("manufacturers_information"+".svg", bbox_inches='tight')
    # plt.show()

    # for types    
    types = list(types_information['type'])
    n_types = list(types_information['count'])
    fig, ax = plt.subplots()
    width = 0.75
    ind = np.arange(len(n_types))  # the x locations for the groups
    bars = ax.barh(ind, n_types, width, color="blue")
    ax.bar_label(bars)
    ax.set_yticks(ind)
    ax.set_yticklabels(types, minor=False)
    plt.title('Distribution of types of robots in dataset')
    plt.xlabel('amount of specific robot type in dataset')
    plt.savefig("types_information"+".svg", bbox_inches='tight')
    plt.show()




if GENERATE_CSVS:
    dataset_information.to_csv("dataset_information.csv", index=False)
    types_information.to_csv("types_information.csv", index=False)
    manufacturers_information.to_csv("manufacturers_information.csv", index=False)
    robots_information.to_csv("robots_information.csv", index=False)
    mutated_robots.to_csv("mutated_robots.csv", index=False)
    robots_w_wo_mutation.to_csv("robots_w_wo_mutation.csv", index=False)
    dataset_sources_n_robots.to_csv("dataset_sources_n_robots.csv", index=False)


if GENERATE_PLOTS:
    _generate_plots()