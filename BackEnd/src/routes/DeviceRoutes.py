from flask import Blueprint, request, jsonify
from src.services.DeviceService import DeviceService
from src.models.deviceModel import Device
from flask_cors import cross_origin

routeDevice = Blueprint('device_blueprint_get', __name__)
# searchDevice = Blueprint('search_blueprint_device', __name__)

@routeDevice.route('/')
@cross_origin(origins='*', methods=['GET', 'POST', 'PATCH', 'DELETE', 'OPTIONS'])
# @routeDevice.route('/', methods=['GET', 'POST', 'PATCH', 'DELETE', 'OPTIONS'], strict_slashes=False)
def get_Device():

    if request.method == "GET":
        print("cuccuucuc")

        list_device = DeviceService.get_device()
   
        print("Consola: Dispositivos obtenidas.")

        return jsonify(list_device)
    
    elif request.method == 'OPTIONS':
        print("optionsss ucucucuc")

        response = jsonify({'message': 'Preflight request success'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,PATCH,POST,DELETE,OPTIONS')
        return response
    

# @routeDevice.route('/',methods=['OPTIONS'])
# def option_Device():

#     print("cuccuucuc OPTIONSSS")

#     response = jsonify({'message': 'Preflight request success'})
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,PATCH,POST,DELETE')
#     return response

# @routeDevice.route("/", methods=["POST"])
# def post_device():

#     name = request.json["device_name"]
#     fee = request.json["fee"]
#     newDevice = Device("",name,"",fee)


#     if DeviceService.post_device(newDevice):
#         return "Dispositivo agregado"
#     else:
#         return "Error al agregar dispositivo"



# @routeDevice.route("/", methods=["PATCH"])
# def patch_device():
    
#     id_device = request.json["id_device"]
#     name = request.json["device_name"]
#     time = request.json["addition_time"]
#     fee = request.json["fee"]

#     updateDevice = Device(id_device,name,time,fee)

#     if DeviceService.patch_device(updateDevice):
#         return "Dispositivo actualizado."
#     else:
#         return "Error al actualizar dispositivo"


# @routeDevice.route("/", methods=["DELETE"])
# def delete_device():
    
#     id_device = request.json["id_device"]

#     if DeviceService.delete_Device(id_device):
#         return "Diospositivo eliminado."
#     else:
#         return "Error al eliminar dispositivo"

# @searchDevice.route('/',methods=['GET'])
# def search_device():

#     id_device = request.json["id_device"]
#     device = DeviceService.search_device(id_device)
   
#     print("Consola: dispositivo obtenido.")

#     return jsonify(device)