from flask import Flask, request, jsonify
from flask_cors import CORS


import string
from collections import Counter

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


app = Flask(__name__)


CORS(app, origins=["http://localhost:3000","https://miniprojectsem4-3ljc.vercel.app"])


@app.route("/process", methods=["POST", "GET"])





def analyze():
    print(request)
    #body = request.get_json(force=True)
    if request.method == "POST":
        text = request.get_json()
        result = alive(text["text_analyze"])
        print(text)
        return jsonify(result), 200
    elif request.method == "GET":
        return "got ", 200
    else:
        return "SERVER DIES", 400


def alive(text):
    if text:

        # data = request.get_data(as_text=True)
        # data = request.get_data(as_text=True)
        # if not data:
        #     return jsonify({"error": "Empty request body"}), 400
        # try:
        #     json_data = json.loads(data)
        # except json.JSONDecodeError:
        #     return jsonify({"error": "Invalid JSON"}), 400
        # text = json_data.get('text', '')
        lower_case = text.lower()
        cleaned_text = lower_case.translate(str.maketrans("", "", string.punctuation))
        tokenized_words = word_tokenize(cleaned_text, "english")
        # Removing Stop Words
        final_words = []
        for word in tokenized_words:
            if word not in stopwords.words("english"):
                final_words.append(word)
        lemma_words = []
        for word in final_words:
            word = WordNetLemmatizer().lemmatize(word)
            lemma_words.append(word)
        emotion_list = []
        with open(
            "./emotions.txt",
            "r",
        ) as file:
            for line in file:
                clear_line = (
                    line.replace("\n", "").replace(",", "").replace("'", "").strip()
                )
                word, emotion = clear_line.split(":")
                if word in lemma_words:
                    emotion_list.append(emotion)
        print(emotion_list)
        w = Counter(emotion_list)
        print(w)

        fig, ax1 = plt.subplots()
        ax1.bar(w.keys(), w.values())
        fig.autofmt_xdate()
        # plt.savefig('graph.png')
        

        def sentiment_analyse(sentiment_text):
            score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
            if score["neg"] > score["pos"]:
                return "Negative"
            elif score["neg"] < score["pos"]:
                return  "Positve"
            else:
                return "Neutral"

        weewoo=sentiment_analyse(cleaned_text)
        plt.show()
        return weewoo


if __name__ == "__main__":
    app.run(debug=True, port=80)
