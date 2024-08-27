#!/usr/bin/env python3
"""
This module sets up a basic Flask application with a single route.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders the index.html template.
    """
    return render_template('index.html')


if __name__ == "__main__":
    """
    Runs the Flask application on host 0.0.0.0 and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
