from http import HTTPStatus


def test_ping_ok(client, app):
    response = client.get('/decentraland/estate/ping')
    assert response.status_code == HTTPStatus.OK
    response_data = response.json
    assert response_data['value'] == 42


def test_echo_ok(client, app):
    me_query = "query fetchMe {me {d, email}}"
    data = {'query': me_query}
    response = client.post('/decentraland/estate/echo', data=data)
    assert response.status_code == HTTPStatus.OK
    response_data = response.json
    assert response_data['query'] == me_query
