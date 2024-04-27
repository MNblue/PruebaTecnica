from flask import Flask
from src.routes import DeviceRoutes
from src.routes import IndustryRoutes
from src.routes import WharehouseRoutes
from flask_cors import CORS

app= Flask(__name__)
CORS(app,resources={"*":{"origins": "http://localhost:5173"}})
# CORS(app)

def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(DeviceRoutes.routeDevice, url_prefix='/device')
    app.register_blueprint(IndustryRoutes.routeIndustry, url_prefix='/industry')
    app.register_blueprint(WharehouseRoutes.routeWharehouse, url_prefix='/wharehouse')

    app.register_blueprint(IndustryRoutes.searchIndustry, url_prefix='/industrySearch')
    app.register_blueprint(DeviceRoutes.searchDevice, url_prefix='/deviceSearch')

    return app