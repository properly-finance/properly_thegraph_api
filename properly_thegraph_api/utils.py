import ast
import os
from .errors import ImproperlyConfigured


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


def ast_env_variable(name, allow_none=False, default=None):
    if name in os.environ:
        value = os.environ[name]
        try:
            return ast.literal_eval(value)
        except ValueError as e:
            raise ValueError(f"{value} is an invalid value for {name}") from e

    if default is not None:
        return default

    if allow_none is False:
        raise ImproperlyConfigured(f"Set the {var_name} environment variable")

    return None
