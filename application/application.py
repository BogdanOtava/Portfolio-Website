# Sets up the routes for all the pages

from flask import Flask, render_template, request
from flask_caching import Cache
from config import TEMPLATES_PATH, TEXT_PATH
from application.helpers import *
from tkn import *


app = Flask(__name__, template_folder=TEMPLATES_PATH)
app.jinja_env.filters["is_active"] = is_active
app.jinja_env.filters["get_language_image"] = get_language_image

cache = Cache(app, config={"CACHE_TYPE": "simple", "CACHE_DEFAULT_TIMEOUT": 3600})


@app.route("/")
def index():
    """Renders the 'Home' page of the website."""

    return render_template("index.html")


@app.route("/about")
def about():
    """Renders the 'About Me' page of the website."""

    content = read_description(f"{TEXT_PATH}/about.txt")

    return render_template("about.html", content=content)


@app.route("/skills")
def skills():
    """Renders the 'Skills' page of the website."""

    skills = get_skills(f"{TEXT_PATH}/skills.json")

    return render_template("skills.html", skills=skills)


@app.route("/portfolio")
@cache.cached()
def portfolio():
    """Renders the 'Portfolio' page of the website."""

    repos = get_repositories()

    return render_template("portfolio.html", repos=repos)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Renders the 'Contact' page of the website."""

    # User reached route via POST
    if request.method == "POST":
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        # Format message
        message = f"FROM: {first_name} {last_name} <{email}>\nSUBJECT: {subject}\n\n{message}"

        # Send email using Mailgun API
        response = requests.post(
            f"https://api.eu.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", MAILGUN_API_KEY),
            data={
                "from": f"{first_name} {last_name} <{email}>",
                "to": RECEIVER_EMAIL,
                "subject": subject,
                "text": message
            }
        )

        # Check for successful API response
        if response.status_code == 200:
            return render_template("result.html", status_code=response.status_code, message="Your email has been sent! I'll contact you as soon as possible.")
        else:
            return render_template("result.html", status_code=response.status_code, message="Your email could not be sent! Please try again.")

    # User reached route via GET
    return render_template("contact.html")
