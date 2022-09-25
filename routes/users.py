from flask import Blueprint, jsonify, request, render_template
from app import db
from dotenv import load_dotenv
import os
import models.user

users_app = Blueprint("users_app", __name__)

load_dotenv()

@users_app.route("/login", methods = ["GET"])
def test():
    return render_template("pages/user/index.html")