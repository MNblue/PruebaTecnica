from flask import Blueprint, request, jsonify
from src.services.DeviceService import DeviceService
from src.models.deviceModel import Device

getDevice = Blueprint('device_blueprint_get', __name__)


@getDevice.route('/',methods=['GET'])

def get_Device():
    list_device = DeviceService.get_device()
   
    print("Consola: Dispositivos obtenidas.")

    return jsonify(list_device)