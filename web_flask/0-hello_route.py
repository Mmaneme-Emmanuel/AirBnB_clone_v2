#!/usr/bin/python3
"""importing Flask"""
from flask import Flask

"""Create a Flask application instance"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


"""Running flask application"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
