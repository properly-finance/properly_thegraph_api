import requests
from http import HTTPStatus
import numpy as np
from decimal import Decimal
from flask import Blueprint, jsonify, request, current_app as app

api = Blueprint("aave_flashloans_api",
                __name__,
                url_prefix="/aave/flashloans")


@api.route('/amount-mean', methods=('GET',))
@api.route('/amount-mean/<int:count>', methods=('GET',))
def amount_mean(count: int = 10):
    if count > 1000:
        return jsonify({
            'count': count,
            'mean': -1,
            'error': 'count > 1000',
        })

    query = """
    {
      flashLoans (first: %(count)d, orderBy: timestamp, orderDirection:desc){
        id
        amount
      }
    }
    """ % dict(count=count)

    url = app.config['THEGRAPH_AAVE_URL']
    response = requests.post(url, json={'query': query})

    if response.status_code != HTTPStatus.OK:
        return jsonify({
            'count': count,
            'mean': -1,
            'error': response.text,
        })

    data = response.json()['data']['flashLoans']
    np_arr = np.array([Decimal(rec['amount']) for rec in data])
    np_mean = np.mean(np_arr)

    return jsonify({
        'count': count,
        'mean': float(np_mean)
    })
