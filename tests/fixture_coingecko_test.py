# curl -X GET "https://api.coingecko.com/api/v3/coins/list" -H "accept: application/json"
# curl -X GET "https://api.coingecko.com/api/v3/simple/supported_vs_currencies" -H "accept: application/json"
# curl -X GET "https://api.coingecko.com/api/v3/simple/price?ids=aave-mana&vs_currencies=eth" -H "accept: application/json"


def test_coingecko_mana_eth(coingecko_wraper):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'aave-mana',
        'vs_currencies': 'eth'
    }
    response = coingecko_wraper(url, params, 'mana_eth')
    assert response
