def init_app(app):
    from .estate import resources as estate_resources
    app.register_blueprint(estate_resources.api)
