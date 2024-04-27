from flask import Flask
from src.routes import DeviceRoutes
from src.routes import IndustryRoutes
from src.routes import WharehouseRoutes

app= Flask(__name__)


def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(DeviceRoutes.routeDevice, url_prefix='/device')
    app.register_blueprint(IndustryRoutes.routeIndustry, url_prefix='/industry')
    app.register_blueprint(WharehouseRoutes.routeWharehouse, url_prefix='/wharehouse')

    app.register_blueprint(IndustryRoutes.searchIndustry, url_prefix='/industrySearch')
    app.register_blueprint(DeviceRoutes.searchDevice, url_prefix='/deviceSearch')

    return app