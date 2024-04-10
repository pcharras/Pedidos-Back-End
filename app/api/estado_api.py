from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.estado_service import EstadoService

estado_api_blueprint = Blueprint('estado_api', __name__)
api = Api(estado_api_blueprint)

class EstadoResource(Resource):
    def get(self, id):
        estado = EstadoService.get_estado_by_id(id)
        if estado:
            return jsonify(estado.serialize())
        return {'message': 'Estado not found'}, 404

    def put(self, id):
        data = request.get_json()
        estado = EstadoService.update_estado(id, **data)
        if estado:
            return jsonify(estado.serialize())
        return {'message': 'Estado not found'}, 404

    def delete(self, id):
        if EstadoService.delete_estado(id):
            return {'message': 'Estado deleted'}, 200
        return {'message': 'Estado not found'}, 404

class EstadoListResource(Resource):
    def get(self):
        estados = EstadoService.get_all_estados()
        return jsonify([estado.serialize() for estado in estados])
        
    def post(self):
        data = request.get_json()
        estado = EstadoService.create_estado(**data)
        return jsonify(estado.serialize())

api.add_resource(EstadoResource, '/estados/<int:id>')
api.add_resource(EstadoListResource, '/estados')