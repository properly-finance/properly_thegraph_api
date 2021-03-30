from .utils import env_variable, ast_env_variable

FLASK_ENV = env_variable("FLASK_ENV")


class Config:

    def init_app(self, app):
        app.config.from_object(self)

    DEBUG = ast_env_variable("DEBUG", default=False)


config = Config()
