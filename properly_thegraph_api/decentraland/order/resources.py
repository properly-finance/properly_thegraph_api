import requests
from http import HTTPStatus
import numpy as np
from decimal import Decimal
from flask import Blueprint, jsonify, request, current_app as app
from .utils import calc_price

api = Blueprint("decentraland_orders_api",
                __name__,
                url_prefix="/decentraland/orders")


@api.route('/price-mean', methods=('GET',))
@api.route('/price-mean/<int:count>', methods=('GET',))
def amount_mean(count: int = 10):
    if count > 1000:
        return jsonify({'count': count, 'mean': -1, 'error': 'count > 1000'})

    # query = """
    # {
    #   orders (first:%(count)d, orderBy:updatedAt, orderDirection:desc){
    #     price
    #   }
    # }
    # """

    query = """
      query fetchNFTS(
        $count: Int,
      ) {
        nfts (
          first:$count,
          orderBy: searchOrderCreatedAt
          orderDirection: desc
          where: {
            searchOrderStatus: open
            searchIsLand: true
          }
        ){
          activeOrder{
            price
          }
          estate {
            size
          }
        }
      }
    """
    variables = {'count': count}

    url = app.config['THEGRAPH_DECENTRALAND_URL']
    response = requests.post(url, json={'query': query, 'variables': variables})

    if response.status_code != HTTPStatus.OK:
        return jsonify({'count': count, 'mean': -1, 'error': response.text})

    data = response.json()['data']['nfts']
    np_arr = np.array([
        calc_price(int(rec['activeOrder']['price']), rec['estate'])
        for rec in data])
    np_mean = np.mean(np_arr)

    return jsonify({'count': count, 'mean': int(np_mean)})
