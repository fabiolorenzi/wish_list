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
def createProduct():
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

@products_app.route("/api/products/<id>", methods = ["PUT"])
def updateProduct(id):
    name = request.json["name"]
    category = request.json["category"]
    updated_at = datetime.now()
    country = request.json["country"]
    materials = request.json["materials"]
    image_url = request.json["image_url"]
    taste = request.json["taste"]
    aroma = request.json["aroma"]
    weight = request.json["weight"]
    quantity = request.json["quantity"]
    price = request.json["price"]

    productTarget = models.product.Products.query.get(id)

    productTarget.name = name or productTarget.name
    productTarget.category = category or productTarget.category
    productTarget.updated_at = updated_at
    productTarget.country = country or productTarget.country
    productTarget.materials = materials or productTarget.materials
    productTarget.image_url = image_url or productTarget.image_url
    productTarget.taste = taste or productTarget.taste
    productTarget.aroma = aroma or productTarget.aroma
    productTarget.weight = weight or productTarget.weight
    productTarget.quantity = quantity or productTarget.quantity
    productTarget.price = price or productTarget.price

    db.session.commit()
    return models.product.product_schema.jsonify(productTarget)