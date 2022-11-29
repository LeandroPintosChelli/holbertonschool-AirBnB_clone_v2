#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    from models import storage
    from models.state import State
    sts = storage.all(State)
    return render_template("7-states_list.html", sts=sts)


@app.teardown_appcontext
def teardown(self):
    from models import storage
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
