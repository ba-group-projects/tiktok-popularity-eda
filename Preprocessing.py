# %% import packages
# import packages
import plotly.express as px
import pandas as pd
from collections import Counter
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as pyplot
import seaborn as sns
import numpy as np
import json

# %% preprocessing the data
# 1. read the data
dfm = pd.read_csv('BasicCompanyDataAsOneFile-2021-12-01.csv')

# %% clean the data
# 2. change str to datetime 
dfm['IncorporationDate'] = pd.to_datetime(dfm['IncorporationDate'], errors = 'coerce')

# 3. drop the rows with missing SICCode_1
## 3.1 drop the rows with missing SICCode_1
dfm = dfm.dropna(subset = ['SICCode.SicText_1'])
## 3.2 drop the rows with SICCode_1 ==9999
dfm = dfm[dfm["SICCode.SicText_1"] != "99999 - Dormant Company"]
## 3.3 drop the rows with SICCode_1 == None Supplied
dfm = dfm[dfm["SICCode.SicText_1"] != "None Supplied"]

# 4. get first 2 number of SIC codes
dfm.loc[:, "SICCode_1_twodigtal"] = dfm["SICCode.SicText_1"].str[0:2]
dfm.loc[:, "SICCode_2_twodigtal"] = dfm["SICCode.SicText_2"].str[0:2]
dfm.loc[:, "SICCode_3_twodigtal"] = dfm["SICCode.SicText_3"].str[0:2]
dfm.loc[:, "SICCode_4_twodigtal"] = dfm["SICCode.SicText_4"].str[0:2]

# 5. get the number of SIC codes
dfm["SICCounts"] = dfm[["SICCode.SicText_1", "SICCode.SicText_2",
                         "SICCode.SicText_3", "SICCode.SicText_4"]].notnull().sum(axis=1)

# 6. generate the a column of the Year and Month
dfm["IncorporationMonth"]  = dfm["IncorporationDate"].apply(lambda x:str(x.year))+"-" +dfm["IncorporationDate"].apply(lambda x:str(x.month))

# %%
# 7. sort IncorporationDate
dfm.sort_values(by = "IncorporationDate",inplace = True)

# %% merge the data
with open("Location.json") as f:
    location = json.load(f)
location = pd.DataFrame(location)
dfm_new = pd.merge(left=dfm, right=location, on="CompanyName")
# %%
dfm_new.to_csv("final_csv.csv")
# %%
