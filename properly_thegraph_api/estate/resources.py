from flask import Blueprint, jsonify


api = Blueprint("api_estate", __name__, url_prefix="/estate")


@api.route('/test')
def test():
    return jsonify({'text': 'hi'})
