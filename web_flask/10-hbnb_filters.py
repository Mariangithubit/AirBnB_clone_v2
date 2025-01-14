#!/usr/bin/python3
"""
Starts a Flask web application.
Routes:
    * /hbnb_filters: HBnB HTML filters page.
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def hbnb_filters():
    """Displays the HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(except=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
