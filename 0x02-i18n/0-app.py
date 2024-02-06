from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    """Define home route"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
