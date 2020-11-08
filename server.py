from flask import Flask, request

app = Flask(__name__)

@app.route("/tweets")
def handleTweets():
    req_data = request.get_json()

    print(req_data)
    return 'hello!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)