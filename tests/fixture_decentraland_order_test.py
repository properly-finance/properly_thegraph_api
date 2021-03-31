import pytest
from . import consts


@pytest.mark.parametrize('count', [10])
def test_order_loader(
    app,
    graphql_wraper,
    count
):
    query = """
    {
      orders (first:%(count)d, orderBy:updatedAt, orderDirection:desc){
        price
      }
    }
    """ % {'count': count}
    url = app.config['THEGRAPH_DECENTRALAND_URL']
    resp = graphql_wraper(url,
                          query,
                          consts.DECENTRALAND_PATHNAME,
                          f'{consts.DECENTRALAND_ORDER_FILENAME}_{count}')
    assert resp
