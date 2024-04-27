from flask import Blueprint, request, jsonify
from src.services.IndustryService import IndustryService
from src.models.industryModel import Industry

routeIndustry= Blueprint('industry_blueprint', __name__)
searchIndustry = Blueprint('search_blueprint_industry', __name__)


@routeIndustry.route('/',methods=['GET'])
def get_industry():
    list_industry = IndustryService.get_Industry()
   
    print("Consola: Industrias obtenidas.")

    return jsonify(list_industry)


@routeIndustry.route("/", methods=["POST"])
def post_industry():

    name = request.json["industry_name"]
    newIndustry = Industry("",name)

    if IndustryService.post_Industry(newIndustry):
        return "Industria agregada"
    else:
        return "Error al agregar industria"



@routeIndustry.route("/", methods=["PATCH"])
def patch_industry():
    
    id_industry = request.json["id_industry"]
    name = request.json["industry_name"]
    updateIndustry = Industry(id_industry,name)

    if IndustryService.patch_Industry(updateIndustry):
        return "Industria actualizada."
    else:
        return "Error al actualizar industria"


@routeIndustry.route("/", methods=["DELETE"])
def delete_industry():
    
    id_industry = request.json["id_industry"]

    if IndustryService.delete_Industry(id_industry):
        return "Industria eliminada."
    else:
        return "Error al eliminar industria"

@searchIndustry.route('/',methods=['GET'])
def search_industry():

    id_industry = request.json["id_industry"]
    industry = IndustryService.search_Industry(id_industry)
   
    print("Consola: Industria obtenida.")

    return jsonify(industry)