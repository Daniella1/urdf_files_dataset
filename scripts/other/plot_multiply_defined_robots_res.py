import numpy as np
import pandas as pd
import altair as alt


sorted_sources = ['ros-industrial','matlab','robotics-toolbox','drake','oems','random']
source_multiply_defined_info = pd.DataFrame(pd.Series({'source':'ros-industrial',
                                                'number of robots': 13,
                                                'number of robots with parsing issues': 0}).to_frame().T)

source_multiply_defined_info = pd.concat([source_multiply_defined_info,pd.Series({'source':'matlab','number of robots':36,'number of robots with parsing issues':0}).to_frame().T],ignore_index=True)
source_multiply_defined_info = pd.concat([source_multiply_defined_info,pd.Series({'source':'robotics-toolbox','number of robots':11,'number of robots with parsing issues':1}).to_frame().T],ignore_index=True)
source_multiply_defined_info = pd.concat([source_multiply_defined_info,pd.Series({'source':'drake','number of robots':3,'number of robots with parsing issues':1}).to_frame().T],ignore_index=True)
source_multiply_defined_info = pd.concat([source_multiply_defined_info,pd.Series({'source':'oems','number of robots':24,'number of robots with parsing issues':1}).to_frame().T],ignore_index=True)
source_multiply_defined_info = pd.concat([source_multiply_defined_info,pd.Series({'source':'random','number of robots':12,'number of robots with parsing issues':1}).to_frame().T],ignore_index=True)

source_multiply_defined_info.source = source_multiply_defined_info.source.astype("category")
source_multiply_defined_info.source = source_multiply_defined_info.source.cat.set_categories(sorted_sources)
source_multiply_defined_info = source_multiply_defined_info.sort_values(['source'])

yval = [13,36,11,3,24,12]#list(source_multiply_defined_info['number of robots'])
bar = alt.Chart(source_multiply_defined_info).mark_bar().encode(
    y=alt.Y('source:N', sort='-x', axis=alt.Axis(titlePadding=1)),
    x=alt.X('number of robots:Q',   ), # axis=alt.Axis(values=yval) , scale=alt.Scale(domain=[0, 43], nice=False),
           color=alt.Color('source:N',sort=sorted_sources,
            scale=alt.Scale(
                # make it look pretty with an enjoyable color pallet
                range=['#96ceb4', '#ffcc5c','#ff6f69', '#AADBFF', '#51A8E1','#B97231'],
            ),
            legend=None
        ),
        # order=alt.Order('color_source_sort_index:Q')
)

tick = alt.Chart(source_multiply_defined_info).mark_tick(
    color='red',
    thickness=2,
    size=20 * 0.9,  # controls width of tick.
).encode(
    y=alt.Y('source', sort='-x'),
    x=alt.X('number of robots with parsing issues'), # scale=alt.Scale(domain=[0, 43], nice=False), axis=alt.Axis(values=list(source_multiply_defined_info['number of robots with parsing issues']))
)

(bar + tick).properties(title='Multiply Defined Robot URDF Bundles')

print(source_multiply_defined_info)


x = ['number of joints','number of links','CAD file type','forward kinematics','number of lines','any','any excl. lines']
y = [11, 11, 6, 15, 36, 36, 16]

multiply_defined_diff_info = pd.DataFrame(pd.Series({'differences': x[0], 'n_robots': y[0]}).to_frame().T)
for i in range(1, len(x)):
    multiply_defined_diff_info = pd.concat([multiply_defined_diff_info, pd.Series({'differences': x[i], 'n_robots': y[i]}).to_frame().T], ignore_index=True)

y.append(43)
bar = alt.Chart(multiply_defined_diff_info).mark_bar().encode(
    x=alt.X('n_robots:Q', title='number of multiply defined robots with differences in features'), # scale=alt.Scale(domain=[0, 43], nice=False), axis=alt.Axis(values=y)
    y=alt.Y('differences:N',  title="features", sort='-x'), # axis=alt.Axis(titlePadding=25),
).properties(title="Differences between URDF Collection features of robot multiply_defined").show()
print(multiply_defined_diff_info)
multiply_defined_diff_info.to_csv("multiply_defined_diff_info.csv",index=False)
