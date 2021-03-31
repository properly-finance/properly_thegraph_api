from flask import (
    Blueprint,
    jsonify,
    request,
    # current_app as app
)


api = Blueprint("decentraland_estate_api",
                __name__,
                url_prefix="/decentraland/estate")


@api.route('/ping', methods=('GET',))
def ping():
    return jsonify({'value': 42})


@api.route('/echo', methods=('POST',))
def echo():
    query = request.json.get('query')
    return jsonify({'query': query})
