import os
import rapidjson
from decimal import Decimal
from enum import Enum

from typing import List, Callable, Dict
from flask import testing, json


class ImproperlyConfigured(Exception):
    pass


def env_variable(var_name, allow_none=False, default=None):
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        if allow_none is False:
            raise ImproperlyConfigured(
                f"Set the {var_name} environment variable")
        return None


class FixtureLoader(object):

    def __init__(self, path):
        self.path = path
        self.type = path.split('.')[-1]

    def load(self):
        with open(self.path, 'r') as f:
            data = f.read()
            if self.type == 'json':
                data = rapidjson.loads(data,
                    datetime_mode=rapidjson.DM_ISO8601 | rapidjson.DM_NAIVE_IS_UTC)
            return data


class FixtureWriter(object):

    def __init__(self, path, data):
        self.path = path
        self.data = data

    @staticmethod
    def default(obj):
        if isinstance(obj, Enum):
            return obj.name
        elif isinstance(obj, Decimal):
            return float(obj)
        else:
            return obj

    def write(self):
        name_dir = '/'.join(self.path.split('/')[:-1])
        if not os.path.exists(name_dir):
            os.makedirs(name_dir)

        data = rapidjson.dumps(self.data,
            sort_keys=True,
            datetime_mode=rapidjson.DM_ISO8601 | rapidjson.DM_NAIVE_IS_UTC,
            default=self.default)

        with open(self.path, 'w') as f:
            f.write(data)

    def text(self):
        name_dir = '/'.join(self.path.split('/')[:-1])
        if not os.path.exists(name_dir):
            os.makedirs(name_dir)

        with open(self.path, 'w') as f:
            f.write(self.data)


class JsonApiClient(testing.FlaskClient):

    def __init__(self, *args, **kwargs):

        super(JsonApiClient, self).__init__(*args, **kwargs)

    def open(self, *args, **kwargs):

        data = kwargs.get("data")

        if data is not None and not kwargs.get("content_type"):
            kwargs["data"] = json.dumps(data)
            kwargs["content_type"] = "application/json"
            kwargs.setdefault("headers", {})["Accept"] = "application/json"

        if data is None and kwargs.get("content_type"):
            kwargs["content_type"] = kwargs["content_type"]
            kwargs.setdefault("headers", {})["Accept"] = kwargs["content_type"]

        return super(JsonApiClient, self).open(*args, **kwargs)
