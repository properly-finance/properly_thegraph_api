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

    # query = """
    #   query fetchNFTS(
    #     $count: Int,
    #   ) {
    #     nfts (
    #       first:$count,
    #       orderBy: searchOrderCreatedAt
    #       orderDirection: desc
    #       where: {
    #         searchOrderStatus: open
    #         searchIsLand: true
    #       }
    #     ){
    #       activeOrder{
    #         price
    #       }
    #       estate {
    #         size
    #       }
    #     }
    #   }
    # """

    query_parcel = """
query fetchParcelOrders($count: Int) {
  orders(
    first: $count
    orderBy: createdAt
    orderDirection: desc
    where: {
      status: sold
      category: parcel
    }
  ) {
    price
  }
}
    """
    query_estate = """
query fetchEstateOrders($count: Int) {
  orders(
    first: $count
    orderBy: createdAt
    orderDirection: desc
    where: {
      status: sold
      category: estate
    }
  ) {
    price
    nft {
      estate {
        size
      }
    }
  }
}
    """
    variables = {'count': count}
    url = app.config['THEGRAPH_DECENTRALAND_URL']

    response_parcel = requests.post(url, json={'query': query_parcel, 'variables': variables})
    if response_parcel.status_code != HTTPStatus.OK:
        return jsonify({
            'count': count,
            'mean': -1,
            'error': response_parcel.text
        })
    data_parcel = [
        int(item['price'])
        for item
        in response_parcel.json()['data']['orders']]

    response_estate = requests.post(url, json={'query': query_estate, 'variables': variables})
    if response_estate.status_code != HTTPStatus.OK:
        return jsonify({
            'count': count,
            'mean': -1,
            'error': response_estate.text
        })
    data_estate = [
        calc_price(int(item['price']), item['nft']['estate'])
        for item
        in response_estate.json()['data']['orders']]

    data = data_parcel + data_estate
    np_arr = np.array(data)
    np_mean = np.mean(np_arr)

    return jsonify({'count': len(data), 'mean': int(np_mean)})
