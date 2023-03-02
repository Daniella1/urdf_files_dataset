# This scripts goes through the urdf_files and adds the urdf file names to the meta information
import json
import os
from pathlib import Path
from helper_functions import _get_files_with


def _check_tag_in_meta_information(filename, tag):
    with open(filename, 'r') as f:
        data = json.load(f)
    tag_in_meta = 0
    for robot in data['robots']:
        if urdf_tag in robot:
            tag_in_meta += 1 # in case  we in the future want to check if not all robots are missing a tag, then we can use the count
    if len(data['robots']) != tag_in_meta:
        return False, len(data['robots']), data
    return True, len(data['robots']), data


dir = "urdf_files/ros-industrial"
meta_filename = "meta-information.json"

urdf_tag = "urdf"

meta_files = _get_files_with(dir, meta_filename)

for metafile in meta_files:
    tag_is_in_meta, n_robots, json_data = _check_tag_in_meta_information(metafile, urdf_tag)
    if not tag_is_in_meta:
        print(f"tag: {tag_is_in_meta}, n_robots: {n_robots}")
    if n_robots > 1:
        continue
    if not tag_is_in_meta:
        metafile_dir = os.path.dirname(metafile)
        urdf_files = _get_files_with(metafile_dir,"*.urdf")
        edited_urdf_files = []
        for urdf_file in urdf_files:
            # change the directory to be correct
            rel_urdf_file = os.path.relpath(urdf_file, metafile_dir)
            rel_urdf_file = rel_urdf_file.replace("\\", '/')
            edited_urdf_files.append(rel_urdf_file)
        json_data["robots"][0]["urdf"] = edited_urdf_files # as there is only one robot, we can just take the first index
        with open(metafile, 'w') as f:
            json.dump(json_data, f)
    
