import json
import pandas as pd
import altair as alt
from helper_functions import _get_files_with, _get_subdirectories

def _extract_meta_information(filename, columns):
    meta_infos = pd.DataFrame(columns=columns)
    with open(filename, 'r') as f:
        data = json.load(f)
    robots = data['robots']
    for robot in robots:
        meta_infos = pd.concat([meta_infos, pd.Series({'name':robot['name'], 'manufacturer':robot['manufacturer']}).to_frame().T], ignore_index=True)
    return meta_infos

def _extract_source_information(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['source']

####

dataframe_columns = ['manufacturer','source']
manufacturer_information = pd.DataFrame(columns=dataframe_columns)

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
        manufacturer_information = pd.concat([manufacturer_information, meta_infos], ignore_index=True)
        

manufacturers_n_source_information = pd.DataFrame(manufacturer_information.groupby(['manufacturer','source']).count())
manufacturers_n_source_information = manufacturers_n_source_information.reset_index().rename({'name':'count'},axis='columns')
manufacturer_n_robots = manufacturer_information['manufacturer'].value_counts()
manufacturer_n_robots = manufacturer_n_robots.reset_index().rename({'index':'manufacturer', 'manufacturer':'count'}, axis = 'columns')

manufacturer_n_robots.to_csv("manufacturer_n_robots.csv",index=False)
manufacturers_n_source_information.to_csv("fig_7_manufacturers_n_source_information.csv",index=False)



sorted_sources = ["ros-industrial","matlab","robotics-toolbox","drake","oems","random"]
manufacturers_n_source_information.source = manufacturers_n_source_information.source.astype("category")
manufacturers_n_source_information.source = manufacturers_n_source_information.source.cat.set_categories(sorted_sources)
manufacturers_n_source_information.sort_values(['source'])

df = manufacturers_n_source_information
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

