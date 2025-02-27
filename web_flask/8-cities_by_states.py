#!/usr/bin/python3
"""Starts a Flask web application"""


from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display a HTML page
       H1 tag: 'States'
       UL tag: with the list of all State objects present in
               DBStorage sorted by name (A->Z)
       LI tag: description of one State: <state.id>: <B><state.name></B> + UL
               tag:with the list of City objects linked to the State
               sorted by name (A->Z)
       LI tag: description of one City: <city.id>: <B><city.name></B>
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
