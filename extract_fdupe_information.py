import pandas as pd

filetypes = ["obj","dae","stl","urdf"]
dir = "duplicates/"


RUNNING_DUPLICATES = True

def _extract_duplicates_information(filename):
    with open(filename) as f:
        lines = f.readlines()

    duplicates = pd.DataFrame(columns=['robot','source','n_duplicates'])
    for i in range(len(lines)-1):
        if "./" in lines[i] and "./" in lines[i+1]:
            # check if it is "./" for more than just two lines, up to 20 next can potentially be the same
            j = i+1
            n_lines_dup = 2
            for j in range(j, len(lines)-1):
                if len(lines)-1 > j:
                    if "./" in lines[j] and "./" in lines[j+1]:
                        j += 1
                        n_lines_dup += 1
                    else:
                        break

            j = i
            for j in range(j, n_lines_dup+j):
                if RUNNING_DUPLICATES:
                    robot = lines[j].split("/")[1]
                    source = lines[j].split("/")[2]
                else:
                    robot = lines[j].split("/")[2]
                    source = lines[j].split("/")[1]

                if robot not in list(duplicates['robot']):
                    duplicates = pd.concat([duplicates, pd.Series({'robot': robot, 'source': source, 'n_duplicates': 1}).to_frame().T], ignore_index=True)
                else:
                    s = duplicates.loc[duplicates['robot'] == robot]
                    if not (duplicates.loc[duplicates.robot == robot]['source'].str.contains(source)).any():
                        duplicates.loc[duplicates.robot == robot, 'source'] = f"{s.source.item()},{source}"
                    duplicates.loc[duplicates.robot == robot, 'n_duplicates'] = s.n_duplicates.item()+1
                    
            # fast forward i:
            i = j
    return duplicates


for filetype in filetypes:
    filename = f"{dir}/duplicates_{filetype}.txt"
    dup = _extract_duplicates_information(filename)
    if not RUNNING_DUPLICATES:
        dup.to_csv(f"fdupe_urdf_file_res_{filetype}.csv",index=False)
    else:
        dup.to_csv(f"fdupe_duplicates_res_{filetype}.csv",index=False)

