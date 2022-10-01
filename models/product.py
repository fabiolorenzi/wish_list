from app import ma, db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    country = db.Column(db.String(50))
    materials = db.Column(db.String(1000))
    image_url = db.Column(db.String(1000))
    taste = db.Column(db.String(1000))
    aroma = db.Column(db.String(1000))
    weight = db.Column(db.String(10))
    quantity = db.Column(db.String(5))
    price = db.Column(db.String(20))

    def __init__(self, name, category, created_at, updated_at, country, materials, image_url, taste, aroma, weight, quantity, price):
        self.name = name
        self.category = category
        self.created_at = created_at
        self.updated_at = updated_at
        self.country = country
        self.materials = materials
        self.image_url = image_url
        self.taste = taste
        self.aroma = aroma
        self.weight = weight
        self.quantity = quantity
        self.price = price

class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "category", "created_at", "updated_at", "country", "materials", "image_url", "taste", "aroma", "weight", "quantity", "price")

product_schema = ProductSchema()
products_schema = ProductSchema(many = True)