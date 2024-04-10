from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.cadete_service import CadeteService

cadete_api_blueprint = Blueprint('cadete_api', __name__)
api = Api(cadete_api_blueprint)

class CadeteResource(Resource):
    def get(self, id):
        cadete = CadeteService.get_cadete_by_id(id)
        if cadete:
            return jsonify(cadete.serialize())
        return {'message': 'Cadete not found'}, 404

    def put(self, id):
        data = request.get_json()
        cadete = CadeteService.update_cadete(id, **data)
        if cadete:
            return jsonify(cadete.serialize())
        return {'message': 'Cadete not found'}, 404

    def delete(self, id):
        if CadeteService.delete_cadete(id):
            return {'message': 'Cadete deleted'}, 200
        return {'message': 'Cadete not found'}, 404

class CadeteListResource(Resource):
    def get(self):
        cadetes = CadeteService.get_all_cadetes()
        return jsonify([cadete.serialize() for cadete in cadetes])
        
    def post(self):
        data = request.get_json()
        cadete = CadeteService.create_cadete(**data)
        return jsonify(cadete.serialize())

api.add_resource(CadeteResource, '/cadetes/<int:id>')
api.add_resource(CadeteListResource, '/cadetes')