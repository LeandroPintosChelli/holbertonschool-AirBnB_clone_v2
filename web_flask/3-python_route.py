#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Holberton():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def School():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_again(text):
    rep = text.replace('_', ' ')
    return 'C %s' % rep


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def IsCool(text):
    rep = text.replace('_', ' ')
    return 'Python %s' % rep

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
