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

    def process_the_data(self):
        self.add_share_rate()
        self.add_dig_rate()
        self.add_comment_rate()

    def save_cleaned_data(self):
        self.dfm.to_csv("data/cleaned_data.csv")


if __name__ == '__main__':
    data = json.load(open('../archive/trending.json', encoding="utf8"))
    data = data['collector']
    df = pd.DataFrame(data)
    clean_data = CleanData(df)
    clean_data.process_the_data()
    clean_data.save_cleaned_data()

