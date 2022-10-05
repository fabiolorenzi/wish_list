from flask import Blueprint, request
from app import db
import models.category
from datetime import datetime

categories_app = Blueprint("categories_app", __name__)

@categories_app.route("/api/categories", methods = ["POST"])
def createCategory():
    name = request.json["name"]
    user_id = request.json["user_id"]
    created_at = datetime.now()

    newCategory = models.category.Categories(name, user_id, created_at)
    db.session.add(newCategory)
    db.session.commit()
    return models.category.category_schema.jsonify(newCategory), 201

@categories_app.route("/api/categories/<id>", methods = ["DELETE"])
def deleteCategory(id):
    targetCategory = models.category.Categories.query.get(id)
    db.session.delete(targetCategory)
    db.session.commit()
    return "Category removed successfully"