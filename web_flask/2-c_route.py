#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask
app = Flask(__name__)


@app.route('/',strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb',strict_slashes=False)
def display_hbnb():
    """ Prints a Message when /hbnb is called """
    return 'HBNB'


@app.route('/c/<text>',strict_slashes=False)
def c_is_fun(text):
    return "C"+text.replace('_','')


"""Run the code if main"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
