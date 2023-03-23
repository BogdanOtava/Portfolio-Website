# Sets up the routes for all the pages

from flask import Flask, render_template
from config import TEMPLATES_PATH, TEXT_PATH
from application.helpers import *


app = Flask(__name__, template_folder=TEMPLATES_PATH)
app.jinja_env.filters["is_active"] = is_active


@app.route("/")
def index():
    """Renders the 'Home' page of the website."""

    return render_template("index.html")


@app.route("/about")
def about():
    """Renders the 'About Me' page of the website."""

    content = read_file(f"{TEXT_PATH}/about.txt")

    return render_template("about.html", content=content)


@app.route("/skills")
def skills():
    """Renders the 'Skills' page of the website."""

    skills = get_skills(f"{TEXT_PATH}/skills.json")

    return render_template("skills.html", skills=skills)
