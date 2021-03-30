def test_riseup(app):
    assert app
    assert app.config
    assert bool(app.config['DEBUG']) is True


def test_endpoints(app):
    endpoints = [rule.endpoint for rule in app.url_map.iter_rules()]
    # estate
    assert 'api_estate.test' in endpoints
#     assert 'api_v1.user_registration_2' in endpoints
#     assert 'api_v1.user_no_exists_2' in endpoints
#     # payments
#     assert 'api_v1.payment_plans_2' in endpoints
#     assert 'api_v1.payment_subscribe_2' in endpoints
#     assert 'api_v1.payment_webhook_2' in endpoints
