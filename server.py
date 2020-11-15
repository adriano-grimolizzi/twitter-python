from flask import Flask, request
import random

app = Flask(__name__)


@app.route("/tweets", methods = ['POST'])
def handlePost():
    print('Handling Request...')

    tweets = request.get_json()['tweets']

    logTweets(tweets)

    return {
        'length': str(len(tweets)),
        'sentiment': getSentiment(random.randint(0, 2))
    }


def getSentiment(index):
    return {
        0: 'Mostly Positive',
        1: 'Neutral',
        2: 'Mostly Negative'
    }[index]


def logTweets(tweets):
    for tweet in tweets:
        print("ID: ", tweet['id'])
        print("Text: ", tweet['text'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
