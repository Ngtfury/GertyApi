import flask
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world!'


if __name__ == '__main__':
    app.run()