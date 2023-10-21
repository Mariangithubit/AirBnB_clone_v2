#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """print welcome page"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """print another word"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """print C followed by the value of the text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """Display “Python ”, followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def integer(n):
    """display number if is an integer"""
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
