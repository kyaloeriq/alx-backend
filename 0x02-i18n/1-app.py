#!/usr/bin/env python3
"""
This module sets up a basic Flask application with a single route.
"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """
    Config class for setting available languages and default configurations.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

# Instantiate Babel object and store it in a module-level variable
babel = Babel(app)

@app.route('/')
def index():
    """
    Renders the index.html template.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    """
    Runs the Flask application on host 0.0.0.0 and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
