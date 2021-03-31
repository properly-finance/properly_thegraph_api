def test_riseup(app):
    assert app
    assert app.config
    assert bool(app.config['DEBUG']) is True


def test_endpoints(app):
    endpoints = [rule.endpoint for rule in app.url_map.iter_rules()]
    # print(endpoints)
    assert 'decentraland_estate_api.ping' in endpoints
    assert 'decentraland_estate_api.echo' in endpoints
    assert 'aave_flashloans_api.amount_mean' in endpoints
