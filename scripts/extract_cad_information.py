import os
import pandas as pd
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

########### Extract CAD information
source = "random"
dir = f"urdf_files/{source}"
root_dir = os.getcwd()

urdf_files = _get_files_with(dir, "*.urdf")    
mesh_analysis_results = get_cad_information(urdf_files)
# mesh_analysis_results.to_csv(f"mesh_analysis_results_{source}.csv")