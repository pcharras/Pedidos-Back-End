from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.pedido_service import PedidoService

pedido_api_blueprint = Blueprint('pedido_api', __name__)
api = Api(pedido_api_blueprint)

class PedidoResource(Resource):
    def get(self, id):
        pedido = PedidoService.get_pedido_by_id(id)
        if pedido:
            return jsonify(pedido.serialize())
        return {'message': 'Pedido not found'}, 404

    def put(self, id):
        data = request.get_json()
        pedido = PedidoService.update_pedido(id, **data)
        if pedido:
            return jsonify(pedido.serialize())
        return {'message': 'Pedido not found'}, 404

    def delete(self, id):
        if PedidoService.delete_pedido(id):
            return {'message': 'Pedido deleted'}, 200
        return {'message': 'Pedido not found'}, 404

class PedidoListResource(Resource):
    def get(self):
        pedidos = PedidoService.get_all_pedidos()
        return jsonify([pedido.serialize() for pedido in pedidos])
        
    def post(self):
        data = request.get_json()
        pedido = PedidoService.create_pedido(**data)
        return jsonify(pedido.serialize())

api.add_resource(PedidoResource, '/pedidos/<int:id>')
api.add_resource(PedidoListResource, '/pedidos')