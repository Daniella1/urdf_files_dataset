import pandas as pd


sources = ['ros-industrial','matlab','robotics-toolbox','drake','oems','random']
df_sources_robots = pd.DataFrame(columns=['source','robots'])

df_id_robots = pd.read_csv("df_id_robots.csv")
for source in sources:
    pass
print(1)