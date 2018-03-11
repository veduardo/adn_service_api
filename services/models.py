from app import db

class Product(db.Model):
    """ This class represents the 'products' table """

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Product {}>".format(self.name)

    def __str__(self):
        return "{}".format(self.id)

    @staticmethod
    def get_top_products():
        """ Returns the top ordered products """
        # TODO: implement the logic to return the top products
        return Product.query.all()