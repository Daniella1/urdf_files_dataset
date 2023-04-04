import json
import pandas as pd
from helper_functions import _get_files_with, _get_subdirectories
import numpy as np
import os
from pathlib import Path

GENERATE_CSVS = True
GENERATE_PLOTS = False


def _extract_meta_information(filename, columns):
    meta_infos = pd.DataFrame(columns=columns)
    with open(filename, 'r') as f:
        data = json.load(f)
    robots = data['robots']
    urdf_path = os.path.dirname(filename)
    for robot in robots:
        meta_infos = pd.concat([meta_infos, pd.Series({'name':robot['name'], 'type': robot['type'], 'variant': robot['variant'], 'manufacturer':robot['manufacturer'], 'urdf_path': str([Path(urdf_path,p) for p in robot['urdf']]), 'n_urdfs':len(robot['urdf'])}).to_frame().T], ignore_index=True)
    return meta_infos

def _extract_source_information(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['source']

####

dataframe_columns = ['name','type','variant','manufacturer','urdf_path', 'n_urdfs']
dataset_information = pd.DataFrame(columns=dataframe_columns)

meta_info_filename = "meta-information.json"
source_info_filename = "source-information.json"

dir = "urdf_files"
subdirs = _get_subdirectories(dir)

for d in subdirs:
    list_of_meta_file_paths = _get_files_with(d, meta_info_filename)
    list_of_source_file_paths = _get_files_with(d, source_info_filename)
    assert len(list_of_source_file_paths) == 1, f"Error, expecting one source information file in subdataset, but found either more or none: {list_of_source_file_paths}"
    for file in list_of_meta_file_paths:
        meta_infos = _extract_meta_information(file, dataframe_columns)
        meta_infos['source'] = _extract_source_information(list_of_source_file_paths[0])
        dataset_information = pd.concat([dataset_information, meta_infos], ignore_index=True)
        

dataset_sources_n_robots = dataset_information[['name','source']].groupby(by='source').count()
dataset_sources_n_robots = dataset_sources_n_robots.reset_index().rename({'index':'source','name':'n_robots'}, axis='columns')
n_urdfs = list(dataset_information[['source','n_urdfs']].groupby(by='source').sum().n_urdfs)
dataset_sources_n_robots['n_urdfs'] = n_urdfs
dataset_sources_n_robots = dataset_sources_n_robots[['source','n_urdfs','n_robots']]

types_n_source_information = pd.DataFrame(dataset_information.groupby(['type','source']).count())
types_information = dataset_information[['type']]['type'].value_counts()
types_information = types_information.reset_index().rename({'index':'type', 'type':'count'}, axis = 'columns')
manufacturers_n_source_information = pd.DataFrame(dataset_information.groupby(['manufacturer','source']).count())
manufacturers_information = dataset_information['manufacturer'].value_counts()
manufacturers_information = manufacturers_information.reset_index().rename({'index':'manufacturer', 'manufacturer':'count'}, axis = 'columns')
robots_information = dataset_information['name'].value_counts()
robots_information = robots_information.reset_index().rename({'index':'name', 'name':'count'}, axis = 'columns')


n_original_robots = (dataset_information['variant'].values == None).sum()
n_all_robots = len(dataset_information)
robots = dataset_information.set_index(['name','variant'])
original_robots = dataset_information[dataset_information['variant'].isna()]
varianted_robots = dataset_information[dataset_information['variant'].notna()]
n_varianted_robots = varianted_robots['name'].value_counts() # n varianted robots of each type
duplicate_original_robots = (original_robots.groupby('name').filter(lambda g: len(g) > 1).drop_duplicates(subset=['name', 'source'], keep="first")).sort_values(by=['name'])
duplicate_original_robots = (duplicate_original_robots.groupby('name').filter(lambda g: len(g) > 1).drop_duplicates(subset=['name', 'source'], keep="first")).sort_values(by=['name']) # to make sure it is only the duplicate robots)
duplicate_varianted_robots = (varianted_robots.groupby('name').filter(lambda g: len(g) > 1).drop_duplicates(subset=['name', 'source'], keep="first")).sort_values(by=['name'])
duplicate_varianted_robots = (duplicate_varianted_robots.groupby('name').filter(lambda g: len(g) > 1).drop_duplicates(subset=['name', 'source'], keep="first")).sort_values(by=['name'])
duplicate_robots = pd.concat([duplicate_original_robots,duplicate_varianted_robots])
n_duplicate_robots = (duplicate_robots['name'].value_counts()).reset_index().rename({'index': 'name','name':'n_duplicates'}, axis='columns')
# duplicate_robots.to_csv("duplicate_robots.csv",index=False)
n_duplicate_robots.to_csv("n_duplicate_robots.csv",index=False)

n_unique_robots = dataset_information[['name','variant']]
n_unique_robots = n_unique_robots.fillna('original')
n_unique_robots_count = n_unique_robots.value_counts()
n_total_unique_robots = len(n_unique_robots_count)
print(f"n_total_unique_robots: {n_total_unique_robots}")
n_unique_robots_count.to_csv("n_unique_robots_count.csv")

duplicate_robots_json = {'robots': []}
duplicate_robots = duplicate_robots.replace(np.nan, 'original')
a = (duplicate_robots.groupby(['name','variant'])['type','manufacturer','source','urdf_path']
       .apply(lambda x: x.to_dict('r'))
       .reset_index(name='data')
       .groupby('name')['variant','data']
       .apply(lambda x: x.set_index('variant')['data'].to_dict())
       .to_json()
       ).replace("\\","")
with open("duplicates.json", 'w') as f:
    json.dump(eval(a), f)

print(manufacturers_information)

def _generate_plots():
    import matplotlib.pyplot as plt
    import numpy as np
    import altair as alt
    # df = manufacturers_information.sort_values(by=['count'])
    # bars = alt.Chart(df).mark_bar().encode(
    # y=alt.Y('manufacturer:N', sort='x',title=''),
    # x=alt.X("count:Q",title='number of robots')
    # )# .properties(height=700)

    # text = bars.mark_text(
    # align='left',
    # baseline='middle',
    # dx=3  # Nudges text to right so it doesn't appear on top of the bar
    # ).encode(text='count:Q')

    # (bars + text).properties(title='Distribution of robots from different manufacturers in dataset').show() 

    sorted_sources = ["ros-industrial","matlab","robotics-toolbox","drake","oems","random"]
    manufacturer_plotting_information = dataset_information[['manufacturer','source']] # extract manufacturer and source
    manufacturer_plotting_information = manufacturer_plotting_information.groupby(["source", "manufacturer"]).size().reset_index(name="count")
    manufacturer_plotting_information.source = manufacturer_plotting_information.source.astype("category")
    manufacturer_plotting_information.source = manufacturer_plotting_information.source.cat.set_categories(sorted_sources)
    manufacturer_plotting_information.sort_values(['source'])

    df = manufacturer_plotting_information
    bars = alt.Chart(df).mark_bar().encode(
        y=alt.Y('manufacturer:N', sort='x',title=''),
        x=alt.X("count:Q",title='number of robots'),

        color=alt.Color('source:N',sort=sorted_sources,
                scale=alt.Scale(
                    # make it look pretty with an enjoyable color pallet
                    range=['#96ceb4', '#ffcc5c','#ff6f69', '#AADBFF', '#51A8E1','#B97231'],
                ),
                legend=alt.Legend(
        orient='none',
        legendX=300, legendY=5,
        direction='vertical',
        titleAnchor='start',
        fillColor='white')
                
    ),
    order=alt.Order('color_source_sort_index:Q')) # for sorting the color in the chart https://stackoverflow.com/questions/66347857/sort-a-normalized-stacked-bar-chart-with-altair/66355902#66355902


    (bars).properties(title='Distribution of robots from different manufacturers in dataset').show()
    # (bars + text).properties(title='Distribution of robots from different manufacturers in dataset').show() 


    # for manufacturers
    # manufacturers = list(manufacturers_information['manufacturer'])
    # n_manufacturers = list(manufacturers_information['count'])

    # plt.rcdefaults()
    # fig, ax = plt.subplots()    
    # width = 0.75 # the width of the bars 
    # ind = np.arange(len(n_manufacturers))  # the x locations for the groups
    # bars = ax.barh(ind, n_manufacturers, width, color="blue")
    # ax.bar_label(bars)
    # ax.set_yticks(ind)
    # ax.set_yticklabels(manufacturers, minor=False)
    # plt.title('Distribution of robots from different manufacturers in dataset')
    # plt.xlabel('number of robots from manufacturer in dataset')
    # plt.savefig("manufacturers_information"+".svg", bbox_inches='tight')
    # plt.show()

    #################
    # for types  

    types_plotting_information = dataset_information[['type','source']] # extract type and source
    types_plotting_information = types_plotting_information.groupby(["source", "type"]).size().reset_index(name="count")
    types_plotting_information.source = types_plotting_information.source.astype("category")
    types_plotting_information.source = types_plotting_information.source.cat.set_categories(sorted_sources)
    types_plotting_information.sort_values(['source'])

    # x=alt.X("count:Q",title='number of robots', scale=alt.Scale(domain=[0, max(list(types_information['count']))], nice=False), axis=alt.Axis(values=list(types_information['count']))),

    df = types_plotting_information
    bars = alt.Chart(df).mark_bar().encode(
        y=alt.Y('type:N', sort='-x',title=''),
        x=alt.X("count:Q",title='number of robots'), #scale=alt.Scale(domain=[0, 198], nice=False), axis=alt.Axis(values=[198,23,20,11,9,8,4,1])),

        color=alt.Color('source:N',sort=sorted_sources,
                scale=alt.Scale(
                    # make it look pretty with an enjoyable color pallet
                    range=['#96ceb4', '#ffcc5c','#ff6f69', '#AADBFF', '#51A8E1','#B97231'],
                ),
                legend=alt.Legend(
        orient='none',
        legendX=300, legendY=60,
        direction='vertical',
        titleAnchor='start',
        fillColor='white')
                
    ),
    order=alt.Order('color_source_sort_index:Q')) # for sorting the color in the chart https://stackoverflow.com/questions/66347857/sort-a-normalized-stacked-bar-chart-with-altair/66355902#66355902


    (bars).properties(title='Distribution of robot types from sources in dataset')

      
    # types = list(types_information['type'])
    # n_types = list(types_information['count'])
    # fig, ax = plt.subplots()
    # width = 0.75
    # ind = np.arange(len(n_types))  # the x locations for the groups
    # bars = ax.barh(ind, n_types, width, color="blue")
    # ax.bar_label(bars)
    # ax.set_yticks(ind)
    # ax.set_yticklabels(types, minor=False)
    # plt.title('Distribution of types of robots in dataset')
    # plt.xlabel('amount of specific robot type in dataset')
    # plt.savefig("types_information"+".svg", bbox_inches='tight')
    # plt.show()




if GENERATE_CSVS:
    dataset_information.to_csv("dataset_information.csv", index=False)
    types_information.to_csv("types_information.csv", index=False)
    manufacturers_information.to_csv("manufacturers_information.csv", index=False)
    robots_information.to_csv("robots_information.csv", index=False)
    dataset_sources_n_robots.to_csv("dataset_sources_n_robots.csv", index=False)
    types_n_source_information.to_csv("types_n_source_information.csv")
    manufacturers_n_source_information.to_csv("manufacturers_n_source_information.csv")

if GENERATE_PLOTS:
    _generate_plots()