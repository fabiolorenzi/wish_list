from app import db, ma

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    surname = db.Column(db.String(20))
    email = db.Column(db.String(100))
    password = db.Column(db.String(20))
    created_at = db.Column(db.DateTime())
    edited_at = db.Column(db.DateTime())

    def __init__(self, name, surname, email, password, created_at, edited_at):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.created_at = created_at
        self.edited_at = edited_at

class UserSchema(ma.Schema):
    class Meta():
        fields = ("id", "name", "surname", "email", "password", "created_at", "edited_at")

user_schema = UserSchema()
users_schema = UserSchema(many = True)