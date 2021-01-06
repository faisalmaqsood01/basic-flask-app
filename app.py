from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get('user', None)
    if name:
        return "Hello {}".format(name)
    else:
        return "Hello World"


if __name__ == '__main__':
    app.run()
