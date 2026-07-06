from app.extensions import db


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(150),
        nullable=False
    )

    sku = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        default=0
    )

    unit_price = db.Column(
        db.Float,
        default=0
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id")
    )

    supplier_id = db.Column(
        db.Integer,
        db.ForeignKey("suppliers.id")
    )

    category = db.relationship("Category")

    supplier = db.relationship("Supplier")

    def __repr__(self):
        return self.name
