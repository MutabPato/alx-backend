#!/usr/bin/env python3
""" i18n - Basic Flask App
Functions:
    index: Renders the index page.
Usage:
    To run the application, execute the script with a Python interpreter.

Example:
    $ ./0-app.py
"""

from flask import Flask, render_template
from flask_babel import Babel, gettext as _

app = Flask(__name__)


@app.route('/')
def index():
    """Index function"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
