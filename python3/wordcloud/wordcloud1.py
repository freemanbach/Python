
#!/bin/env python

"""
author     : freeman
date       : 20210117
desc       : wordcloud test
exec       : python3 wordcloud1.py
link       : https://towardsdatascience.com/simple-wordcloud-in-python-2ae54a9f58e5
img        : https://www.kaggle.com/aashita/masks
"""


import wikipedia
import re
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image


def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud) 
    plt.axis("off")


def main():
    wiki = wikipedia.page('Web scraping')
    text = wiki.content
    text = re.sub(r'==.*?==+', '', text)
    text = text.replace('\n', '')

    # black square
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords = STOPWORDS).generate(text)
    #wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)
    wordcloud.to_file("wordcloud1.png")
    
    # Thumb
    mask = np.array(Image.open('upvote.png'))
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords = STOPWORDS, mask=mask).generate(text)
    wordcloud.to_file("upvote.png")


if __name__ == "__main__":
    main()