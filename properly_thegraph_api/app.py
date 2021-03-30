from flask import Flask


def create_app():
    from .config import config
    from .estate import api as asestate_api

    app = Flask(__name__.split(".")[0])
    config.init_app(app)
    asestate_api.init_app(app)

    return app


app = create_app()
