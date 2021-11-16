# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
dfm = pd.read_csv('data/cleaned_data.csv')



# %%
def convert_timestamp_to_string(timestamp):
    return pd.to_datetime(timestamp, unit='s').apply(lambda x: datetime.datetime.strftime(x,'%Y-%m-%d'))
#%%



plt.style.use('ggplot')
plt.grid(False)
dfm["verified"]=dfm["authorMeta"].apply(lambda x: True if eval(x)["verified"]==True else False)
# set y axis expenential

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set_yscale('log')
ax.set_facecolor((1, 1, 1))

dfm_verified = dfm[dfm["verified"]==True]
dfm_unverified = dfm[dfm["verified"]==False]
ax.scatter(pd.to_datetime(dfm_verified["createTime"],unit="s"),dfm_verified["playCount"],color="#99dfe1",label="verified")
ax.scatter(pd.to_datetime(dfm_unverified["createTime"],unit="s"),dfm_unverified["playCount"],color="#e3bfff",alpha=0.2,label="unverified")

X = dfm_verified["createTime"]
Y = dfm_verified["diggCount"]
slope, intercept = np.polyfit(X, Y, 1)
x = [pd.to_datetime(dfm_unverified["createTime"],unit="s").min(),pd.to_datetime(dfm_unverified["createTime"],unit="s").max()]
y_temp = X*slope + intercept
y = [y_temp.min(),y_temp.max()]
verified_y_max = y[-1]
ax.plot(x,y,'#99dfe1',linewidth=2,alpha=1)

X = dfm_unverified["createTime"]
Y = dfm_unverified["diggCount"]
slope, intercept = np.polyfit(X, Y, 1)
x = [pd.to_datetime(dfm_unverified["createTime"],unit="s").min(),pd.to_datetime(dfm_unverified["createTime"],unit="s").max()]
y_temp = X*slope + intercept
y = [y_temp.min(),y_temp.max()]
ax.plot(x,y, '#e3bfff',linewidth=2,alpha=1)

ax.set_xlim(pd.to_datetime(dfm_unverified["createTime"],unit="s").min(),pd.to_datetime(dfm_unverified["createTime"],unit="s").max()+datetime.timedelta(days=10))
ax.set_ylim(100,100000000)

# add horizontal line
# ax.axhline(min(y),xmax = x[-1], color='#e3bfff', linestyle='--',linewidth=2)
ax.plot(x,[y_temp.min(),y_temp.min()], color='#e3bfff', linestyle='--',linewidth=2)

# add legend
legend = ax.legend(loc='lower right',fontsize=12,facecolor = '#f7f7f7')


# add title
ax.set_title('Dig count change over time\n ',fontsize=16)

# add annotation
# draw vertical arrow(increase)
ax.annotate("", xy=(x[-1],y[-1]),  xycoords='data', xytext=(x[-1],y[0]),
                arrowprops=dict(arrowstyle='<->', color="grey", lw=1)
                )
ax.text(x=x[-1]+datetime.timedelta(days=2),y= 35000,fontsize=10,s="{:,}".format(int(max(y)-min(y))))

# draw vertical arrow(end differnce)
ax.annotate("", xy=(x[-1],y[-1]),  xycoords='data', xytext=(x[-1],verified_y_max),
                arrowprops=dict(arrowstyle='<->', color="grey", lw=1))
ax.text(x=x[-1]+datetime.timedelta(days=2),y=200000,fontsize=10,s="{:,}".format(int(verified_y_max-max(y))))
# draw vertical arrow(start differnce)
ax.annotate("", xy=(x[0]+datetime.timedelta(days=1),y[0]),  xycoords='data', xytext=(x[0]+datetime.timedelta(days=1),verified_y_max),
                arrowprops=dict(arrowstyle='<->', color="grey", lw=1))
ax.text(x=x[0]+datetime.timedelta(days=2),y=140000,fontsize=10,s="{:,}".format(int(verified_y_max-min(y))))

# draw horizontal arrow
ax.annotate("", xy=(x[0],10000),  xycoords='data', xytext=(x[-1],10000),
                arrowprops=dict(arrowstyle='<->', color="grey", lw=1)
                )
ax.text(datetime.datetime(2020,11,1),y= 5000,fontsize=10,s="3 months")
plt.show()

# %%

# %%

# %%
