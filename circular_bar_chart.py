import json
import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
from clean import CleanData
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from datetime import datetime, timedelta
# proprocess the data
# .sort_values(by='videoMeta.duration',axis=1)#.plot(kind="bar", legend=False)
data = json.load(open('./data/trending.json', encoding="utf8"))
data = data['collector']
toParse = pd.json_normalize(data)
df = CleanData(toParse)
df.process_the_data()
df.summary_of_data()
df_clean = df.dfm
# df_clean.sort_values(by=['likeCount'],ascending=False).head(1).T
df_clean.info()

count_df = df_clean[['videoMeta.duration']].groupby(
    df_clean["videoMeta.duration"]).count()
count_df = count_df.rename(columns={"videoMeta.duration": "count"})
count_df = count_df.reset_index()

avg_df = df_clean[['videoMeta.duration',
                   'likeRate', 'shareRate', 'commentRate']]
avg_df = avg_df.groupby(['videoMeta.duration'], as_index=False).agg(
    [np.mean]).reset_index()
avg_df.columns = avg_df.columns.droplevel(-1)
avg_df

fig = plt.figure(figsize=(16, 48), constrained_layout=True)

ax1 = fig.add_subplot(131, projection='polar')
ax2 = fig.add_subplot(132, projection='polar')
ax3 = fig.add_subplot(133, projection='polar')


def draw_circular_bar(ax, x, y, title, lower_limit, curve_position, text_position):
    ax.set_theta_direction(-1)
    ax.set_xticks(np.arange(0, 2*np.pi, np.pi/2))
    ax.set_xticklabels(["60s", "15s", "30s", "45s"])
    ax.set_theta_zero_location('N')
    for _x, _y in zip(x, y):
        # _x = _x + np.pi/30
        _x_second = _x
        _x = _x*np.pi/30
        if _x <= np.pi/2:
            ax.bar(x=_x, height=_y, width=np.pi/30,
                   color='#fcbcbb', bottom=lower_limit,edgecolor='white')
        elif _x > np.pi/2 and _x <= np.pi:
            ax.bar(x=_x, height=_y, width=np.pi/30,
                   color='#c2d794', bottom=lower_limit,edgecolor='white')
        elif _x > np.pi and _x <= np.pi*3/2:
            ax.bar(x=_x, height=_y, width=np.pi/30,
                   color='#99dee1', bottom=lower_limit,edgecolor='white')
        else:
            ax.bar(x=_x, height=_y, width=np.pi/30,
                   color='#e3bfff', bottom=lower_limit,edgecolor='white')
        if _x_second <= 30:
            ax.text((_x_second-0.25)/30*np.pi, _y+lower_limit*1.1,rotation=-np.rad2deg((_x_second-0.25)/30*np.pi+np.pi/2*3),s ="{:.3%}".format(_y),size=6 ,ha = "left",rotation_mode='anchor',va="center") #TODO
        else:
            ax.text((_x_second-0.25)/30*np.pi, _y+lower_limit*1.1,rotation=-np.rad2deg((_x_second-0.25)/30*np.pi+np.pi/2),s ="{:.3%}".format(_y),size=6 ,ha ="right",rotation_mode='anchor',va ="center") #TODO
        
    # draw the curve
    x = np.linspace(np.pi/30+0.15*np.pi, np.pi/2 - np.pi/40, 100)
    y = np.full(len(x), curve_position)
    ax.plot(x, y, color='black', linewidth=1, alpha=0.8)  # draw the curve
    # ax.text(x=np.pi/4, y=0.000774233508826262, s="<15s",ha="left",
    #         va='center',
    #         rotation=np.pi/4,
    #         rotation_mode="anchor")
    ax.text(x=np.pi/2-np.pi/12, y=text_position, s='<15 s', rotation=-
            54, rotation_mode='anchor', va='center', ha='right', size=8)
    # # curve between 15s to 30s
    x = np.linspace(np.pi/2 + np.pi/20, np.pi - np.pi/40, 100)
    y = np.full(len(x), curve_position)
    ax.plot(x, y, color='black', linewidth=1, alpha=0.8)  # draw the curve
    ax.text(x=np.pi-np.pi/10, y=text_position, s='15-30 s', rotation=-
            144, rotation_mode='anchor', va='center', ha='right', size=8)
    # # curve between 30s to 45s
    x = np.linspace(np.pi + np.pi/20, 3*np.pi/2-np.pi/40, 100)
    y = np.full(len(x), curve_position)
    ax.plot(x, y, color='black', linewidth=1, alpha=0.8)  # draw the curve
    ax.text(x=np.pi + np.pi/10, y=text_position, s='31-45 s', rotation=144,
            rotation_mode='anchor', va='center', ha='left', size=8)
    # # curve between 45s to 60s
    x = np.linspace(3*np.pi/2+np.pi/20, 2*np.pi-np.pi/40, 100)
    y = np.full(len(x), curve_position)
    ax.plot(x, y, color='black', linewidth=1, alpha=0.8)  # draw the curve
    ax.text(x=3*np.pi/2 + np.pi/10, y=text_position, s='46-60 s',
            rotation=54, rotation_mode='anchor', va='center', ha='left', size=8)
    # add title
    # remove the axis
    ax.set_xticks([])
    ax.set_title(title, fontsize=16)
    ax.axis('off')


draw_circular_bar(ax1, avg_df["videoMeta.duration"],
                  avg_df["shareRate"], "Share Rate", 0.003, 0.003,0.0025)
draw_circular_bar(ax2, avg_df["videoMeta.duration"],
                  avg_df["likeRate"], "Like Rate", 0.098, 0.098,0.076)
draw_circular_bar(ax3, avg_df["videoMeta.duration"],
                  avg_df["commentRate"], "Comment Rate", 0.0025, 0.0025,0.002)
plt.axis('off')
plt.show()
