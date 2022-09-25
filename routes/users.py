from flask import Blueprint, jsonify, request, template_rendered
from app import db
from dotenv import load_dotenv
import os
import models.user

users_app = Blueprint("users_app", __name__)

load_dotenv()

@users_app.route("/", methods = ["GET"])
def test():
    return template_rendered("index.html")