def init_app(app):
    from .estate import resources as estate_resources
    from .order import resources as order_resources
    app.register_blueprint(estate_resources.api)
    app.register_blueprint(order_resources.api)
