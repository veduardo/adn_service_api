from flask import jsonify, make_response

from app import app


#
# Routes and Endpoints
#
@app.route("/service/health")
def ping():
    if True:
        return make_response("Ok", 200)
    else:
        return make_response("Oops", 400)