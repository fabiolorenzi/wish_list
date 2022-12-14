from flask import Blueprint, jsonify, request, render_template
from app import db
from tools.security import crypt, decrypt
from dotenv import load_dotenv
import models.user
from datetime import datetime

users_app = Blueprint("users_app", __name__)

load_dotenv()

@users_app.route("/login", methods = ["GET"])
def loginPage():
    return render_template("pages/user/user.html")

@users_app.route("/account", methods = ["GET"])
def accountPage():
    id = request.args.get("user", type = int)
    targetUserData = models.user.Users.query.filter(models.user.Users.id == id)
    user = models.user.users_schema.dump(targetUserData)
    return render_template("pages/account/account.html", user=user)

@users_app.route("/api/user", methods = ["POST"])
def createUser():
    name = request.json["name"]
    surname = request.json["surname"]
    email = crypt(request.json["email"])
    password = crypt(request.json["password"])
    created_at = datetime.now()
    edited_at = datetime.now()

    newUser = models.user.Users(name, surname, email, password, created_at, edited_at)
    db.session.add(newUser)
    db.session.commit()
    return models.user.user_schema.jsonify(newUser), 201

@users_app.route("/api/user/<id>", methods = ["DELETE"])
def deleteUser(id):
    targetUser = models.user.Users.query.get(id)
    
    db.session.delete(targetUser)
    db.session.commit()
    return "User deleted successfully"

@users_app.route("/api/login", methods = ["POST"])
def login():
    allUsers = models.user.Users.query.all()
    result = models.user.users_schema.dump(allUsers)

    email = request.json["email"]
    password = request.json["password"]

    for x in result:
        emailCheck = decrypt(x["email"].encode())
        passwordCheck = decrypt(x["password"].encode())
        if email == emailCheck and password == passwordCheck:
            userData = models.user.Users.query.get(x["id"])
            return models.user.user_schema.jsonify(userData)
    return {"email": "unavailable", "password": "unavailable"}, 404

@users_app.route("/api/user/<id>", methods = ["GET"])
def checkPermission(id):
    targetUser = models.user.Users.query.get(id)
    return models.user.user_schema.jsonify(targetUser)