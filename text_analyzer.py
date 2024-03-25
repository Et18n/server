import string
from collections import Counter


import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

text="HEllo this is not m,a acooussaname,!!! Happy"
lowercase_text = text.lower()
cleaned_text = lowercase_text.translate(str.maketrans("", "", string.punctuation))
tokenized = word_tokenize(cleaned_text, "english")

final_words = []
for word in tokenized:
    if word not in stopwords.words("english"):
        final_words.append(word)

emotion_list = []
with open("emotions.txt", "r") as file:
    for line in file:
        clear_line = line.replace("\n", "").replace(",", "").replace("'", "").strip()
        word, emotion = clear_line.split(":")
        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)


def Analyszer(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    negative = score["neg"]
    positve = score["pos"]
    if negative > positve:
        print("Negative")
    elif positve > negative:
        print("Positive")
    else:
        print("Neutral")


Analyszer(cleaned_text)
emotion_counter = Counter(emotion_list)
print(emotion_counter)
fig, ax1 = plt.subplots()
ax1.bar(emotion_counter.keys(), emotion_counter.values())
fig.autofmt_xdate()

plt.savefig("grph.png")
plt.show()
