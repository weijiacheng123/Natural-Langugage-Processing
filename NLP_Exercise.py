import nltk
import matplotlib.pyplot as plt
from pathlib import Path
from nltk.corpus import stopwords
from textblob import TextBlob
import imageio
from wordcloud import WordCloud
import wordcloud
from operator import itemgetter
import operator
import pandas as pd
import spacy

blob = TextBlob(Path("book of John text.txt").read_text())
stops = stopwords.words("english")
#print(stops)

without_stopwords =[]
more_stops= ['thy', 'ye', 'verily', 'thee', 'hath', 'say', 'thou', 'art', 'shall']
stops += more_stops

cleanlist = [word for word in blob.words if word not in stops]
#print(cleanlist)

items = blob.word_counts.items()
clean_items = [i for i in items if i[0] not in stops]
#print(clean_items[:10])

sorted_list = sorted(clean_items, key=itemgetter(1), reverse=True)
#print(sorted_list[:10])

top15 = sorted_list[:16]
df = pd.DataFrame(top15, columns=["word", "count"])
print(df)
#print(top15)

text_list = []
for i in top15:
    x = i[0]
    text_list.append(x)

text = ' '.join(text_list)
mask_image = imageio.imread("mask_rectangle.png")



wordcloud = WordCloud(colormap='ocean', mask=mask_image,
                      background_color='gray')

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("NLP_exercise.png")

print("done")