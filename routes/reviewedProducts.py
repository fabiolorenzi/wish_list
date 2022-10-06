from flask import Blueprint, request, render_template
from app import db
import models.category
import models.reviewedProduct
from datetime import datetime

reviewedProducts_app = Blueprint("reviewedProducts_app", __name__)

@reviewedProducts_app.route("/reviews", methods = ["GET"])
def renderReviews():
    user = request.args.get("user", type = int)
    categoriesData = models.category.Categories.query.filter(models.category.Categories.user_id == user).order_by(models.category.Categories.name)
    categories = models.category.categories_schema.dump(categoriesData)
    reviewsData = models.reviewedProduct.ReviewedProducts.query.filter(
        models.reviewedProduct.ReviewedProducts.created_by == user
    ).order_by(models.reviewedProduct.ReviewedProducts.name)
    reviews = models.reviewedProduct.reviewedProducts_schema.dump(reviewsData)
    return render_template("pages/reviews/reviews.html", categories=categories, reviews=reviews)

@reviewedProducts_app.route("/api/reviews", methods = ["POST"])
def createReview():
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
    price = request.json["price"]
    note = request.json["note"]
    vote = request.json["vote"]
    created_by = request.json["created_by"]

    newReview = models.reviewedProduct.ReviewedProducts(name, category, created_at, updated_at, country, materials, image_url, taste, aroma, weight, price, note, vote, created_by)
    db.session.add(newReview)
    db.session.commit()
    return models.reviewedProduct.reviewedProduct_schema.jsonify(newReview)

@reviewedProducts_app.route("/api/reviews/<id>", methods = ["PUT"])
def updateReview(id):
    name = request.json["name"]
    category = request.json["category"]
    updated_at = datetime.now()
    country = request.json["country"]
    materials = request.json["materials"]
    image_url = request.json["image_url"]
    taste = request.json["taste"]
    aroma = request.json["aroma"]
    weight = request.json["weight"]
    price = request.json["price"]
    note = request.json["note"]
    vote = request.json["vote"]

    reviewTarget = models.reviewedProduct.ReviewedProducts.query.get(id)

    reviewTarget.name = name or reviewTarget.name
    reviewTarget.category = category or reviewTarget.category
    reviewTarget.update_at = updated_at
    reviewTarget.country = country or reviewTarget.country
    reviewTarget.materials = materials or reviewTarget.materials
    reviewTarget.image_url = image_url or reviewTarget.image_url
    reviewTarget.taste = taste or reviewTarget.taste
    reviewTarget.aroma = aroma or reviewTarget.aroma
    reviewTarget.weight = weight or reviewTarget.weight
    reviewTarget.price = price or reviewTarget.price
    reviewTarget.note = note or reviewTarget.note
    reviewTarget.vote = vote or reviewTarget.vote

    db.session.commit()
    return models.reviewedProduct.reviewedProduct_schema.jsonify(reviewTarget)

@reviewedProducts_app.route("/api/reviews/<id>", methods = ["DELETE"])
def deleteReview(id):
    targetReview = models.reviewedProduct.ReviewedProducts.query.get(id)
    db.session.delete(targetReview)
    db.session.commit()
    return "Review deleted successfully"