import os
import pytest
import logging
import requests
# from datetime import datetime, timezone, timedelta

from properly_thegraph_api.app import create_app
from .utils import (
    env_variable,
    JsonApiClient,
    FixtureLoader,
    FixtureWriter
)


#######################################################################


logging.getLogger().setLevel(logging.DEBUG)


FIXTURE_PATH = env_variable('FIXTURE_PATH')


@pytest.fixture(scope='session')
def app():
    application = create_app()
    application.testing = True
    # application.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
    # application.config['FLASK_DEBUG'] = False
    application.test_client_class = JsonApiClient
    with application.app_context():
        yield application


@pytest.fixture
def app_client(app):
    def wrap():
        with app.test_client() as client:
            yield client
    return wrap


@pytest.fixture
def requester_get():
    def wrap(url, params={}):
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f'Error reponce from {url}')
        return response.json()
    return wrap


@pytest.fixture
def requester():
    def wrap(url, query, variables={}):
        data = {
            'query': query,
            'variables': variables,
        }
        response = requests.post(url, json=data)
        if response.status_code != 200:
            raise Exception(f'Error reponce from {url} '
                            f'text={response.text}')
        return response.json()
    return wrap


@pytest.fixture
def fixture_loader():
    def wrap(path):
        return FixtureLoader(path).load()
    return wrap


@pytest.fixture
def fixture_writer():
    def wrap(path, data):
        FixtureWriter(path, data).write()
    return wrap


@pytest.fixture
def fixture_check_path():
    def wrap(path):
        if os.path.isfile(path):
            return True
        return False
    return wrap

# ------------------------ graphql ----------------------


@pytest.fixture
def graphql_writer(requester,
                   fixture_check_path,
                   fixture_writer):
    def write(url, query, variables, path):
        if fixture_check_path(path):
            return
        response = requester(url, query, variables)
        fixture_writer(path, response)
    return write


@pytest.fixture
def graphql_wraper(graphql_writer,
                   fixture_loader):
    def wrap(url, query, pathname, filename, variables={}):
        path = f"{FIXTURE_PATH}/{pathname}/{filename}.json"
        graphql_writer(url, query, variables, path)
        response = fixture_loader(path)
        return response
    return wrap


@pytest.fixture
def graphql_loader_json(fixture_loader):
    def wrap(pathname, filename):
        path = f"{FIXTURE_PATH}/{pathname}/{filename}.json"
        response = fixture_loader(path)
        return response
    return wrap


# ------------------------ coingecko ----------------------


@pytest.fixture
def coingecko_writer(requester_get,
                     fixture_check_path,
                     fixture_writer):
    def write(url, params, path):
        if fixture_check_path(path):
            return
        response = requester_get(url, params)
        fixture_writer(path, response)
    return write


@pytest.fixture
def coingecko_wraper(coingecko_writer,
                     fixture_loader):
    def wrap(url, params, filename):
        path = f"{FIXTURE_PATH}/coingecko/{filename}.json"
        coingecko_writer(url, params, path)
        response = fixture_loader(path)
        return response
    return wrap


# ------------------------ patch ----------------------


@pytest.fixture
def patch_request_post(mocker):
    def wrap(patch_fixture):
        response_mock = mocker.Mock()
        response_mock.status_code = 200
        response_mock.json = mocker.Mock(return_value=patch_fixture)
        client = mocker.patch('requests.post')
        client.return_value = response_mock
        return client
    return wrap


@pytest.fixture
def patch_request_post_side_effect(mocker):
    def wrap(side_effect_fn):
        client = mocker.patch('requests.post',
            mocker.Mock(side_effect=side_effect_fn, autospec=True))
        return client
    return wrap


@pytest.fixture
def patch_request_get(mocker):
    def wrap(patch_fixture):
        response_mock = mocker.Mock()
        response_mock.status_code = 200
        response_mock.json = mocker.Mock(return_value=patch_fixture)
        client = mocker.patch('requests.get')
        client.return_value = response_mock
        return client
    return wrap
