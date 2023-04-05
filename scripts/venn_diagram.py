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


df_original_robots = df[df.variant == "none"] # without variant
df_variant_robots = df[df.variant != "none"] # non-original

unique_robots = df_original_robots.name.unique() # extract robots without a variant
unique_variants = df_variant_robots.variant.unique()

df_id_original_robots = pd.DataFrame(columns=["name","id","locations","type"])


ids = 0
for index, row in df_original_robots.iterrows():
    print(row)
    # check if robot exists in dataframe, if not then add it
    if len(df_id_original_robots[df_id_original_robots.name == row.name]) < 1:
        # add robot to df
        urdf_path = row.urdf_path.strip('][').replace('"','')
        urdf_path = urdf_path.strip("WindowsPath('")
        urdf_path = urdf_path.strip("')")
        new_row = {'name': row.name, 'id': ids, 'locations': [urdf_path], 'type': row.type}
        df_id_original_robots = df_id_original_robots.append(new_row, ignore_index=True)
    else:
        pass
    
    ids += 1

print(df)