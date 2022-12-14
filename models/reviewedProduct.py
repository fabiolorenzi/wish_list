from app import ma, db

class ReviewedProducts(db.Model):
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
    price = db.Column(db.String(20))
    note = db.Column(db.String(10000))
    vote = db.Column(db.Integer)
    created_by = db.Column(db.Integer)

    def __init__(self, name, category, created_at, updated_at, country, materials, image_url, taste, aroma, weight, price, note, vote, created_by):
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
        self.price = price
        self.note = note
        self.vote = vote
        self.created_by = created_by

class ReviewedProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "category", "created_at", "updated_at", "country", "materials", "image_url", "taste", "aroma", "weight", "price", "note", "vote", "created_by")

reviewedProduct_schema = ReviewedProductSchema()
reviewedProducts_schema = ReviewedProductSchema(many = True)