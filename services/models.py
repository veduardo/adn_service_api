from datetime import datetime

from app import db


#
# Using a separate table to store the Order x Product relation
#
products = db.Table('products',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)


class Product(db.Model):
    """ This class represents the 'product' table """

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


class Order(db.Model):
    """ This class represents the 'order' table """


    id                  = db.Column(db.Integer, primary_key=True)
    products            = db.relationship('Product',
                            secondary=products,
                            lazy='subquery',
                            backref=db.backref('orders', lazy=True))
    customer_id         = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    purchase_date       = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Order {}>".format(self.id)

    @property
    def serialize(self):
        customer = Customer.query.get(self.customer_id)

        return {
            'order_id'          : self.id,
            'products'          : [product.name for product in self.products],
            'customer_id'       : self.customer_id,
            'customer_name'     : customer.name,
            'customer_surname'  : customer.surname,
            'customer_address'  : customer.address,
            'customer_zipcode'  : customer.zipcode,
            'purchase_date'     : self.purchase_date.strftime("%d.%m.%Y %H:%M")
        }


class Customer(db.Model):
    """ This class represents the 'customer' table """


    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(20))
    surname = db.Column(db.String(40))
    address = db.Column(db.String(80))
    zipcode = db.Column(db.String(10))
    orders  = db.relationship('Order', backref='customer', lazy=True)

    def __init__(self, name, surname, address, zipcode):
        self.name    = name
        self.surname = surname
        self.address = address
        self.zipcode = zipcode

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Customer {}>".format(self.name)