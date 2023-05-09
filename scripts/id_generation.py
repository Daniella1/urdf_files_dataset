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

df_id_robots = pd.DataFrame(columns=["name","variant","id","sources","type"])


ids = 0
for index, row in df_original_robots.iterrows():
    # check if robot exists in dataframe, if not then add it
    if len(df_id_robots[df_id_robots.name == row["name"]]) < 1:
        # add robot to df
        urdf_path = row.urdf_path.strip('][').replace('"','')
        urdf_path = urdf_path.strip("WindowsPath('")
        urdf_path = urdf_path.strip("')")
        source = urdf_path.split("/")[1]
        new_row = {'name': row["name"], 'variant': 'none', 'id': ids, 'sources': [source], 'type': row.type}
        df_id_robots = df_id_robots.append(new_row, ignore_index=True)
        ids += 1
    else:
        updated_sources = list(df_id_robots.loc[df_id_robots[df_id_robots.name == row["name"]].index,"sources"])[0]
        updated_sources.append(row["source"])
    
df_id_robots = df_id_robots.sort_values('name',ascending=True)

# finish adding the variants to the dataframe
for index, row in df_variant_robots.iterrows():
    # check if robot exists in dataframe, if not then add it
    # if len(df_id_robots.loc[(df_id_robots.name == row["name"]) & (df_id_robots.variant == row["variant"])]) < 1:
    if len(df_id_robots.loc[(df_id_robots.name == row["name"]) & (df_id_robots.variant == row["variant"])]) < 1:
        # add robot to df
        urdf_path = row.urdf_path.strip('][').replace('"','')
        urdf_path = urdf_path.strip("WindowsPath('")
        urdf_path = urdf_path.strip("')")
        source = urdf_path.split("/")[1]
        new_row = {'name': row["name"], 'variant': row["variant"], 'id': ids, 'sources': [source], 'type': row.type}
        df_id_robots = df_id_robots.append(new_row, ignore_index=True)
        ids += 1
    else:
        updated_sources = list(df_id_robots.loc[df_id_robots[(df_id_robots.name == row["name"]) & (df_id_robots.variant == row["variant"])].index,"sources"])[0]
        updated_sources.append(row["source"])
    
df_id_robots[-len(df_variant_robots):] = df_id_robots[-len(df_variant_robots):].sort_values('name',ascending=True)

# update ids
ids = np.linspace(0,ids-1,ids,dtype=int)
df_id_robots['id'] = ids

# perform a check to see that the number of variant robots is correct
    
df_id_robots.to_csv("df_id_robots.csv", index=False)

