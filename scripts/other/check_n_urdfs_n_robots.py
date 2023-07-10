# This script checks if the number of robots is the same as the number of urdf files in the paths. If not then it will print them out. This is used to detect if there any URDF Collections with multiple URDF Files per robot.
import json
import os
from pathlib import Path
from helper_functions import _get_files_with


def _get_n_robots_meta_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return len(data['robots'])

dir = "urdf_files/"
meta_filename = "meta-information.json"

urdf_tag = "urdf"

meta_files = _get_files_with(dir, meta_filename)

for metafile in meta_files:
    n_robots = _get_n_robots_meta_file(metafile)
    metafile_dir = os.path.dirname(metafile)
    urdf_files = _get_files_with(metafile_dir,"*.urdf")
    if n_robots != len(urdf_files):
        print(f"n_robots {n_robots} not equal to n_urdfs {len(urdf_files)} in dir {metafile_dir}")