import pytest
from http import HTTPStatus
from . import consts


def test_amount_mean_default(
    patch_request_post,
    graphql_loader_json,
    client,
    app,
):
    response_stub = graphql_loader_json(consts.AAVE_PATHNAME,
                                        f'{consts.AAVE_FLASHLOANS_FILENAME}_1000')
    patch_request_post(response_stub)

    response = client.get('/aave/flashloans/amount-mean')
    assert response.status_code == HTTPStatus.OK
    response_data = response.json
    assert response_data['count'] == 10
    assert response_data['mean']


@pytest.mark.parametrize('count', [20, 30, 40])
def test_amount_mean(
    patch_request_post,
    graphql_loader_json,
    client,
    app,
    count
):
    response_stub = graphql_loader_json(consts.AAVE_PATHNAME,
                                        consts.AAVE_FLASHLOANS_FILENAME)
    patch_request_post(response_stub)

    response = client.get(f'/aave/flashloans/amount-mean/{count}')
    assert response.status_code == HTTPStatus.OK
    response_data = response.json
    assert response_data['count'] == count
    assert response_data['mean']
