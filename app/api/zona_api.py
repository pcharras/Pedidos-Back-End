from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.zona_service import ZonaService

zona_api_blueprint = Blueprint('zona_api', __name__)
api = Api(zona_api_blueprint)

class ZonaResource(Resource):
    def get(self, id):
        zona = ZonaService.get_zona_by_id(id)
        if zona:
            return jsonify(zona.serialize())
        return {'message': 'Zona not found'}, 404

    def put(self, id):
        data = request.get_json()
        zona = ZonaService.update_zona(id, **data)
        if zona:
            return jsonify(zona.serialize())
        return {'message': 'Zona not found'}, 404

    def delete(self, id):
        if ZonaService.delete_zona(id):
            return {'message': 'Zona deleted'}, 200
        return {'message': 'Zona not found'}, 404

class ZonaListResource(Resource):
    def get(self):
        zonas = ZonaService.get_all_zonas()
        return jsonify([zona.serialize() for zona in zonas])
        
    def post(self):
        data = request.get_json()
        zona = ZonaService.create_zona(**data)
        print(zona.serialize())
        return jsonify(zona.serialize())
        

api.add_resource(ZonaResource, '/zonas/<int:id>')
api.add_resource(ZonaListResource, '/zonas')