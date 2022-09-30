from flask import Blueprint, render_template

dashboard_app = Blueprint("dashboard_app", __name__)

@dashboard_app.route("/dashboard", methods = ["GET"])
def test():
    return render_template("pages/dashboard/dashboard.html")