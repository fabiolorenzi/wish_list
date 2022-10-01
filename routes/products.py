from flask import Blueprint, jsonify, request, render_template
from app import db
import models.category
import models.product
from datetime import datetime

products_app = Blueprint("products_app", __name__)

@products_app.route("/wish-list", methods = ["GET"])
def renderPage():
    return render_template("pages/wish-list/wish-list.html")

@products_app.route("/api/products", methods = ["POST"])
def createPage():
    name = request.json["name"]
    category = request.json["category"]
    created_at = datetime.now()
    updated_at = datetime.now()
    country = request.json["country"]
    materials = request.json["materials"]
    image_url = request.json["image_url"]
    taste = request.json["taste"]
    aroma = request.json["aroma"]
    weight = request.json["weight"]
    quantity = request.json["quantity"]
    price = request.json["price"]

    newProduct = models.product.Products(name, category, created_at, updated_at, country, materials, image_url, taste, aroma, weight, quantity, price)
    db.session.add(newProduct)
    db.session.commit()
    return models.product.product_schema.jsonify(newProduct)