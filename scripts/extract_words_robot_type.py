import json
import pandas as pd
import os
from pathlib import Path
import operator
from helper_functions import _get_files_with
import collections
from itertools import islice


takeN = 20

def take(n, iterable):
    """Return the first n items of the iterable as a list."""
    return list(islice(iterable, n))

def _strip_out(words, filters=[]):
    for filter in filters:
        words = [word.split(filter) for word in words] # filter out strip
        words = [word for word_list in words for word in word_list]
    return words

def _remove_numbers(words):
    only_words = []
    for word in words:
        if word[-1] == "e":
            try:
                float(word[:-1])
            except:
                only_words.append(word)
        else:
            try:
                float(word)
            except:
                only_words.append(word)
        
    return only_words

def _extract_meta_robot_information(filename, tag_name, tag_value):
    with open(filename, 'r') as f:
        data = json.load(f)
    metafile_dir = os.path.dirname(filename)
    urdf_files = []
    n_robots = 0
    for robot in data['robots']:
        if robot[tag_name] == tag_value:
            n_robots += 1
            for urdf in robot["urdf"]:
                if not os.path.isfile(Path(metafile_dir,urdf)):
                    print(f"Path {Path(metafile_dir,urdf)} does not exist. Skipping URDF file.")
                    continue
                urdf_files.append(Path(metafile_dir, urdf))

    return urdf_files, n_robots



def count_unique_words(urdf_files, df, df_source_robot_type_reduced, source, robot_type, n_robots):
    word_count_all = {}
    for urdf_file in urdf_files:
        with open(urdf_file) as f:
            urdf = f.read()

        all_lines = urdf.splitlines()
        words = []
        for a in all_lines:
            a = a.strip("<")
            a = a.strip(">")
            words.append(a.split(" "))

        words = [word.lower() for word_list in words for word in word_list]
        words = _strip_out(words, ["/",">","<","=","[","]","!",'"',"-",",","?",".","(",")","_",":","$",";","\\","#"],)
        words = [word for word in words if len(word) > 0] # filter out ''
        words = _remove_numbers(words)

        word_count = {}
        unique_words = set(words)
        for kw in unique_words:
            word_count[kw] = words.count(kw)

        for key in list(word_count.keys()):
            if key in word_count_all:
                word_count_all[key] += word_count[key]
            else:
                word_count_all[key] = word_count[key]

    word_count_all = dict(sorted(word_count_all.items(), key=operator.itemgetter(1),reverse=True)) # sort descending

    df = pd.concat([df, pd.Series({'source':source, 'type': robot_type, 'n_robots': n_robots, 'n_urdf_files': len(urdf_files), 'word count':word_count_all}).to_frame().T], ignore_index=True)
    df_source_robot_type_reduced = pd.concat([df_source_robot_type_reduced, pd.Series({'source':source, 'type': robot_type, 'n_robots': n_robots, 'word count':take(takeN, sorted(collections.OrderedDict(word_count_all).items(), key=lambda x:x[1], reverse=True))}).to_frame().T], ignore_index=True)
    return df, df_source_robot_type_reduced



sources = ["drake","matlab","oems","random","robotics-toolbox","ros-industrial"]
root_dir = "urdf_files/"
robot_types = ["robotic arm","end effector","mobile robot","humanoid robot","dual arm robot","mobile manipulator","quadrupedal robot","unknown"]
meta_filename = "meta-information.json"

df_source_robot_type = pd.DataFrame(columns=["source","type","n_robots","n_urdf_files","word count"])
df_source_robot_type_reduced = pd.DataFrame(columns=["source","type","n_robots","word count"])


for source in sources:
    meta_files = _get_files_with(Path(root_dir,source), meta_filename)
    for robot_type in robot_types:
        all_urdf_files = []
        n_all_robots = 0
        for metafile in meta_files:
            urdf_files, n_robots = _extract_meta_robot_information(metafile, "type", robot_type)
            all_urdf_files.append(urdf_files)
            n_all_robots += n_robots
        all_urdf_files = [urdf_list for urdf_files in all_urdf_files for urdf_list in urdf_files] # flatten list of lsits
        if len(all_urdf_files) > 0:
            df_source_robot_type, df_source_robot_type_reduced = count_unique_words(all_urdf_files, df_source_robot_type, df_source_robot_type_reduced, source, robot_type, n_all_robots)
    

# Dataframe with source and robot type, and word count
# Dataframe with robot type and word count, regardless of sources (robot type, n_robots, n_urdf_files, word count)
# Dataframe with source and number of each robot type, and number of urdf files for each robot types (source, type, n_robots, n_urdf_files, word count)

print(df_source_robot_type)
print(df_source_robot_type['n_robots'].sum()) # check the number of robots is equal to the total number of robots in the dataset (274)
print(df_source_robot_type['n_urdf_files'].sum()) # check the number of URDF files is equal to the total number of URDF iles in the dataset (326)




df_source_robot_type.to_csv("df_source_robot_type.csv", index=False)
df_source_robot_type_reduced.to_csv("df_source_robot_type_reduced.csv", index=False)