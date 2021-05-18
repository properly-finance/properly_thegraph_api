import pytest
from http import HTTPStatus
from . import consts


def side_effect_post(mocker, datadict):
    def wrap(*args, **kwargs):
        patch_fixture = None
        if 'fetchParcelOrders' in kwargs['json']['query']:
            patch_fixture = datadict['parcel']
        if 'fetchEstateOrders' in kwargs['json']['query']:
            patch_fixture = datadict['estate']
        response_mock = mocker.Mock()
        response_mock.status_code = 200
        response_mock.json = mocker.Mock(return_value=patch_fixture)
        return response_mock
    return wrap


@pytest.mark.parametrize('count', [10])
def test_price_mean(
    mocker,
    patch_request_post_side_effect,
    graphql_loader_json,
    client,
    app,
    count
):
    response_parcel_stub = graphql_loader_json(
        consts.DECENTRALAND_PATHNAME,
        f'{consts.DECENTRALAND_ORDER_FILENAME}_parcel_{count}')
    response_estate_stub = graphql_loader_json(
        consts.DECENTRALAND_PATHNAME,
        f'{consts.DECENTRALAND_ORDER_FILENAME}_estate_{count}')

    patch_request_post_side_effect(side_effect_post(mocker, {
        'parcel': response_parcel_stub,
        'estate': response_estate_stub,
    }))

    response = client.get(f'/decentraland/orders/price-mean/{count}')
    assert response.status_code == HTTPStatus.OK
    response_data = response.json
    assert response_data['count'] == count * 2
    assert response_data['mean']
    print(response_data['mean'])
