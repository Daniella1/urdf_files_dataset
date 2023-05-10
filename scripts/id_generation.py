# extract all unique robots
# group robots depending on source
# plot venn diagram
import fileinput
import sys
import pandas as pd
import numpy as np
import os
import subprocess


URDF_LINK = False

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

df_id_robots = pd.DataFrame(columns=["name","variant","id","sources","type"])

# <a href="urdf_files/ros-industrial/xacro_generated/robotiq/robotiq_2f_140_gripper_visualization/urdf/robotiq_arg2f_140_model.urdf">ros-industrial</a>

ids = 0
for index, row in df_original_robots.iterrows():
    # check if robot exists in dataframe, if not then add it
    if len(df_id_robots[df_id_robots.name == row["name"]]) < 1:
        # add robot to df
        urdf_path = extract_urdf_path(row)
        source = urdf_path.split("/")[1]
        if not URDF_LINK:
            new_row = {'name': row["name"], 'variant': 'none', 'id': ids, 'sources': [source], 'type': row.type}
        else:
            new_row = {'name': row["name"], 'variant': 'none', 'id': ids, 'sources': [f"<a href=\"{urdf_path}\">{source}</a>"], 'type': row.type} # f"[{source}]({urdf_path})"
        
        df_id_robots = pd.concat([df_id_robots, pd.DataFrame([new_row])], axis=0, ignore_index=True)
        # df_id_robots = df_id_robots.append(new_row, ignore_index=True)
        ids += 1
    else:
        updated_sources = list(df_id_robots.loc[df_id_robots[df_id_robots.name == row["name"]].index,"sources"])[0]
        if not URDF_LINK:
            updated_sources.append(row["source"])
        else:
            updated_sources.append(f"<a href=\"{extract_urdf_path(row)}\">{row['source']}</a>") # f"[{row['source']}]({extract_urdf_path(row)})" 
    
df_id_robots = df_id_robots.sort_values('name',ascending=True)

# finish adding the variants to the dataframe
for index, row in df_variant_robots.iterrows():
    # check if robot exists in dataframe, if not then add it
    # if len(df_id_robots.loc[(df_id_robots.name == row["name"]) & (df_id_robots.variant == row["variant"])]) < 1:
    if len(df_id_robots.loc[(df_id_robots.name == row["name"]) & (df_id_robots.variant == row["variant"])]) < 1:
        # add robot to df
        urdf_path = extract_urdf_path(row)
        source = urdf_path.split("/")[1]
        if not URDF_LINK:
            new_row = {'name': row["name"], 'variant': row["variant"], 'id': ids, 'sources': [source], 'type': row.type}
        else:
            new_row = {'name': row["name"], 'variant': row["variant"], 'id': ids, 'sources': [f"<a href=\"{urdf_path}\">{source}</a>"], 'type': row.type} # [f"[{source}]({urdf_path})"]
        df_id_robots = pd.concat([df_id_robots, pd.DataFrame([new_row])], axis=0, ignore_index=True)
        # df_id_robots = df_id_robots.append(new_row, ignore_index=True)
        ids += 1
    else:
        updated_sources = list(df_id_robots.loc[df_id_robots[(df_id_robots.name == row["name"]) & (df_id_robots.variant == row["variant"])].index,"sources"])[0]
        if not URDF_LINK:
            updated_sources.append(row["source"])
        else:
            updated_sources.append(f"<a href=\"{extract_urdf_path(row)}\">{row['source']}</a>")
    
df_id_robots[-len(df_variant_robots):] = df_id_robots[-len(df_variant_robots):].sort_values('name',ascending=True)

# update ids
ids = np.linspace(0,ids-1,ids,dtype=int)
df_id_robots['id'] = ids

# perform a check to see that the number of variant robots is correct

if not URDF_LINK:
    df_id_robots.to_csv("df_id_robots.csv", index=False)    
else:
    df_id_robots.to_csv("df_id_robots_md.csv", index=False)


with open("robot_index.md", 'w') as md:
  df_id_robots.to_markdown(buf=md, index=False, tablefmt='unsafehtml', stralign=None, numalign=None)


# for line in fileinput.input("README.md", inplace = 1): 
#     print(line.replace("## Robots", f"## Robots\n{df_id_robots.to_markdown(index=False, tablefmt='unsafehtml', stralign=None, numalign=None)}\n").rstrip())
# fileinput.close()
