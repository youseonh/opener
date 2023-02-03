from flask import jsonify, request, Blueprint

review = Blueprint('review', __name__)


@review.route("/review", methods=['GET'])
def first_route():
    msg = {
        "page": "review",
        "method": "GET"
    }
    return jsonify(msg)
