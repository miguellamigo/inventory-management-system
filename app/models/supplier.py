from app.extensions import db


class Supplier(db.Model):

    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key=True)

    company_name = db.Column(
        db.String(150),
        nullable=False
    )

    contact_person = db.Column(db.String(100))

    phone = db.Column(db.String(30))

    email = db.Column(db.String(120))

    address = db.Column(db.Text)

    def __repr__(self):
        return self.company_name
