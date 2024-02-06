#!/usr/bin/env python3
"""Define a basic flask project"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Contains babel config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route("/")
@app.route("/home")
def home() -> str:
    """Define home route"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)