from flask import jsonify, make_response

from app import app
from models import Product


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
