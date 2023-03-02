# This script checks if the number of robots is the same as the number of urdf files in the paths. If not then it will print them out. This is used to detect if there any URDF Collections with multiple URDF Files per robot.
import json
import os
from pathlib import Path
from helper_functions import _get_files_with


def _check_urdf_paths_in_meta_information(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    metafile_dir = os.path.dirname(metafile)
    for robot in data['robots']:
        for urdf in robot["urdf"]:
            if not os.path.isfile(Path(metafile_dir,urdf)):
                print(f"Path {Path(metafile_dir,urdf)} does not exist")

dir = "urdf_files/"
meta_filename = "meta-information.json"

urdf_tag = "urdf"

meta_files = _get_files_with(dir, meta_filename)

for metafile in meta_files:
    _check_urdf_paths_in_meta_information(metafile)
