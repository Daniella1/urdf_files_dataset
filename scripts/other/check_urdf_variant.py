# This script checks if each meta file has a urdf variant. It then moves the variant tag to be after the urdf tag in the json file
import json
import os
from pathlib import Path
from helper_functions import _get_files_with


def _check_variant_in_meta_information(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    metafile_dir = os.path.dirname(metafile)
    robots_data = []
    for robot in data['robots']:
        if "variant" not in robot:
            print(f"Variant in file {metafile_dir}/{filename} missing")
        else:
            ordered_data = robot.copy()
            del ordered_data["variant"]
            ordered_data["variant"] = robot["variant"]
            robots_data.append(ordered_data)
    with open(filename, 'w') as f:
        json.dump({"robots": robots_data}, f, indent=4)
    

dir = "urdf_files"
meta_filename = "meta-information.json"

meta_files = _get_files_with(dir, meta_filename)

for metafile in meta_files:
    _check_variant_in_meta_information(metafile)
