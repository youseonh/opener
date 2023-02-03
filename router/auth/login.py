from flask import jsonify, request, Blueprint

login = Blueprint('auth', __name__)


@login.route("/auth", methods=['GET'])
def first_route():
    msg = {
        "page": "auth",
        "method": "GET"
    }
    return jsonify(msg)
