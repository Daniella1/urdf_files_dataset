import json
import pandas as pd
import os
from pathlib import Path
import operator
from helper_functions import _get_files_with, _get_subdirectories

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
        meta_infos = pd.concat([meta_infos, pd.Series({'manufacturer':robot['manufacturer'], 'type': robot['type'], 'name': robot['name']}).to_frame().T], ignore_index=True)
    return meta_infos

def _extract_source_information(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['source']


# change to use replace instead of this
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

######  Extract unique words


def count_unique_words(file, filename):
    with open(file) as f:
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

    word_count = dict(sorted(word_count.items(), key=operator.itemgetter(1),reverse=True)) # sort descending

    # TODO: change to write word and count to json file
    txt = [f"{k}: {word_count[k]}\n" for k in word_count.keys()]
    with open(f"{filename}.txt", 'w') as fp:
        for t in txt:
            fp.write(t)


# get unique words

meta_info_filename = "meta-information.json"
source_info_filename = "source-information.json"

dir = "urdf_files/drake"
subdirs = _get_subdirectories(dir)
root_dir = os.getcwd()
results_dir = Path(root_dir, "results")

# for d in subdirs:
a = dir
list_of_meta_file_paths = _get_files_with(a, meta_info_filename)
list_of_source_file_paths = _get_files_with(a, source_info_filename)
assert len(list_of_source_file_paths) == 1, f"Error, expecting one source information file in subdataset, but found either more or none: {list_of_source_file_paths}"


def get_count(urdf_files, i):
    for urdf_file in urdf_files:
        filename = Path(results_source_dir,f"{(meta_infos['name'][i]).replace('/','')}__{meta_infos['manufacturer'][i]}__{meta_infos['type'][i]}")
        count_unique_words(urdf_file,filename)
        i += 1

for file in list_of_meta_file_paths:
    i = 0
    meta_infos = _extract_meta_information(file, ['manufacturer','type','name'])
    meta_infos['source'] = _extract_source_information(list_of_source_file_paths[0])

    pathname = os.path.dirname(file)
    urdf_files = _get_files_with(pathname, "*.urdf")
    results_source_dir = Path(results_dir, meta_infos['source'][0])
    if not results_source_dir.exists():
        os.mkdir(results_source_dir)


    n_robots_equal = len(meta_infos) != len(urdf_files) 
    unique_manufacturers = len(meta_infos['manufacturer'].unique()) > 1
    unique_robot_types = len(meta_infos['type'].unique()) > 1
    if n_robots_equal or unique_manufacturers or unique_robot_types:
        if n_robots_equal:
            print(f"len(meta_infos): {len(meta_infos)}, len(urdf_files): {len(urdf_files)}, meta_infos['name']: {meta_infos['name']}, meta_file: {file}. Files need to be analysed manually.")
        if unique_manufacturers:
            print(f"ERROR: different manufacturers in folder: {meta_infos['manufacturer']}, meta_file: {file}.\nNeeds manual analysis")
        if unique_robot_types:
            print(f"ERROR: different robot types in folder: {meta_infos['type']}, meta_file: {file}.\nNeeds manual analysis")
    else:
        get_count(urdf_files, i)
        

