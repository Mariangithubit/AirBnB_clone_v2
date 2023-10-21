#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list')
def states_list():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
