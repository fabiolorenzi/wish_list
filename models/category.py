from app import db, ma

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer)
    created_by = db.Column(db.DateTime)

    def __init__(self, name, user_id, created_by):
        self.name = name
        self.user_id = user_id
        self.created_by = created_by

class CategorySchema(ma.Schema):
    class Meta():
        fields = ("id", "name", "user_id", "created_by")

category_schema = CategorySchema()
categories_schema = CategorySchema(many = True)