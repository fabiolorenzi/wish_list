from flask import Blueprint, render_template

home_app = Blueprint("home_app", __name__)

@home_app.route("/", methods = ["GET"])
def test():
    return render_template("pages/home/home.html")