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