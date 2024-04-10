from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.parametro_service import ParametroService

parametro_api_blueprint = Blueprint('parametro_api', __name__)
api = Api(parametro_api_blueprint)

class ParametroResource(Resource):
    def get(self, id):
        parametro = ParametroService.get_parametro_by_id(id)
        if parametro:
            return jsonify(parametro.serialize())
        return {'message': 'Parametro not found'}, 404

    def put(self, id):
        data = request.get_json()
        parametro = ParametroService.update_parametro(id, **data)
        if parametro:
            return jsonify(parametro.serialize())
        return {'message': 'Parametro not found'}, 404

    def delete(self, id):
        if ParametroService.delete_parametro(id):
            return {'message': 'Parametro deleted'}, 200
        return {'message': 'Parametro not found'}, 404

class ParametroListResource(Resource):
    def get(self):
        parametros = ParametroService.get_all_parametros()
        return jsonify([parametro.serialize() for parametro in parametros])
        
    def post(self):
        data = request.get_json()
        parametro = ParametroService.create_parametro(**data)
        return jsonify(parametro.serialize())

api.add_resource(ParametroResource, '/parametros/<int:id>')
api.add_resource(ParametroListResource, '/parametros')