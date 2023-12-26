import os
import pandas as pd
from urdf_analyzer import api

sources = ["ros-industrial","matlab","robotics-toolbox","drake","oems","random"]
parsers = api.URDFparser.supported_parsers
urdf_res = pd.DataFrame(index=sources+["total"],columns=parsers)

for src in sources:
    urdf_search_dir = f"urdf_files/{src}"
    urdf_files = api.search_for_urdfs(urdf_search_dir)
    urdf_parsing_res = api.generate_urdf_parsing_comparison_schema(urdf_files, out=f"urdf_parsing_{src}.csv") # TODO: change when the urdf_analyzer tool is updated to handle no output file
    os.remove(f"urdf_parsing_{src}.csv")

    for parser in parsers:
        res = urdf_parsing_res[parser].value_counts()
        try:
            res = res[True]
        except:
            res = 0
        urdf_res.loc[src,parser] = res

urdf_res.loc['total'] = urdf_res.sum()
urdf_res.to_csv("table_xiii_urdf_parsers.csv")
