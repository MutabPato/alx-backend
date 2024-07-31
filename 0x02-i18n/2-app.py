#!/usr/bin/env python3
"""Get locale from request"""

from flask import Flask, render_template
from flask_babel import Babel
from typing import Any


app = Flask(__name__)


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
def get_locale():
    """
    determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> Any:
    """
    Index function

    Returns: Rendered HTML template.
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
