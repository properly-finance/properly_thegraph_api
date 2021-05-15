import pytest
from . import consts


@pytest.mark.parametrize('count', [10])
def test_order_loader(
    app,
    graphql_wraper,
    count
):
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
    #         status
    #         category
    #       }
    #     }
    #   }
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
    resp = graphql_wraper(url,
                          query,
                          consts.DECENTRALAND_PATHNAME,
                          f'{consts.DECENTRALAND_NFT_ORDER_FILENAME}_{count}',
                          variables)
    assert resp
