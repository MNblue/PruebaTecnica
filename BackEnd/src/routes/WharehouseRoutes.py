from flask import Blueprint, request, jsonify
from src.services.WharehouseService import WharehouseService
from src.models.wharehouseModel import Wharehouse

routeWharehouse= Blueprint('wharehouse_blueprint_get', __name__)


@routeWharehouse.route('/',methods=['GET'])
def get_wharehouse():
    list_wharehouse = WharehouseService.get_wharehouse()
   
    print("Consola: Almacen obtenido.")

    return jsonify(list_wharehouse)



@routeWharehouse.route("/", methods=["POST"])
def post_wharehouse():

    id_device = request.json["id_device"]
    id_industry = request.json["id_industry"]
    newWharehouse = Wharehouse(id_device,id_industry)

    if WharehouseService.post_wharehouse(newWharehouse):
        return "almacen agregada"
    else:
        return "Error al agregar almacen"

@routeWharehouse.route("/", methods=["PATCH"])
def patch_wharehouse():
    
    id_industry = request.json["id_industry"]
    id_device = request.json["id_device"]
    updateWharehouse = Wharehouse(id_device,id_industry)

    if WharehouseService.patch_wharehouse(updateWharehouse):
        return "almacen actualizado."
    else:
        return "Error al actualizar almacen"


@routeWharehouse.route("/", methods=["DELETE"])
def delete_wharehouse():
    
    id_device = request.json["id_device"]
    id_industry = request.json["id_industry"]

    if WharehouseService.delete_wharehouse(id_device,id_industry):
        return "almacen eliminada."
    else:
        return "Error al eliminar almacen"