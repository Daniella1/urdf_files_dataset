# extract all unique robots
# group robots depending on source
# plot venn diagram
import pandas as pd
import numpy as np
import os
import json
import fileinput
import subprocess
from helper_functions import _get_files_with


URDF_LINK = True
ADD_TO_META_INFO = False

def extract_urdf_path(row):
    full_path = row.urdf_path.strip('][').replace('"','')
    full_path = full_path.strip("WindowsPath('")
    full_path = full_path.strip("')")
    return full_path

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

df_id_robots = pd.DataFrame(columns=["name","variant","id:source","type","manufacturer"])

df_original_robots['id'] = np.nan
ids = 0
for index, row in df_original_robots.iterrows():
    # check if robot exists in dataframe, if not then add it
    if len(df_id_robots[df_id_robots.name == row["name"]]) < 1:
        # add robot to df
        urdf_path = extract_urdf_path(row)
        source = urdf_path.split("/")[1]
        if not URDF_LINK:
            new_row = {'name': row["name"], 'variant': 'none', 'id:source': {ids:source}, 'type': row.type, 'manufacturer': row.manufacturer}
        else:
            new_row = {'name': row["name"], 'variant': 'none', 'id:source': {ids:f"<a href=\"{urdf_path}\">{source}</a>"}, 'type': row.type, 'manufacturer': row.manufacturer} # f"[{source}]({urdf_path})"
        
        df_id_robots = pd.concat([df_id_robots, pd.DataFrame([new_row])], axis=0, ignore_index=True)
    else:
        updated_sources = list(df_id_robots.loc[df_id_robots[df_id_robots.name == row["name"]].index,"id:source"])[0]
        if not URDF_LINK:
            updated_sources.update({ids:row["source"]})
        else:
            updated_sources.update({ids:f"<a href=\"{extract_urdf_path(row)}\">{row['source']}</a>"}) # f"[{row['source']}]({extract_urdf_path(row)})" 
    df_original_robots.loc[index,'id'] = ids # update the df_original_robots dataframe, so we can use it when updating the meta information file   
    ids += 1
df_id_robots = df_id_robots.sort_values('name',ascending=True)

df_variant_robots['id'] = np.nan
# finish adding the variants to the dataframe
for index, row in df_variant_robots.iterrows():
    # check if robot exists in dataframe, if not then add it
    if len(df_id_robots.loc[(df_id_robots.name == row["name"]) & (df_id_robots.variant == row["variant"])]) < 1:
        # add robot to df
        urdf_path = extract_urdf_path(row)
        source = urdf_path.split("/")[1]
        if not URDF_LINK:
            new_row = {'name': row["name"], 'variant': row["variant"], 'id:source': {ids:source}, 'type': row.type, 'manufacturer': row.manufacturer}
        else:
            new_row = {'name': row["name"], 'variant': row["variant"], 'id:source': {ids:f"<a href=\"{urdf_path}\">{source}</a>"}, 'type': row.type, 'manufacturer': row.manufacturer} # [f"[{source}]({urdf_path})"]
        df_id_robots = pd.concat([df_id_robots, pd.DataFrame([new_row])], axis=0, ignore_index=True)    
    else:
        updated_sources = list(df_id_robots.loc[df_id_robots[(df_id_robots.name == row["name"]) & (df_id_robots.variant == row["variant"])].index,"id:source"])[0]
        if not URDF_LINK:
            updated_sources.update({ids:row["source"]})
        else:
            updated_sources.update({ids:f":<a href=\"{extract_urdf_path(row)}\">{row['source']}</a>"})
    df_variant_robots.loc[index,'id'] = ids # update the df_original_robots dataframe, so we can use it when updating the meta information file
    ids += 1
    
df_id_robots[-len(df_variant_robots):] = df_id_robots[-len(df_variant_robots):].sort_values('name',ascending=True)

# update ids
# ids = np.linspace(0,ids-1,ids,dtype=int)
# df_id_robots['id'] = ids


if len(list({k: v for d in list(df_id_robots['id:source']) for k, v in d.items()}.keys())) != len(df): # len should be equal to number of robots
    print(f"ERROR: the length of the ids for the robots {len(list({k: v for d in list(df_id_robots['id:source']) for k, v in d.items()}.keys()))} is not equal to the number of robots {len(df)}")


# Print number of unique robots, and number of variants
n_unique_original_robots_across_sources = len(df_id_robots.loc[df_id_robots['variant'] == 'none'])
n_unique_variant_robots_across_sources = len(df_id_robots.loc[df_id_robots['variant'] != 'none'])
n_original_robots_in_total = len(df_original_robots)
n_variant_robots_in_total = len(df_variant_robots)

print(f"n_unique_original_robots_across_sources: {n_unique_original_robots_across_sources}")
print(f"n_unique_variant_robots_across_sources: {n_unique_variant_robots_across_sources}")
print(f"n_original_robots_in_total: {n_original_robots_in_total}")
print(f"n_variant_robots_in_total: {n_variant_robots_in_total}")

# add to meta files
if ADD_TO_META_INFO:
    df_all_robots = pd.concat([df_original_robots, df_variant_robots])
    # get list of all meta files
    # loop through each meta file
    # extract urdf_path
    # add id
    meta_files = _get_files_with("urdf_files", "meta-information.json")
    for meta_file in meta_files:
        # read meta file
        with open(meta_file, 'r') as f:
            data = json.load(f)
        for i in range(len(data['robots'])):
            robot_urdf = df_all_robots[(df_all_robots['urdf_path'].str.contains(data['robots'][i]['urdf'][0])) & (df_all_robots['urdf_path'].str.contains(os.path.dirname(meta_file).replace("\\","/")))]
            id = int(robot_urdf['id'])
            data['robots'][i]['id'] = id
        with open(meta_file, 'w') as f:
            json.dump(data, f,indent=4)


# perform a check to see that the number of variant robots is correct

# if not URDF_LINK:
#     df_id_robots.to_csv("df_id_robots.csv", index=False)    
# else:
#     df_id_robots.to_csv("df_id_robots_md.csv", index=False)


# with open("robot_index.md", 'w') as md:
#   df_id_robots.to_markdown(buf=md, index=False, tablefmt='unsafehtml', stralign=None, numalign=None)


# ## add id's to readme
# for line in fileinput.input("README.md", inplace = 1): 
#     print(line.replace("## Robots", f"## Robots\n{df_id_robots.to_markdown(index=False, tablefmt='unsafehtml', stralign=None, numalign=None)}\n").rstrip())
# fileinput.close()
