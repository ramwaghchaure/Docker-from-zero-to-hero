from flask import flask
import redius

app = Flask(_name_)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello();
     count = r.incr('hits')
     return f'Welcome! This page was viewed {count} times.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
