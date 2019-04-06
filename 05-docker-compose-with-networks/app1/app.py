from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis-1', port=6379)
server_name="server-1"

@app.route('/')
def hello_world():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times. (server : {})\n'.format(count, server_name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 