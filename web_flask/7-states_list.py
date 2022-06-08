#!/usr/bin/python3
"""Starts a Flask web application"""


from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a HTML page
       H1 tag: 'States'
       UL tag: with the list of all State objects present in
               DBStorage sorted by name (A->Z)
       LI tag: description of one State: <state.id>: <B><state.name></B>
    """
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
