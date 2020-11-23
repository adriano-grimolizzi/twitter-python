from flask import Flask, request
import random
from utils import load_model, get_sentiment

app = Flask(__name__)

model = load_model('model.pkl')

@app.route("/tweets", methods = ['POST'])
def handlePost():
    print('Handling Request...')

    tweets = request.get_json()['tweets']

    logTweets(tweets)

    return {
        'length': str(len(tweets)),
        'sentiment': getSentiment(tweets)
    }


def getSentiment(tweets):
    general_sentiment = get_sentiment(tweets, model)
    return {
        0: 'Mostly Negative',
        1: 'Mostly Positive'
    }[general_sentiment]


def logTweets(tweets):
    for tweet in tweets:
        print("ID: ", tweet['id'])
        print("Text: ", tweet['text'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
