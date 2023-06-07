import pandas as pd
import json
from helper_functions import _get_files_with
import os
from urdf_analyzer import api


def _extract_meta_information(filename, meta_infos, cur_dir, source):
    with open(filename, 'r') as f:
        data = json.load(f)
    robots = data['robots']
    for robot in robots:
        # extract information
        name = robot['name']
        type = robot['type']
        manufacturer = robot['manufacturer']
        urdf_paths = robot['urdf']
        variant = robot['variant']

        # extract information from urdf files
        n_joints = 0
        n_links = 0
        joint_names = []
        link_names = []
        for urdf_file in urdf_paths:
            models_information = api.generate_model_information_schema(f"{cur_dir}/{urdf_file}") # list of URDFInformation
            for urdf_info in models_information:
                if urdf_info.filename is not None:
                    n_joints += urdf_info.joint_information.n_joints
                    n_links += urdf_info.link_information.n_links
                    joint_names += list(urdf_info.joint_information.df_results_full['joint_names'])
                    link_names += list(urdf_info.link_information.df_results_full['link_names'])
        
        joint_names = [item for sublist in joint_names for item in sublist]
        link_names = [item for sublist in link_names for item in sublist]

        # add information to dataframe
        meta_infos = pd.concat([meta_infos, pd.Series({'name':name, 'type': type, 'manufacturer':manufacturer, 'urdf': urdf_paths, 'variant': variant, 'source':source,'n_links': n_links, 'n_joints': n_joints, 'joint_names': joint_names, 'link_names': link_names}).to_frame().T], ignore_index=True)
    return meta_infos

sources = ["ros-industrial","matlab","robotics-toolbox","drake","oems","random"]
root_dir = "urdf_files"
meta_info_columns = ['name','type','manufacturer','urdf','variant','source']
meta_infos = pd.DataFrame(columns=meta_info_columns)
for source in sources:
    src_dir = f"{root_dir}/{source}"
    meta_files = _get_files_with(src_dir,"meta-information.json")
    for meta_file in meta_files:
        meta_file_dir = os.path.dirname(meta_file).replace('\\','/').replace(src_dir,'')
        meta_infos = _extract_meta_information(meta_file, meta_infos, f"{src_dir}/{meta_file_dir}", source)
    

##### TABLE XII avg links and joints
# get the number of links and joints for each type of robot
robot_types = ["robotic arm","end effector", "mobile robot","humanoid robot","dual arm robot","mobile manipulator", "quadrupedal robot"]
robot_type_model_information = pd.DataFrame(columns=["Robot type","Avg. #links","Avg. #joints"])
for robot_type in robot_types:
    n_links = list(meta_infos.loc[meta_infos['type'] == robot_type, 'n_links'])
    n_joints = list(meta_infos.loc[meta_infos['type'] == robot_type, 'n_joints'])
    
    assert len(n_links) == len(n_joints), "n_links is not equal to n_joints"
    n_robots = len(n_links)

    if n_robots != 0: # jsut for testing purposes
        avg_links = sum(n_links)/n_robots
        avg_joints = sum(n_joints)/n_robots

        robot_type_model_information = pd.concat([robot_type_model_information, pd.Series({'Robot type':robot_type, 'Avg. #links':avg_links, 'Avg. #joints': avg_joints}).to_frame().T], ignore_index=True)

robot_type_model_information.to_csv("table_xii_avg_links_joints.csv",index=False)



##### TABLE XIII words world and flange
# check the number of joints and links named 'world' and 'flange' from the different sources
words_to_check = ['world','flange']
source_model_name_information = pd.DataFrame(columns=["source"] + words_to_check)
for source in sources:
    joint_names = list(meta_infos.loc[meta_infos['source'] == source, 'joint_names'])
    joint_names = [item for sublist in joint_names for item in sublist]
    link_names = list(meta_infos.loc[meta_infos['source'] == source, 'link_names'])
    link_names = [item for sublist in link_names for item in sublist]

    word_count_info = {'source': source}
    for word in words_to_check:
        word_count_joints = sum(word in s for s in joint_names)
        word_count_links = sum(word in s for s in link_names)
        total_word_count = word_count_joints + word_count_links
        word_count_info[f"{word} joints"] = word_count_joints
        word_count_info[f"{word} links"] = word_count_links
        word_count_info[word] = total_word_count

    source_model_name_information = pd.concat([source_model_name_information, pd.Series(word_count_info).to_frame().T], ignore_index=True)

source_model_name_information[["source","world","flange"]].to_csv("table_xiii_world_flange_links_joints.csv",index=False) # extract only columns for the table