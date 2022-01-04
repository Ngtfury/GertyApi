import flask
import helper
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world!'


@app.route('/word')
def random_word():
    word = helper.get_random_word()
    return str(word)


if __name__ == '__main__':
    app.run()