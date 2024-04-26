from flask import Blueprint, request, jsonify
from src.services.WharehouseService import WharehouseService
from src.models.wharehouseModel import Wharehouse

getWharehouse= Blueprint('wharehouse_blueprint_get', __name__)


@getWharehouse.route('/',methods=['GET'])

def get_wharehouse():
    list_wharehouse = WharehouseService.get_wharehouse();
   
    print("Consola: Almacen obtenido.")

    return jsonify(list_wharehouse)