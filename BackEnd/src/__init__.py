from flask import Flask
from src.routes import DeviceRoutes

app= Flask(__name__)


def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(DeviceRoutes.get_device, url_prefix='/device')

    return app