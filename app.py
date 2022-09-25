from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("TEMPDB")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(db)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)