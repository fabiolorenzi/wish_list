from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__, static_url_path="/static")
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("WISHLIST_DB")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(db)
migrate = Migrate(app, db)

import models.user
import models.category
import models.product
import models.reviewedProduct

from routes.home import home_app
from routes.users import users_app
from routes.dashboard import dashboard_app
from routes.categories import categories_app
from routes.products import products_app
from routes.error import error_app
from routes.reviewedProducts import reviewedProducts_app

app.register_blueprint(home_app)
app.register_blueprint(users_app)
app.register_blueprint(dashboard_app)
app.register_blueprint(categories_app)
app.register_blueprint(products_app)
app.register_blueprint(error_app)
app.register_blueprint(reviewedProducts_app)

if __name__ == "__main__":
    app.run(debug=True)