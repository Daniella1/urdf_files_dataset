import json
import pandas as pd


duplicates_filename = "duplicates.json" 
with open(duplicates_filename, 'r') as f:
    duplicates = json.load(f)

multiply_defined_robots_information = pd.DataFrame(columns=['name','variant','sources'])

for robot in duplicates:
    for variant in duplicates[robot]:
        sources_set = {src["source"] for src in duplicates[robot][variant]}
        robot_sources = {'name':robot,'variant': variant,'sources': str(sources_set)}

        multiply_defined_robots_information = pd.concat([multiply_defined_robots_information, pd.Series(robot_sources).to_frame().T], ignore_index=True)
            

multiply_defined_robots_information.to_csv("multiply_defined_robots_information.csv",index=False)





