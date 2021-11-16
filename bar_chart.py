import json
import numpy as np
import pandas as pd
from clean import CleanData
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from datetime import datetime, timedelta

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.options.mode.chained_assignment = None
data = json.load(open('./data/trending.json', encoding="utf8"))
data = data['collector']
toParse = pd.json_normalize(data)
df = CleanData(toParse)
df.process_the_data()
df.summary_of_data()
df_clean = df.dfm
df_clean = df.dfm
# df_clean.sort_values(by=['likeCount'],ascending=False).head(1).T
df_clean.info()
segmentDf = df_clean[['authorMeta.name','authorMeta.verified','shareRate','likeRate','commentRate','playCount','shareCount','likeCount','commentCount']]
segmentDf = segmentDf.groupby(['authorMeta.name','authorMeta.verified'],as_index=False).agg(np.mean)
segmentDf = segmentDf.sort_values(by='likeRate',ascending=False)#.head(3).T
segmentDf.head(3).Tax1 = fig.add_subplot(131, projection='polar')
ax2 = fig.add_subplot(132, projection='polar')
def draw_circular_bar(ax, x, y, title,lower_limit):
    ax.set_theta_direction(-1)
    ax.set_xticks(np.arange(0, 2*np.pi, np.pi/2))
    ax.set_xticklabels(["60s", "15s", "30s", "45s"])
    ax.set_theta_zero_location('N')
    for _x, _y in zip(x, y):
        # _x = _x + np.pi/30
        _x_second = _x
        _x = _x*np.pi/30
        rotation = np.rad2deg(_x+np.pi/15+np.pi/30)
        if _x <= np.pi/2:
            ax.bar(x=_x, height=_y, width=np.pi/30,
                    color='#FBD1B7', bottom=lower_limit)
        elif _x > np.pi/2 and _x <= np.pi:
            ax.bar(x=_x, height=_y, width=np.pi/30,
                    color='#FEE9B2', bottom=lower_limit)
        elif _x > np.pi and _x <= np.pi*3/2:
            ax.bar(x=_x, height=_y, width=np.pi/30,
                    color='#F9FCE1', bottom=lower_limit)
        else:
            ax.bar(x=_x, height=_y, width=np.pi/30,
                    color='#D3F6F3', bottom=lower_limit)
    # draw the curve
    x = np.linspace(np.pi/30+0.15*np.pi, np.pi/2 - np.pi/40, 100)
    y = np.full(len(x), 0.0025)
    ax.plot(x, y, color='black', linewidth=1, alpha=0.8)  # draw the curve
    # ax.text(x=np.pi/4, y=0.000774233508826262, s="<15s",ha="left", 
    #         va='center', 
    #         rotation=np.pi/4, 
    #         rotation_mode="anchor")
    ax.text(x=np.pi/2-np.pi/12,y=0.002,s='<15 s',rotation=-54,rotation_mode='anchor',va='center',ha='right',size=8)
    # # curve between 15s to 30s
    x = np.linspace(np.pi/2 + np.pi/40, np.pi - np.pi/40, 100)
    y = np.full(len(x), 0.0025)
    ax.plot(x, y, color='black', linewidth=1, alpha=0.8)  # draw the curve
    ax.text(x=np.pi-np.pi/10, y=0.002,s='15-30 s',rotation=-144,rotation_mode='anchor',va='center',ha='right',size=8)
    # # curve between 30s to 45s
    x = np.linspace(np.pi + np.pi/40, 3*np.pi/2-np.pi/40, 100)
    y = np.full(len(x), 0.0025)
    ax.plot(x, y, color='black', linewidth=1, alpha=0.8)  # draw the curve
    ax.text(x=np.pi+ np.pi/10, y=0.002,s='31-45 s',rotation=144,rotation_mode='anchor',va='center',ha='left',size=8)
    # # curve between 45s to 60s
    x = np.linspace(3*np.pi/2+np.pi/40, 2*np.pi-np.pi/40, 100)
    y = np.full(len(x), 0.0025)
    ax.plot(x, y, color='black', linewidth=1, alpha=0.8)  # draw the curve
    ax.text(x=3*np.pi/2+ np.pi/10, y=0.002,s='31-45 s',rotation=54,rotation_mode='anchor',va='center',ha='left',size=8)
    # add title
    ax.set_title(title, fontsize=16)

ax2 = fig.add_subplot(132, projection='polar')
draw_circular_bar(ax1, x, y, "Share Rate",0.0025)
draw_circular_bar(ax2, avg_df["videoMeta.duration"], avg_df["likeRate"], "Like Rate", 0.0025)
plt.show()

pivot_df = df_clean[['createTime']].groupby(df_clean["createTime"].dt.month).count()#.sort_values(by='videoMeta.duration',axis=1)#.plot(kind="bar", legend=False)
pivot_df = pivot_df.rename(columns={"createTime": "count"})
pivot_df = pivot_df.reset_index()

filter_df = df_clean[['createTime','videoMeta.duration','authorMeta.verified','shareCount','likeCount','commentCount','playCount','shareRate','likeRate','commentRate']]
filter_df['videoMeta.duration_segment'] = filter_df['videoMeta.duration'].apply(lambda x: '<= 15' if x <= 15 else '> 15') 
filter_df['date'] = filter_df['createTime'].dt.date
filter_df.drop(['createTime'],axis=1,inplace=True)
filter_df.head()



df_clean[['createTime']].groupby(df_clean["createTime"].dt.month).count().transpose()

filter_df = df_clean[['createTime','videoMeta.duration','authorMeta.verified','shareCount','likeCount','commentCount','playCount','shareRate','likeRate','commentRate']]
filter_df['videoMeta.duration_segment'] = filter_df['videoMeta.duration'].apply(lambda x: '<= 15' if x <= 15 else '> 15') 
filter_df['date'] = filter_df['createTime'].dt.date
filter_df.drop(['createTime'],axis=1,inplace=True)
filter_df.head()

filter_df["durationSeg"] = filter_df["videoMeta.duration"].apply(lambda x: '<= 15' if x <= 15 else '> 15')
filter_df_seg_mean = filter_df.groupby(["durationSeg","authorMeta.verified"])['shareCount','likeCount','commentCount','playCount','shareRate','likeRate','commentRate'].mean().reset_index()
filter_df_seg_count = filter_df.groupby(["durationSeg","authorMeta.verified"]).count().reset_index()
filter_df_seg_count["count"] = filter_df_seg_count["videoMeta.duration"]
filter_df_seg_count = filter_df_seg_count.loc[:,["durationSeg","authorMeta.verified","count"]]
filter_df_seg_count  = pd.merge(filter_df_seg_mean,filter_df_seg_count,on=["durationSeg","authorMeta.verified"])

dfm = filter_df_seg_count


fig = plt.figure(figsize=(10, 6))
ax_1 = fig.add_subplot(3, 1, 1)
ax_2 = fig.add_subplot(3, 1, 2)
ax_3 = fig.add_subplot(3, 1, 3)

def plot_bars(ax, y_col,y_label):
    x = dfm[dfm["authorMeta.verified"]==True]['durationSeg']
    y = dfm[dfm["authorMeta.verified"]==True][y_col]
    ax.bar(x,y,width=np.array(dfm[dfm["authorMeta.verified"]==True]["count"])/1000,alpha=0.8,color='orange')
    x = dfm[dfm["authorMeta.verified"]==False]['durationSeg']
    y = dfm[dfm["authorMeta.verified"]==False][y_col]
    ax.set_ylabel(f'{y_label}', fontdict={'fontsize': 14})
    ax.bar(x,y,width=np.array(dfm[dfm["authorMeta.verified"]==False]["count"])/1000,alpha=0.8,color='lightgrey')


plot_bars(ax_1, 'shareRate',"share rate")
plot_bars(ax_2, 'likeRate',"like rate")
plot_bars(ax_3, 'commentRate',"comment rate")
plt.show()

