from flask import jsonify, make_response, request

from app import app
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
    received = request.get_json()            #TODO: All input fields must be validated
    customer_id = int(received['customer_id'])
    order = Order(customer_id=customer_id)

    for product_id in received['products']:
        product = Product.query.get(product_id)
        order.products.append(product)
    order.save()

    success = {"message" : "success"}
    return make_response(jsonify(success), 201)