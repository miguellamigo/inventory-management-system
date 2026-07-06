from flask import render_template
from app.routes.main import main


@main.route("/")
def home():
    return render_template("dashboard/index.html")
