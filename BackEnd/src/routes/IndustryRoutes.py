from flask import Blueprint, request, jsonify
from src.services.IndustryService import IndustryService
from src.models.industryModel import Industry

getIndustry= Blueprint('industry_blueprint_get', __name__)


@getIndustry.route('/',methods=['GET'])

def get_Industry():
    list_industry = IndustryService.get_Industry()
   
    print("Consola: Industrias obtenidas.")

    return jsonify(list_industry)