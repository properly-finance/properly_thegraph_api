import requests
from http import HTTPStatus
import numpy as np
from decimal import Decimal
from flask import Blueprint, jsonify, request, current_app as app

api = Blueprint("decentraland_orders_api",
                __name__,
                url_prefix="/decentraland/orders")


@api.route('/price-mean', methods=('GET',))
@api.route('/price-mean/<int:count>', methods=('GET',))
def amount_mean(count: int = 10):
    if count > 1000:
        return jsonify({'count': count, 'mean': -1, 'error': 'count > 1000'})

    query = """
    {
      orders (first:%(count)d, orderBy:updatedAt, orderDirection:desc){
        price
      }
    }
    """ % dict(count=count)

    url = app.config['THEGRAPH_DECENTRALAND_URL']
    response = requests.post(url, json={'query': query})

    if response.status_code != HTTPStatus.OK:
        return jsonify({'count': count, 'mean': -1, 'error': response.text})

    data = response.json()['data']['orders']
    np_arr = np.array([int(rec['price']) for rec in data])
    np_mean = np.mean(np_arr)

    return jsonify({'count': count, 'mean': f'{int(np_mean)}'})
