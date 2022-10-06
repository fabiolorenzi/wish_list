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