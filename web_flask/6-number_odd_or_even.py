#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Display 'C ' followed by the value of the text variable"""
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """Display 'Python ' followed by the value of the text variable"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    """Display '{n} is a number' only if n is an integer"""
    if isinstance(n, int):
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Display an HTML page with 'Number: n' if n is an integer"""
    if isinstance(n, int):
        return render_template('6-number_template.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    """Display an HTML page with 'Number: n is even|odd' if n is an integer"""
    if isinstance(n, int):
        odd_or_even = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html',
                               n=n, odd_or_even=odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
