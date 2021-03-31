from flask import Flask


def create_app():
    from .config import config
    from .decentraland import api as decentraland_api
    from .aave import api as aave_api

    app = Flask(__name__.split(".")[0])
    config.init_app(app)
    decentraland_api.init_app(app)
    aave_api.init_app(app)

    return app


app = create_app()
