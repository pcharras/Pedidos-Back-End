from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.punto_poligono_zona_service import PuntoPoligonoZonaService

punto_poligono_zona_api_blueprint = Blueprint('punto_poligono_zona_api', __name__)
api = Api(punto_poligono_zona_api_blueprint)

class PuntoPoligonoZonaResource(Resource):
    def get(self, id):
        punto = PuntoPoligonoZonaService.get_punto_by_id(id)
        if punto:
            return jsonify(punto.serialize())
        return {'message': 'Punto not found'}, 404

    def put(self, id):
        data = request.get_json()
        punto = PuntoPoligonoZonaService.update_punto(id, **data)
        if punto:
            return jsonify(punto.serialize())
        return {'message': 'Punto not found'}, 404

    def delete(self, id):
        if PuntoPoligonoZonaService.delete_punto(id):
            return {'message': 'Punto deleted'}, 200
        return {'message': 'Punto not found'}, 404

class PuntoPoligonoZonaListResource(Resource):
    def get(self):
        puntos = PuntoPoligonoZonaService.get_all_puntos()
        return jsonify([punto.serialize() for punto in puntos])
        
    def post(self):
        data = request.get_json()
        punto = PuntoPoligonoZonaService.create_punto(**data)
        return jsonify(punto.serialize())

api.add_resource(PuntoPoligonoZonaResource, '/puntos-poligono-zona/<int:id>')
api.add_resource(PuntoPoligonoZonaListResource, '/puntos-poligono-zona')