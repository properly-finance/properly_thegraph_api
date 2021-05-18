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


@pytest.mark.parametrize('count', [10])
def test_order_parcel_loader(
    app,
    graphql_wraper,
    count
):
    query = """
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
    variables = {'count': count}
    url = app.config['THEGRAPH_DECENTRALAND_URL']
    resp = graphql_wraper(
        url,
        query,
        consts.DECENTRALAND_PATHNAME,
        f'{consts.DECENTRALAND_ORDER_FILENAME}_parcel_{count}',
        variables=variables
    )
    assert resp


@pytest.mark.parametrize('count', [10])
def test_order_estate_loader(
    app,
    graphql_wraper,
    count
):
    query = """
query fetchParcelOrders($count: Int) {
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
    resp = graphql_wraper(
        url,
        query,
        consts.DECENTRALAND_PATHNAME,
        f'{consts.DECENTRALAND_ORDER_FILENAME}_estate_{count}',
        variables=variables
    )
    assert resp
