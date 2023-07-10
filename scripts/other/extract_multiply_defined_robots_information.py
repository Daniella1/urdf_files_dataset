import json
import pandas as pd
import subprocess


multiply_defined_robots_filename = "multiply_defined.json" 
with open(multiply_defined_robots_filename, 'r') as f:
    multiply_defined_robots = json.load(f)


## initialise parser
def check_urdf(filename):
    res = subprocess.run(f'check_urdf {filename}', shell=True, capture_output=True, text=True)
    if res.returncode == 0: # success
        return res.stdout
    else:
        return None

####

multiply_defined_robots_parsing_information = pd.DataFrame(columns=['name','variant','sources_passed','sources_failed', 'all_sources', 'failed_files'])


for robot in multiply_defined_robots:
    for variant in multiply_defined_robots[robot]:
        sources_passing = {'name':robot,'variant': variant,'sources_passed': [], 'sources_failed':[], 'all_sources': [],'failed_files': []}
        for duplicate in multiply_defined_robots[robot][variant]:
            n_sources = len(multiply_defined_robots[robot][variant])
            urdf_files = list(map(str.strip, duplicate['urdf_path'].strip('][').replace('"', '').split(',')))
            for urdf_file in urdf_files:
                urdf_file = urdf_file.strip("WindowsPath('")
                urdf_file = urdf_file.strip("')")
                res = check_urdf(str(urdf_file))
                source = duplicate['source']
                if res is not None:
                    sources_passing['sources_passed'].append(source)
                else:
                    sources_passing['sources_failed'].append(source)
                    sources_passing['failed_files'].append(urdf_file)
                sources_passing['all_sources'].append(source)

        multiply_defined_robots_parsing_information = pd.concat([multiply_defined_robots_parsing_information, pd.Series(sources_passing).to_frame().T], ignore_index=True)
                

multiply_defined_robots_parsing_information.to_csv("multiply_defined_robots_parsing_information.csv",index=False)

