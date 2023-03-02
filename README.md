# A URDF Dataset

This repository contains a dataset of URDF Collections from various sources.
All the URDF Collections can be found in the subdirectory _urdf\_files_.
We have manually constructed a duplicates directory containing the robots with duplicate URDF Collections from different sources. This can be found in the _duplicates_ subdirectory.
Scripts for producing analysis results on the dataset, can be found in the _scripts_ subdirectory.

### Source and Meta Information
Source and meta information files describe the source of the URDF Collection, a link to the source origin, name of the robot, manufacturer, and whether or not the file was manually xacro generated.

### Obtaining Analysis Results
The following table shows the information, which scripts to generate the information, and the resulting CSV file that contains the results.

<table>
    <tr>
        <td><b>Information</b></td>
        <td><b>Script (.py)</b></td>
        <td><b>Results CSV</b></td>
    </tr>
    <tr>
        <td>Sources and URDF files</td>
        <td><tt>extract_dataset_information</tt></td>
        <td><em>dataset_sources_n_robots</em></td>
    </tr>
    <tr>
        <td>Robot types</td>
        <td><tt>extract_dataset_information</tt></td>
        <td><em>types_information</em></td>
    </tr>
    <tr>
        <td>Manufacturers</td>
        <td><tt>extract_dataset_information</tt></td>
        <td><em>manufacturers_information</em></td>
    </tr>
    <tr>
        <td>Common folder structures</td>
        <td>Manual process</td>
        <td><em>folder_structure_information</em></td>
    </tr>
    <tr>
        <td>Source xacro generated</td>
        <td><tt>extract_xacro_information</tt></td>
        <td><em>source_xacro_information</em></td>
    </tr>
    <tr>
        <td>Manufacturer xacro generated</td>
        <td><tt>extract_xacro_information</tt></td>
        <td><em>manufacturer_xacro_information</em></td>
    </tr>
    <tr>
        <td>Duplicate robots</td>
        <td><tt>extract_duplicates_information</tt></td>
        <td><em>duplicates_parsing_information</em></td>
    </tr>
    <tr>
        <td>Identical files</td>
        <td><tt>extract_fdupe_information</tt></td>
        <td><em>fdupe_duplicates_res_EXT</em></td>
    </tr>
    <tr>
        <td>URDF parsing errors</td>
        <td><tt>extract_ROS_parsing_issues</tt></td>
        <td><em>ros_parsing_errors</em></td>
    </tr>
    <tr>
        <td>URDF parsing warnings</td>
        <td><tt>extract_ROS_parsing_issues</tt></td>
        <td><em>ros_parsing_warnings</em></td>
    </tr>
    <tr>
        <td>CAD file types</td>
        <td><tt>extract_cad_information</tt></td>
        <td><em>mesh_analysis_results_SOURCE</em></td>
    </tr>
    <tr>
        <td>Joint and link count</td>
        <td><tt>get_model_structure_information</tt></td>
        <td><em>robot_type_model_information</em></td>
    </tr>
    <tr>
        <td>Word count in names of joints and links</td>
        <td><tt>get_model_structure_information</tt></td>
        <td><em>source_model_name_information</em></td>
    </tr>
</table>


## Creating the dataset

"variants" was defined by looking at the urdf file names and using them to define the variants of a robot.
An example of how a variant was defined, 
drake/atlas/urdf has both 'atlas_convex_hull.urdf' and 'atlas_minimal_contact.urdf', and as this is the exact same physical robot, but with modifications to the urdf file, we have defined them as variants of the robot.
If there are robots such as ros-industrial/xacro_generated/abb/abb_irb52_support/urdf/ 'irb52_7_120.urdf' and 'irb52_7_145.urdf', we do not define them as different variants, as they are original robots with different characteristics, and have nothing to do with their urdf implementation.

<!-- "Variants" are defined by a robot with various features, e.g. the same robot but with extended or different features, this could be the payload, workspace, force, etc.
An example of this is the 
If there are robots such as ros-industrial/xacro_generated/abb/abb_irb52_support/urdf/ 'irb52_7_120.urdf' and 'irb52_7_145.urdf' they are defined as robot: 'irb52 7' with the modifications '120' and '145'.

Would the drake/allegro_hand_description/urdf/ be a modification or variation -->

### Contributing
Create a pull request with the URDF Collection or source.

Suggestions for a new structure of the dataset are welcome.


