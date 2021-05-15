import pytest
from http import HTTPStatus
from . import consts


@pytest.mark.parametrize('count', [10])
def test_price_mean(
    patch_request_post,
    graphql_loader_json,
    client,
    app,
    count
):
    response_stub = graphql_loader_json(
        consts.DECENTRALAND_PATHNAME,
        f'{consts.DECENTRALAND_NFT_ORDER_FILENAME}_{count}')
    patch_request_post(response_stub)

    response = client.get(f'/decentraland/orders/price-mean/{count}')
    assert response.status_code == HTTPStatus.OK
    response_data = response.json
    assert response_data['count'] == count
    assert response_data['mean']
    print(response_data['mean'])
