from flask import Blueprint, jsonify, request, render_template
from app import db
import models.category
from datetime import datetime

products_app = Blueprint("products_app", __name__)

@products_app.route("/wish-list", methods = ["GET"])
def renderPage():
    return render_template("pages/wish-list/wish-list.html")