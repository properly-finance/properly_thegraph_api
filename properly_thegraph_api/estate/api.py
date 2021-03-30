def init_app(app):
    from .resources import api
    app.register_blueprint(api)
