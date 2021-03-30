from http import HTTPStatus


def test_test_ok(client, app):
    response = client.get('/estate/test')
    assert response.status_code == HTTPStatus.OK

    response_data = response.json
    assert response_data['text'] == 'hi'
