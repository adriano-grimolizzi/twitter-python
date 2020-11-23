from flask import Flask, request
import random
from utils import load_model, get_sentiment, predict_tweet

app = Flask(__name__)

model = load_model('model.pkl')

@app.route("/tweets", methods = ['POST'])
def handlePost(mode = "general"):
    print('Handling Request...')

    tweets = request.get_json()['tweets']

    logTweets(tweets)
    if mode == "general": # general sentiment
        return {
            'length': str(len(tweets)),
            'overallSentiment': getSentiment(tweets)
        }
    else: # sentiment for each tweet
        return {'length': str(len(tweets)),
                'overallSentiment': getSentiment(tweets),
                'analysedTweets': [{str(i): get_single_sentiment(tweets[i])} for i in range(len(tweets))]}
        


def getSentiment(tweets):
    general_sentiment = get_sentiment(tweets, model)
    return {
        0: 'Mostly Negative',
        1: 'Mostly Positive'
    }[general_sentiment]


def get_single_sentiment(tweet):
    sentiment = predict_tweet(tweet, model[1], model[0]) > 0.5
    return {
        0: 'Negative',
        1: 'Positive'
    }[sentiment[0,0]]
    
def logTweets(tweets):
    for tweet in tweets:
        print("ID: ", tweet['id'])
        print("Text: ", tweet['text'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
