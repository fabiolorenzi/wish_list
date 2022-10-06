from flask import Blueprint, request, render_template
from app import db
import models.category
import models.product
from datetime import datetime

reviewedProducts_app = Blueprint("reviewedProducts_app", __name__)

@reviewedProducts_app.route("/reviews", methods = ["GET"])
def renderReviews():
    return render_template("pages/reviews/reviews.html")