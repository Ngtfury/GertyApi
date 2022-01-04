import flask
from flask import json
import helper
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
#    return flask.redirect('https://gerty-api.herokuapp.com/home')


#@app.route('/home')
#def home():
#    return 'Hello world!'

@app.route('/word')
def random_word():
    _number = request.args.get('number')

    if not _number == None:
        try:
            _int_number = int(_number)
        except:
            flask.abort(405)
    else:
        _int_number = 1

    word = helper.get_random_word(_int_number)
    JSON = jsonify(
        words = word,
        code = 200
    )
    return JSON

@app.errorhandler(500)
def error_500(error):
    _json = jsonify(
        message = 'There was an error while you tried to visit our page, our devs are working on it. Please be patient.',
        code = 500
    )
    print(error)
    return _json, 500

@app.errorhandler(404)
async def page_not_found(error):
    _json = jsonify(
        message = 'The requested URL was not found in our server.',
        code = 404
    )
    return _json, 404


if __name__ == '__main__':
    app.run()