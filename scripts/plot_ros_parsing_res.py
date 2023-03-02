import matplotlib.pyplot as plt
import numpy as np



##### PLOTTING

issues = ["Issue with joint limits", "No link elements found in urdf file", "Non-unique link", "No name given for robot", "Parent link not found"]
issues = ["(A)","(B)","(C)","(D)","(E)"]
source_urdfs_per_issue = [['drake','drake'],['random', 'random', 'robotics-toolbox', 'robotics-toolbox'],['random'],['oems'],['random']]
n_urdfs_per_issue = [len(sources) for sources in source_urdfs_per_issue]
sources_pr_issue = [set(sources) for sources in source_urdfs_per_issue]
n_sources_pr_issue = np.array([len(sources) for sources in sources_pr_issue])




print(n_urdfs_per_issue)
print(n_sources_pr_issue)
print(sources_pr_issue)

plt.rcParams.update({'font.size': 12})

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))
sizes = np.array(n_urdfs_per_issue)
colors = ['#FF7F0E', '#1F77B4','#D62728','#2CA02C', '#9467BD']
labels_subgroup = ['drake','random','robotics-toolbox','random','oems','random']#['product A', 'product B', 'product C', 'product D', 'product E', 'product F', 'product G']
sizes_subgroup = [2,2,2,1,1,1] # [20, 15, 10, 20, 15, 10, 10]
colors_subgroup = ['#FDB55B', '#AADBFF', '#51A8E1','#FF877D', '#72D872','#C5ACDB']

def outer_circle_absolute_value(val):
    a = int(np.round(val/100.*sizes.sum(), 0))
    return a

def inner_circle_absoluate_value(val):
    a = int(np.round(val/100.*n_sources_pr_issue.sum(), 0))
    return a
 
outside_donut = plt.pie(sizes, labels=issues, colors=colors,startangle=90, frame=True,pctdistance =0.85,autopct=outer_circle_absolute_value,wedgeprops=dict(width=0.5)) # labels=issues
# for t in outside_donut[1]:
#     t.set_horizontalalignment('center')
#     t.set_verticalalignment('center')
    # t.set_rotation(15)
# outside_donut[1][1].set_horizontalalignment('left')
inside_donut = plt.pie(sizes_subgroup, labels=labels_subgroup,colors=colors_subgroup, radius=0.7,startangle=90, labeldistance=0.76,pctdistance =0.85)
for t in inside_donut[1]:
    t.set_horizontalalignment('center')
centre_circle = plt.Circle((0, 0), 0.4, color='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
# kw = dict(arrowprops=dict(arrowstyle="-"),bbox=bbox_props, zorder=0, va="center")
# for i, p in enumerate(outside_donut[0]):
    
#     ang = (p.theta2 - p.theta1)/2. + p.theta1
#     y = np.sin(np.deg2rad(ang))
#     x = np.cos(np.deg2rad(ang))
#     horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
#     connectionstyle = "angle,angleA=0,angleB={}".format(ang)
#     kw["arrowprops"].update({"connectionstyle": connectionstyle})
#     ax.annotate(issues[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
#                 horizontalalignment=horizontalalignment, **kw)
 
plt.axis('equal')
plt.tight_layout()
plt.title('ROS Parsing Errors of URDF Files')
fig.tight_layout()
fig.subplots_adjust(top=0.65)
plt.savefig("piechart_urdf_parsing_issues1"+".svg", bbox_inches='tight')
plt.show()

