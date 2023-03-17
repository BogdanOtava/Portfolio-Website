from flask import Flask, render_template
from config import TEMPLATES_PATH


app = Flask(__name__, template_folder=TEMPLATES_PATH)

@app.route("/")
def index():
    """Renders the homepage of the website."""

    return render_template("index.html")
