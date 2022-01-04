import flask
import helper
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello world!'
#    return flask.redirect('https://gerty-api.herokuapp.com/home')


#@app.route('/home')
#def home():
#    return 'Hello world!'

@app.route('/word')
def random_word():
    _number = request.args.get('number')
    print(_number)
    return 'ok!'

    if _number:
        try:
            _int_number = int(_number)
        except:
            flask.abort(405)
    else:
        _int_number = 1

    word = helper.get_random_word(_int_number)
    return word

@app.errorhandler(500)
async def error_500(error):
    return '500'


if __name__ == '__main__':
    app.run()