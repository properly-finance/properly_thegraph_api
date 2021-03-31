from . import consts


def test_aave_flash_loans_loader_10(app, graphql_wraper):
    query = """
    {
      flashLoans (first: 10, orderBy: timestamp, orderDirection:desc){
        id
        amount
        target
        timestamp
      }
    }
    """
    url = app.config['THEGRAPH_AAVE_URL']
    resp = graphql_wraper(url,
                          query,
                          consts.AAVE_PATHNAME,
                          consts.AAVE_FLASHLOANS_FILENAME)
    assert resp


def test_aave_flash_loans_loader_100(app, graphql_wraper):
    query = """
    {
      flashLoans (first: 100, orderBy: timestamp, orderDirection:desc){
        id
        amount
      }
    }
    """
    url = app.config['THEGRAPH_AAVE_URL']
    resp = graphql_wraper(url,
                          query,
                          consts.AAVE_PATHNAME,
                          f'{consts.AAVE_FLASHLOANS_FILENAME}_100')
    assert resp


def test_aave_flash_loans_loader_1000(app, graphql_wraper):
    query = """
    {
      flashLoans (first: 1000, orderBy: timestamp, orderDirection:desc){
        id
        amount
      }
    }
    """
    url = app.config['THEGRAPH_AAVE_URL']
    resp = graphql_wraper(url,
                          query,
                          consts.AAVE_PATHNAME,
                          f'{consts.AAVE_FLASHLOANS_FILENAME}_1000')
    assert resp
