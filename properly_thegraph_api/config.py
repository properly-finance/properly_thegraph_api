from .utils import env_variable, ast_env_variable

FLASK_ENV = env_variable('FLASK_ENV')


class Config:

    def init_app(self, app):
        app.config.from_object(self)

    DEBUG = ast_env_variable('DEBUG', default=False)
    THEGRAPH_DECENTRALAND_URL = env_variable('THEGRAPH_DECENTRALAND_URL')
    THEGRAPH_AAVE_URL = env_variable('THEGRAPH_AAVE_URL')

config = Config()
