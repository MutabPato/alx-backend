#!/usr/bin/env python3
"""i18n
Parametrize templates

Functions:
    get_locale: Determines the best match for supported languages based on the
                request's accept languages.
    index: Renders the index page.

Usage:
    To run the application, execute the script with a Python interpreter.

Example:
    $ ./0-app.py
"""

from flask import Flask, render_template, request, session
from flask_babel import Babel
from typing import Any


app = Flask(__name__)
app.secret_key = 'i18n'

class Config():
    """
    configure available languages
    """
    LANGUAGES = ["en", "fr"]


app.config['BABEL_DEFAULT_LOCALE'] = "en"
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
app.config.from_object(Config)


# Instantiate Babel
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    determine the best match with our supported languages.
    """
    # URL parameter
    locale = request.args.get('locale')
    if locale:
        session['locale'] = locale
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> Any:
    """
    Index function

    Returns: Rendered HTML template.
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
