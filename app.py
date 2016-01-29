from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='10.0.0.21', port='6379')


@app.route('/')
def hello():
    redis.incr('hits')
    hits = redis.get('hits')
    return 'Hello World! This page has been viewed %s times.' % hits

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
