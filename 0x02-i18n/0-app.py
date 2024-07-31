#!/usr/bin/env python3
"""Basic Flask App"""

from flask import Flask, render_template
from flask_babel import Babel, gettext as _

app = Flask(__name__)


@app.route('/')
def index():
    """Index function"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
