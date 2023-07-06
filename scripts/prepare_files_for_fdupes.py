import subprocess
from helper_functions import _get_files_with

# This script can only be run on Linux, and requires installing the command unix2dos.
# It is most convenient to run this command on a separate copy of the dataset, as the files are being changed for comparison. Then run the fdupes extraction, and delete the copy of the dataset.
urdf_dir = "urdf_files"
urdf_files = _get_files_with(urdf_dir,"*.urdf")

for urdf_file in urdf_files:
    # Change carriage return for all files to be CRLF
    subprocess.run(["unix2dos",urdf_file])

    # Remove whitespaces and tabs
    subprocess.run(["sed","-i","-e",'s/^[[:space:]]*//g',"-e",'s/[ \t]*//',urdf_file])