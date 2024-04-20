#!/usr/bin/python3
"""Starts a Flash Web Application HBNB"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Prints a Message when / is called"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


"""Run the code if main"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
