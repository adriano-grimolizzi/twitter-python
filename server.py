from flask import Flask, request
from utils import load_model, get_sentiment

app = Flask(__name__)

model = load_model('model.pkl')

@app.route("/tweets", methods = ['POST'])
def handlePost():
    print('Handling Request...')

    tweets = request.get_json()['tweets']
    mode = request.args.get("mode")
    
    logTweets(tweets)
    if len(tweets) == 0:
        return {'error': "empty request"}
    
    results = get_sentiment(tweets,model,mode)
    
    if mode == "general": # general sentiment
        return {
            'length': str(len(tweets)),
            'overallSentiment': results
        }
    else: # sentiment for each tweet
        return {'length': str(len(tweets)),
                'overallSentiment': results[0],
                'analysedTweets': results[1]}
     
   
def logTweets(tweets):
    for tweet in tweets:
        print("ID: ", tweet['id'])
        print("Text: ", tweet['text'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
