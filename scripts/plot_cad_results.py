import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
from extract_cad_information import get_cad_information
from helper_functions import _get_files_with


sources = ["drake","matlab","oems","random","robotics-toolbox","ros-industrial"]
dir = f"urdf_files/"
mesh_analysis_results_all_sources = {}
cad_types = ['stl','dae','obj']

for source in sources:
    urdf_files = _get_files_with(f"{dir}/{source}", "*.urdf")
    mesh_analysis_results_all_sources[source] = get_cad_information(urdf_files)

    missing_cads = list(set(cad_types) - set(list(mesh_analysis_results_all_sources[source].columns)))
    for m in missing_cads:
        mesh_analysis_results_all_sources[source][m] = '0'
    mesh_analysis_results_all_sources[source] = mesh_analysis_results_all_sources[source][['stl','dae','obj']] # sort the columns, i.e. cad file types: stl, dae, obj

    for cad in mesh_analysis_results_all_sources[source].columns:
        mesh_analysis_results_all_sources[source][cad]['visual'] = int(mesh_analysis_results_all_sources[source][cad]['visual'].split("/")[0])
        mesh_analysis_results_all_sources[source][cad]['collision'] = int(mesh_analysis_results_all_sources[source][cad]['collision'].split("/")[0])
    mesh_analysis_results_all_sources[source] = mesh_analysis_results_all_sources[source].sort_index(ascending=False) # sort the index, i.e. visual and collision meshes
 


indices = list(cad_types)
cols = ["visual","collision"]

# if the cad type is not in the source dataset

df_drake = pd.DataFrame(mesh_analysis_results_all_sources['drake'].to_numpy().T,index=indices,columns=cols)
df_matlab = pd.DataFrame(mesh_analysis_results_all_sources['matlab'].to_numpy().T,index=indices,columns=cols)
df_oems = pd.DataFrame(mesh_analysis_results_all_sources['oems'].to_numpy().T,index=indices,columns=cols)
df_random = pd.DataFrame(mesh_analysis_results_all_sources['random'].to_numpy().T,index=indices,columns=cols)
df_rtb = pd.DataFrame(mesh_analysis_results_all_sources['robotics-toolbox'].to_numpy().T,index=indices,columns=cols)
df_rosi = pd.DataFrame(mesh_analysis_results_all_sources['ros-industrial'].to_numpy().T,index=indices,columns=cols)

def prep_df(df, name):
    df = df.stack().reset_index()
    df.columns = ['c1', 'c2', 'values']
    df['source'] = name
    return df

df_drake = prep_df(df_drake, 'drake')
df_matlab = prep_df(df_matlab, 'matlab')
df_oems = prep_df(df_oems, 'oems')
df_random = prep_df(df_random, 'random')
df_rtb = prep_df(df_rtb, 'robotics-toolbox')
df_rosi = prep_df(df_rosi, 'ros-industrial')

df = pd.concat([df_rosi, df_matlab, df_rtb, df_drake, df_oems, df_random])

sorted_sources = ["ros-industrial","matlab","robotics-toolbox","drake","oems","random"]

total_mesh_cad_types = df[['c1','c2','values']]
total_mesh_cad_types = total_mesh_cad_types.groupby(['c2','c1']).values.sum().reset_index()
print(total_mesh_cad_types)
total_mesh_cad_types.to_csv("cad_mesh_information.csv", index=False)

# https://stackoverflow.com/questions/22787209/how-to-have-clusters-of-stacked-bars

#### horizontal grouped stacked bar chart
alt.Chart(df).mark_bar().encode(

    # tell Altair which field to group columns on
    y=alt.Y('c1:N', title=None, sort=cad_types),

    # tell Altair which field to use as Y values and how to calculate
    x=alt.X('sum(values):Q',
        axis=alt.Axis(
            grid=False,
            title='number of CAD files')),

    # tell Altair which field to use to use as the set of columns to be represented in each group
    row=alt.Column('c2:N', title=None, sort=cols,),

    # tell Altair which field to use for color segmentation 
    color=alt.Color('source:N',sort=sorted_sources,
            scale=alt.Scale(
                # make it look pretty with an enjoyable color pallet
                range=['#96ceb4', '#ffcc5c','#ff6f69', '#AADBFF', '#51A8E1','#B97231'],
            ),
            legend=alt.Legend(title=None,
        orient='none',
        legendX=0, legendY=-20,
        direction='horizontal',
        titleAnchor='middle',
        fillColor='white')
        ),
        order=alt.Order('color_source_sort_index:Q'))\
    .configure_view(
        # remove grid lines around column clusters
        strokeOpacity=0    
    ).show()



#### vertical grouped stacked bar chart

# # https://stackoverflow.com/questions/22787209/how-to-have-clusters-of-stacked-bars
# alt.Chart(df).mark_bar().encode(

#     # tell Altair which field to group columns on
#     x=alt.X('c1:N', title=None, sort=cad_types),

#     # tell Altair which field to use as Y values and how to calculate
#     y=alt.Y('sum(values):Q',
#         axis=alt.Axis(
#             grid=False,
#             title=None)),

#     # tell Altair which field to use to use as the set of columns to be  represented in each group
#     column=alt.Column('c2:N', title=None, sort=cols,),

#     # tell Altair which field to use for color segmentation 
#     color=alt.Color('source:N',
#             scale=alt.Scale(
#                 # make it look pretty with an enjoyable color pallet
#                 range=['#96ceb4', '#ffcc5c','#ff6f69', '#AADBFF', '#51A8E1','#B97231'],
#             ),
#         ))\
#     .configure_view(
#         # remove grid lines around column clusters
#         strokeOpacity=0    
#     ).show()