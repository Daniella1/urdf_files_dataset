# extract all unique robots
# group robots depending on source
# plot venn diagram


import json
import pandas as pd
from helper_functions import _get_files_with, _get_subdirectories
import numpy as np
import os
from pathlib import Path
import subprocess


# if dataset information not available, then generate
filename_dataset_information = "dataset_information.csv"
if not os.path.isfile(filename_dataset_information):
    subprocess.run(["python","scripts/extract_dataset_information.py"]) 
# load dataset information
df = pd.read_csv(filename_dataset_information)
df = df.fillna("none")

unique_robots = df.name.unique()
unique_variants = df.variant.unique()

print(df)