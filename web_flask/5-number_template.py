#!/usr/bin/python3
""" script that starts a Flask web application:"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    if isinstance(n, int):
        return '{} is a number'.format(n)

@app.route('/number_template/<n>', strict_slashes=False)
def display_html(n):
    if isinstance(n, int):
        return '{} HTML'.format(n)


"""Run the app"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
