from flask import jsonify, make_response, request

from app import app
from forms import OrderForm
from models import Customer, Product, Order


#
# Routes and Endpoints
#

@app.route("/service/health")
def ping():
    if True:
        return make_response("Ok", 200)
    else:
        return make_response("Oops", 400)

@app.route("/service/products/top")
def top_products():
    products = [str(product) for product in Product.get_top_products()]
    if products:
        return make_response(jsonify(products), 200)
    else:
        err = {"message" : "internal server error"}
        return make_response(jsonify(err), 500)

@app.route('/service/order', methods=['POST'])
def new_order():
    received = request.get_json()
    form = OrderForm(data=received)

    if form.validate():
        customer_id = int(received['customer_id'])
        order = Order(customer_id=customer_id)

        for product_id in received['products']:
            product = Product.query.get(product_id)
            order.products.append(product)
        order.save()

        success = {"message" : "success"}
        return make_response(jsonify(success), 201)

    if form.errors:
        validation_err = []
        for entry in form.errors:
            validation_err.append({"message": "incorrect value: < {0} : {1} >".format(entry, received[entry])})
        return make_response(jsonify(validation_err), 400)

    # Something went really bad
    err = {"message": "internal server error"}
    return make_response(jsonify(err), 500)

@app.route('/service/order/<customer_id>')
def get_orders(customer_id):
    orders = [o.serialize for o in Order.query.filter_by(customer_id=customer_id).all()]
    if orders:
        return make_response(jsonify(orders), 200)
    else:
        err = {"message" : "internal server error"}
        return make_response(jsonify(err), 500)