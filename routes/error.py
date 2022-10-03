from flask import Blueprint, render_template

error_app = Blueprint("error_app", __name__)

@error_app.route("/error", methods = ["GET"])
def error():
    return render_template("pages/error/error.html")