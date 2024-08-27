#!/usr/bin/env python3
"""
This module sets up a Flask application with Babel for internationalization.
It includes a `get_locale` function to select the best matching language.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    """
    Config class for setting available languages and default configurations.
    
    Attributes:
        LANGUAGES (list): List of supported languages, currently ["en", "fr"].
        BABEL_DEFAULT_LOCALE (str): Default language/locale for the app, set to "en".
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app, set to "UTC".
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

# Instantiate Babel object and store it in a module-level variable
babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages using request.accept_languages.

    Returns:
        str: The best match language from the supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    Renders the 2-index.html template.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('2-index.html')

if __name__ == "__main__":
    """
    Runs the Flask application on host 0.0.0.0 and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
