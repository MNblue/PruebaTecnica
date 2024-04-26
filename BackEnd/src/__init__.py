from flask import Flask
from src.routes import DeviceRoutes
from src.routes import IndustryRoutes
from src.routes import WharehouseRoutes

app= Flask(__name__)


def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(DeviceRoutes.getDevice, url_prefix='/device')
    app.register_blueprint(IndustryRoutes.getIndustry, url_prefix='/industry')
    app.register_blueprint(WharehouseRoutes.getWharehouse, url_prefix='/wharehouse')

    return app