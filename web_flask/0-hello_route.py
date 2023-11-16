#!/usr/bin/python3
""" Script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """print welcome page"""
    return 'Hello HBNB!'


@app.route('/airbnb-onepage/')
def airbnb_onepage():
    """Returns the Airbnb One-Page content."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
