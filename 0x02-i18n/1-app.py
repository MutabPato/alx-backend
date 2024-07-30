#!/usr/bin/env python3
"""i18n"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """configure available languages"""
    LANGUAGES = ["en", "fr"]


app.config['BABEL_DEFAULT_LOCALE'] = "en"
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
app.config.from_object(Config)


@app.route('/')
def index():
    """Index function"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
