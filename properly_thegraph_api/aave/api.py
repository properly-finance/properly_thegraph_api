def init_app(app):
    from .flashloans import resources as flashloans_resources
    app.register_blueprint(flashloans_resources.api)
