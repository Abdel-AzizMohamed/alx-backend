#!/usr/bin/env python3
"""Define a basic flask project"""
from flask import Flask, render_template, request
from flask_babel import Babel

# pylint: disable=E1101


class Config:
    """Contains babel config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get the local from a webpage"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
@app.route("/home")
def home() -> str:
    """Define home route"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
