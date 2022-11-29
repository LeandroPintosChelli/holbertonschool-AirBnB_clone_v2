#!/usr/bin/python3
"""Starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    store = storage.all(State)
    return render_template("7-states_list.html", store=store)


@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
