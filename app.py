import flask
import helper
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def home():
    return flask.redirect('https://gerty-api.herokuapp.com/home')

@app.route('/home')
def home():
    return 'Hello world!'

@app.route('/word')
def random_word():
    _number = request.args.get('number')

    if _number:
        try:
            _int_number = int(_number)
        except:
            flask.abort(405)
    else:
        _int_number = 1

    word = helper.get_random_word(_int_number)
    return word



if __name__ == '__main__':
    app.run()