import os
import pandas as pd
import altair as alt
import xml.etree.ElementTree as ET
from helper_functions import _get_files_with


def xml_urdf_reader(path):
    root_dir = os.getcwd()
    basename = os.path.abspath(path)
    dirname = os.path.dirname(basename)
    filename = os.path.basename(basename)
    try:
        os.chdir(dirname)
        tree = ET.ElementTree(file=filename)
    except:
        print(f"error while loading {basename}")
        tree = None
        pass
    os.chdir(root_dir)
    if tree is None:
        return None
    root = tree.getroot()
    return root

def _get_mesh_type_from(tag_names, visualisation_type):
    vis_type = tag_names[visualisation_type]
    try:
        return os.path.splitext((list(vis_type.iter("mesh"))[0].attrib['filename']))[-1][1:]
    except:
        return None

def _add_mesh_info(mesh_link_dict, link_name, mesh_type, tag_names):
    if mesh_type in tag_names:
        cur_mesh_type = _get_mesh_type_from(tag_names,mesh_type)
        if cur_mesh_type is not None:
            mesh_link_dict[link_name] = cur_mesh_type.lower()
        else:
            mesh_link_dict[link_name] = None
    return mesh_link_dict


def get_link_information(root):
    links_visual = {}
    links_collision = {}
    for link in root.iter("link"):
        link_name = link.attrib["name"]
        tag_names = {x.tag:x for x in link.iter("*")}
        links_visual = _add_mesh_info(links_visual, link_name, "visual", tag_names)
        links_collision = _add_mesh_info(links_collision, link_name, "collision", tag_names)
    return links_visual, links_collision

def _count_mesh_types_urdf(counter_dict, mesh_set):
    if len(mesh_set) > 0:
        for mesh_type in mesh_set:
            if mesh_type is None:
                continue
            if mesh_type in counter_dict:
                counter_dict[mesh_type] += 1
            else:
                counter_dict[mesh_type] = 1
    return counter_dict


def _insert_mesh_results(dataframe_results, mesh_type_column, mesh_use_row, count_mesh_types, n_urdf_files_analysed):
    if mesh_type_column in count_mesh_types:
        dataframe_results.at[mesh_use_row,str(mesh_type_column)] = f"{count_mesh_types[mesh_type_column]}/{n_urdf_files_analysed}"
    else:
        dataframe_results.at[mesh_use_row,str(mesh_type_column)] = f"0/{n_urdf_files_analysed}"
    return dataframe_results


def get_cad_information(list_of_urdf_file_paths):
    count_visual_mesh_types = {}
    count_collision_mesh_types = {}
    n_urdf_files_analysed = 0
    
    for urdf_path in list_of_urdf_file_paths:
        # Analyse link and joints of urdf file
        root = xml_urdf_reader(urdf_path)
        if root is None:
            continue
        visual_links, collision_links = get_link_information(root)

        visual_mesh_types = set(visual_links.values())
        collision_mesh_types = set(collision_links.values())
        count_visual_mesh_types = _count_mesh_types_urdf(count_visual_mesh_types, visual_mesh_types)
        count_collision_mesh_types = _count_mesh_types_urdf(count_collision_mesh_types, collision_mesh_types)
        n_urdf_files_analysed += 1

    # results on mesh types in urdfs
    mesh_analysis_column_names = list(set(list(count_collision_mesh_types.keys()) + list(count_visual_mesh_types.keys())))
    mesh_analysis_results = pd.DataFrame(index=["visual","collision"], columns=mesh_analysis_column_names)
    for mesh_type in mesh_analysis_column_names:
        mesh_analysis_results = _insert_mesh_results(mesh_analysis_results, mesh_type, "visual", count_visual_mesh_types, n_urdf_files_analysed)
        mesh_analysis_results = _insert_mesh_results(mesh_analysis_results, mesh_type, "collision", count_collision_mesh_types, n_urdf_files_analysed)
    
    return mesh_analysis_results


#### Extract and plot information


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
            title='number of URDF Bundles using the different CAD file types')),

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