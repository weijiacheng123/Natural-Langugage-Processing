from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."
#text = "You are the best!"

blob = TextBlob(text)

# print(blob.sentences)

# print(blob.words)

# print(blob.tags)

# print(blob.noun_phrases)

print(round(blob.sentiment.polarity, 3))
print(round(blob.sentiment.subjectivity, 3))

'''
for sentence in blob.sentences:
    print(sentence)
    print(round(sentence.sentiment.polarity, 3))
'''


blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

# print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)


spanish = blob.translate(to='es')

print(spanish)

chinese = blob.translate(to='zh')
print(chinese)

print(chinese.translate())
