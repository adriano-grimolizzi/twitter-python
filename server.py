from flask import Flask, request

app = Flask(__name__)


@app.route("/tweets")
def get():
    tweets = request.get_json()['tweets']

    handleTweets(tweets)

    return {'length': str(len(tweets))}


def handleTweets(tweets):
    for tweet in tweets:
        print("ID: ", tweet['id'])
        print("Text: ", tweet['text'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
