# extract all unique robots
# group robots depending on source
# plot venn diagram


# import json
# import pandas as pd
# from helper_functions import _get_files_with, _get_subdirectories
# import numpy as np
# import os
# from pathlib import Path
# import subprocess



# # if dataset information not available, then generate
# filename_dataset_information = "dataset_information.csv"
# if not os.path.isfile(filename_dataset_information):
#     subprocess.run(["python","scripts/extract_dataset_information.py"]) 
# # load dataset information
# df = pd.read_csv(filename_dataset_information)
# df = df.fillna("none")


# df_original_robots = df[df.variant == "none"] # without variant
# df_variant_robots = df[df.variant != "none"] # non-original

# unique_robots = df_original_robots.name.unique() # extract robots without a variant
# unique_variants = df_variant_robots.variant.unique()

# df_id_original_robots = pd.DataFrame(columns=["name","id","locations","type"])


# ids = 0
# for index, row in df_original_robots.iterrows():
#     print(row)
#     # check if robot exists in dataframe, if not then add it
#     if len(df_id_original_robots[df_id_original_robots.name == row.name]) < 1:
#         # add robot to df
#         urdf_path = row.urdf_path.strip('][').replace('"','')
#         urdf_path = urdf_path.strip("WindowsPath('")
#         urdf_path = urdf_path.strip("')")
#         new_row = {'name': row.name, 'id': ids, 'locations': [urdf_path], 'type': row.type}
#         df_id_original_robots = df_id_original_robots.append(new_row, ignore_index=True)
#     else:
#         pass
    
#     ids += 1

# print(df)




# from venn import pseudovenn, venn
import venn



from matplotlib.pyplot import subplots
from itertools import chain, islice
from string import ascii_uppercase
from numpy.random import choice


labels = venn.get_labels([range(10), range(5, 15), range(3, 8), range(8, 17), range(10, 20), range(13, 25)], fill=['number', 'logic'])
fig, ax = venn.venn6(labels, names=['list 1', 'list 2', 'list 3', 'list 4', 'list 5', 'list 6'])
fig.show()



# letters = iter(ascii_uppercase)

# dataset_dict = {
#     name: set(choice(1000, 700, replace=False))
#     for name in islice(letters, 6)
# }
# pseudovenn(dataset_dict, cmap="plasma")