import pytest
import logging
# from datetime import datetime, timezone, timedelta

from properly_thegraph_api.app import create_app
from .utils import (
    env_variable,
    JsonApiClient
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
    def wrap(user):
        with app.test_client() as client:
            yield client
    return wrap
