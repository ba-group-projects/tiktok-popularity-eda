import json
import nltk
import numpy as np
import pandas as pd


class CleanData:
    def __init__(self, data: pd.DataFrame):
        self.dfm = data

    def add_share_rate(self):
        self.dfm["shareRate"] = self.dfm["shareCount"] / self.dfm["playCount"]

    def add_dig_rate(self):
        self.dfm["likeRate"] = self.dfm["diggCount"] / self.dfm["playCount"]

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

    def add_split_text(self):
        self.dfm["split_text"] = df["text"].apply(lambda x: x[x.find("#")+1:].split("#"))

    # def add_split_text_without_stop_words(self):
    #     stop_words = nltk.corpus.stopwords.words("english")
    #     df["text_list_drop_stop_words"] = df["split_text"].apply(
    #         lambda x: [word for word in x if word not in stop_words])

    def get_time_period(self):
        minDate = min(self.dfm['createTime'])
        maxDate = max(self.dfm['createTime'])
        timeDiff = maxDate - minDate
        print(
            f'Data Time Period:\n=================\nStart Date: {minDate}\n  End Date: {maxDate}\n Timedelta: {timeDiff}')

    def process_the_data(self):
        self.add_share_rate()
        self.add_dig_rate()
        self.add_comment_rate()
        self.unix_to_datetime()
        self.rename_col({"diggCount": "likeCount"})
        self.add_split_text()
        # self.add_split_text_without_stop_words()
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
