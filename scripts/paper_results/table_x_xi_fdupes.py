import pandas as pd
from pathlib import Path
import json
import numpy as np



# todo: check the meshes folder, if it is different for the robots or not

filetypes = ["urdf","stl","dae","obj"]
dir = "urdf_files/"
all_sources = ["ros-industrial","matlab","robotics-toolbox","drake","oems","random"]

def _get_files_with_in_cur_subdir(dir, files):
    list_of_file_paths = []

    # Check that path exists
    if not Path(dir).exists():
        return list_of_file_paths

    for path in Path(dir).glob(files):
        list_of_file_paths.append(path)

    return list_of_file_paths

def _get_meta_file_information(meta_file_path, path_name, path_parts, robots_so_far):
    with open(f"{meta_file_path}/meta-information.json", 'r') as f:
        data = json.load(f)
    n_robots = len(data['robots'])
    if n_robots > 1:
        for p in path_parts:
            for r in data['robots']:
                if r['name'].lower() in robots_so_far or r['name'].lower() in p.lower():
                    return r['name'].lower()
                elif r['name'].lower() not in robots_so_far and len(robots_so_far) > 0:
                    return robots_so_far[0]
        return path_name.lower()
    else:
        return data['robots'][0]['name'].lower()


def check_if_meta_information_file_in_dir(subdir):
    list_of_meta_files = _get_files_with_in_cur_subdir(subdir, "meta-information.json")
    return True if len(list_of_meta_files) > 0 else False

def _extract_fdupes_information(filename):
    with open(filename) as f:
        lines = f.readlines()

    identical_files = pd.DataFrame(columns=['robot','source','n_identical_files'])
    for i in range(len(lines)-1):
        robots_so_far = []
        if "./" in lines[i] and "./" in lines[i+1]:
            # check if it is "./" for more than just two lines
            j = i+1
            n_lines_dup = 2
            for j in range(j, len(lines)-1):
                if len(lines)-1 > j:
                    if "./" in lines[j] and "./" in lines[j+1]:
                        j += 1
                        n_lines_dup += 1
                    else:
                        break

            j = i
            # first check if the sources are different
            k = j
            sources = []
            for k in range(k, n_lines_dup+k):
                sources.append(lines[k].split("/")[1])
            if len(set(sources)) != len(sources) and len(set(sources)) == 1:
                # print(f"sources failed: {sources}")
                continue

            # elif len(set(sources)) != len(sources) and len(set(sources)) > 1:
                # need to remove one of the duplicates from the sources?
            sources = set(sources)



            # if robot exists but number of sources is different, then we need to create a new robot
            
            for j in range(j, n_lines_dup+j):
                lines[j] = lines[j].replace("\n","")
                path_parts = Path(lines[j]).parts
                source = path_parts[0]
                urdf_dir_index_start = 1
                urdf_dir_index = urdf_dir_index_start
                urdf_dir = path_parts[urdf_dir_index]
                
                
                robot_dir = Path(dir,source,urdf_dir)
                robot_dir_val = check_if_meta_information_file_in_dir(robot_dir)
                while not robot_dir_val: # check if meta-information file is within the urdf_bundle folder, if not, then go to next subdir and repeat
                    urdf_dir_index += 1
                    urdf_dir = path_parts[urdf_dir_index_start:urdf_dir_index+1]
                    robot_dir = Path(dir,source,*urdf_dir)
                    robot_dir_val = check_if_meta_information_file_in_dir(robot_dir)
                    

                urdf_bundle = path_parts[urdf_dir_index]
                urdf_bundle = _get_meta_file_information(robot_dir, urdf_bundle, path_parts, robots_so_far)
                robots_so_far.append(urdf_bundle)

            if urdf_bundle not in list(identical_files['robot']):
                identical_files = pd.concat([identical_files, pd.Series({'robot': urdf_bundle, 'source': str(sources), 'n_identical_files': 1}).to_frame().T], ignore_index=True)
            else:
                # two conditions: 
                #   1: the urdf_bundle and sources exist in identical_files, and we just need to increase the count. 
                #   2: the urdf_bundle exists but the sources are different, meaning we need to include a new row with this, and set n_identical_files to 1.

                identical_files.loc[np.logical_and(identical_files.robot == urdf_bundle, identical_files.source.to_list()[0] == sources)]
                urdf_bundle_and_sources = identical_files.loc[np.logical_and(identical_files.robot == urdf_bundle, str(sources) in identical_files.source.to_list())]

                if str(sources) in urdf_bundle_and_sources.source.to_list():
                    # locate source in dataframe, and add 1 to n_identical_files
                    r_index = identical_files.loc[identical_files['robot'] == urdf_bundle].index.to_list()
                    s = identical_files.source == str(sources)
                    s_index = [i for i, x in enumerate(identical_files.source == str(sources)) if x]
                    common_indices = list(set(s_index) & set(r_index))
                    assert len(common_indices) < 2, f"error occurred when calculating the identical files."
                    cur_index = common_indices[0]
                    identical_files.iloc[cur_index]['n_identical_files'] = identical_files.iloc[cur_index].n_identical_files+1
                else:
                    identical_files = pd.concat([identical_files, pd.Series({'robot': urdf_bundle, 'source': str(sources), 'n_identical_files': 1}).to_frame().T], ignore_index=True)

            i = j
    return identical_files

# dataframe for table X
source_filetype_df = pd.DataFrame(columns=all_sources,index=filetypes)
source_filetype_df.index = filetypes
source_filetype_df = source_filetype_df.fillna(0)

# dataframe for table XI
sources_correlation_df = pd.DataFrame(columns=all_sources,index=all_sources)
sources_correlation_df.index = all_sources
sources_correlation_df = sources_correlation_df.fillna(0)

for filetype in filetypes:
    filename = f"scripts/fdupes_run/identical_files_{filetype}.txt"
    fdupes_information = _extract_fdupes_information(filename)
    # fdupes_information.to_csv(f"fdupe_urdf_file_res_{filetype}.csv",index=False)

    # create Table X and Table XI
    for source in all_sources:
        source_robots = []
        correlated_sources = {s: [] for s in all_sources}
        for index, row in fdupes_information.iterrows():
            if source in row['source']:
                robot = row['robot']
                list_correlated_sources = [s for s in all_sources if s in row['source'] and s != source]
                for cs in list_correlated_sources:
                    if robot not in correlated_sources[cs]:
                        sources_correlation_df.loc[sources_correlation_df.index == source, cs] = sources_correlation_df.loc[sources_correlation_df.index == source, cs] +1
                        correlated_sources[cs].append(robot)
                 # extract other sources
                if robot not in source_robots:
                    source_filetype_df.loc[source_filetype_df.index == filetype,source] = source_filetype_df.loc[source_filetype_df.index == filetype,source] + 1
                    source_robots.append(robot)

source_filetype_df = source_filetype_df.transpose()
source_filetype_df.to_csv("table_x_fdupes_filetypes.csv")
sources_correlation_df.to_csv("table_xi_fdupes_sources.csv")
  
    
