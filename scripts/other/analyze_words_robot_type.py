import pandas as pd
from itertools import islice
import collections
import json

def take(n, iterable):
    """Return the first n items of the iterable as a list."""
    return list(islice(iterable, n))


df_source_robot_type = pd.read_csv("df_source_robot_type.csv")
print(df_source_robot_type)
print(df_source_robot_type['n_robots'].sum())
print(df_source_robot_type['n_urdf_files'].sum())

takeN = 20

sources = ["drake","matlab","oems","random","robotics-toolbox","ros-industrial"]
robot_types = ["robotic arm","end effector","mobile robot","humanoid robot","dual arm robot","mobile manipulator","quadrupedal robot","unknown"]

# get average number of each robot type
df_robot_type_avg_word = pd.DataFrame(columns=["type","n_robots","avg word count pr robot", "n_urdf_files","avg word count pr urdf"])
df_robot_type_avg_word_reduced = pd.DataFrame(columns=["type","n_robots","avg word count pr robot"])
n_robot_types = {robot_type: 0 for robot_type in robot_types}
n_urdf_files_robot_type = {robot_type: 0 for robot_type in robot_types}
total_words_count = {}
for robot_type in robot_types:
    avg_word_count_pr_robot = {}
    avg_word_count_pr_urdf = {}
    total_words_count_pr_robot = {}
    n_robot_types.update({robot_type: (df_source_robot_type[df_source_robot_type['type'] == robot_type]['n_robots']).sum()})
    n_urdf_files_robot_type.update({robot_type: (df_source_robot_type[df_source_robot_type['type'] == robot_type]['n_urdf_files']).sum()})
    for k,word_dict in dict(df_source_robot_type[df_source_robot_type['type'] == robot_type]['word count']).items():
        word_dict = eval(word_dict)
        for word in word_dict.keys():
            if word in total_words_count_pr_robot:
                total_words_count_pr_robot.update({word: total_words_count_pr_robot[word] + round(word_dict[word])})
            else:
                total_words_count_pr_robot[word] = round(word_dict[word])
            if word in total_words_count:
                total_words_count.update({word: total_words_count[word] + round(word_dict[word])})
            else:
                total_words_count[word] = round(word_dict[word])
    avg_word_count_pr_robot[robot_type] = {w: int(total_words_count_pr_robot[w]/n_robot_types[robot_type]) for w in total_words_count_pr_robot.keys()}
    avg_word_count_pr_urdf[robot_type] = {w: int(total_words_count_pr_robot[w]/n_urdf_files_robot_type[robot_type]) for w in total_words_count_pr_robot.keys()}

    sorted_avg_word_pr_robot = sorted(collections.OrderedDict(avg_word_count_pr_robot[robot_type]).items(), key=lambda x:x[1], reverse=True)
    sorted_avg_word_pr_urdf = sorted(collections.OrderedDict(avg_word_count_pr_urdf[robot_type]).items(), key=lambda x:x[1], reverse=True)

    df_robot_type_avg_word = pd.concat([df_robot_type_avg_word,pd.Series({'type': robot_type, 'n_robots': n_robot_types[robot_type],'avg word count pr robot': sorted_avg_word_pr_robot,'n_urdf_files': n_urdf_files_robot_type[robot_type], 'avg word count pr urdf': sorted_avg_word_pr_urdf}).to_frame().T], ignore_index=True)
    
    df_robot_type_avg_word_reduced = pd.concat([df_robot_type_avg_word_reduced,pd.Series({'type': robot_type, 'n_robots': n_robot_types[robot_type],'avg word count pr robot':take(takeN,sorted_avg_word_pr_robot)}).to_frame().T], ignore_index=True)


    print(f"robot_type ({robot_type}): {n_robot_types[robot_type]},\navg word count pr robot: {take(takeN, sorted(avg_word_count_pr_robot[robot_type].items(),key=lambda x:x[1]))},\navg word count pr urdf file: {sorted(take(takeN, avg_word_count_pr_urdf[robot_type].items()),key=lambda x:x[1], reverse=True)}\n")


df_robot_type_avg_word.to_csv("df_robot_type_avg_word.csv",index=False)
df_robot_type_avg_word_reduced.to_csv("df_robot_type_avg_word_reduced.csv",index=False)

with open("total_words_count.json",'w') as f:
    json.dump(total_words_count, f)

print(f"total words count: {sorted(take(takeN, collections.OrderedDict(total_words_count).items()),key=lambda x:x[1], reverse=True)}")



