import nltk
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import pandas as pd


class ContentAnalysis:
    def __init__(self):
        self.dfm = pd.read_csv("../data/cleaned_data.csv")

    def get_keywords(self):
        keywords_list = []
        for i in self.dfm["split_text"]:
            keywords_list.extend(eval(i))
        return self.replace_same_meaning_string("".join(keywords_list))

    @staticmethod
    def replace_same_meaning_string(text: str):
        # replace 'for you'
        for_you_list = ["foryoupage", "fyp", "fy", "fyp for youpage", "voorjou", "foryou"]
        for i in for_you_list:
            text = text.replace(i, "for you")
        return text

    def draw_wordcloud(self):
        text = self.get_keywords()
        wordcloud = WordCloud(width=600, height=400).generate(text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.show()


if __name__ == '__main__':
    analysis = ContentAnalysis()
    analysis.draw_wordcloud()
