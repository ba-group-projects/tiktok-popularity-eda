import json
import numpy as np
import pandas as pd


class CleanData:
    def __init__(self, data: pd.DataFrame):
        self.dfm = data

    def add_share_rate(self):
        self.dfm["shareRate"] = self.dfm["shareCount"] / self.dfm["playCount"]

    def add_dig_rate(self):
        self.dfm["digRate"] = self.dfm["diggCount"] / self.dfm["playCount"]

    def add_comment_rate(self):
        self.dfm["commentRate"] = self.dfm["commentCount"] / self.dfm["playCount"]

    def unix_to_datetime(self):
        self.dfm['createTime'] = pd.to_datetime(self.dfm['createTime'], unit='s')

    def drop_useless_col(self, colArr):
        self.dfm.drop(colArr, axis=1, inplace=True)

    def rename_col(self, renameDict):
        self.dfm.rename(columns=renameDict, inplace=True)

    def check_missing_data(self):
        columns = self.dfm.columns
        countNull = self.dfm.isnull().sum()
        
        if sum(countNull) == 0:
            print('Missing Data:\n=============\nNone\n')
        else:
            for index in range(len(columns)):
                if countNull[index] > 0:
                    print(f'Missing Data: {columns[index]} column has {countNull[index]} missing values\n')

    def get_time_period(self):
        minDate = min(self.dfm['createTime'])
        maxDate = max(self.dfm['createTime'])
        timeDiff = maxDate - minDate
        print(f'Data Time Period:\n=================\nStart Date: {minDate}\n  End Date: {maxDate}\n Timedelta: {timeDiff}')

    def process_the_data(self):
        self.add_share_rate()
        self.add_dig_rate()
        self.add_comment_rate()
        self.unix_to_datetime()
        self.rename_col({"diggCount": "likeCount"})
        self.drop_useless_col(['videoUrl', 'videoUrlNoWaterMark'])

    def summary_of_data(self):
        self.check_missing_data()
        self.get_time_period()

    def save_cleaned_data(self):
        self.dfm.to_csv("data/cleaned_data.csv")


if __name__ == '__main__':
    data = json.load(open('./data/trending.json', encoding="utf8"))
    data = data['collector']
    df = pd.json_normalize(data)
    clean_data = CleanData(df)
    clean_data.process_the_data()
    clean_data.summary_of_data()
    clean_data.save_cleaned_data()