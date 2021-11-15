# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dfm = pd.read_csv('data/cleaned_data.csv')

#%%
dfm["verified"]=dfm["authorMeta"].apply(lambda x: True if eval(x)["verified"]==True else False)
# set y axis expenential
plt.yscale('log')
dfm_verified = dfm[dfm["verified"]==True]
dfm_unverified = dfm[dfm["verified"]==False]
plt.scatter(dfm_verified["createTime"],dfm_verified["playCount"],color="green")
plt.scatter(dfm_unverified["createTime"],dfm_unverified["playCount"],color="red",alpha=0.1)

X = dfm_verified["createTime"]
Y = dfm_verified["diggCount"]
slope, intercept = np.polyfit(X, Y, 1)
plt.plot(X, X*slope + intercept, 'g')

X = dfm_unverified["createTime"]
Y = dfm_unverified["diggCount"]
slope, intercept = np.polyfit(X, Y, 1)
plt.plot(X, X*slope + intercept, 'r')
# draw t
# %%