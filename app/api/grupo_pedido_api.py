from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.grupo_pedido_service import GrupoPedidoService

grupo_pedido_api_blueprint = Blueprint('grupo_pedido_api', __name__)
api = Api(grupo_pedido_api_blueprint)

class GrupoPedidoResource(Resource):
    def get(self, id):
        grupo_pedido = GrupoPedidoService.get_grupo_pedido_by_id(id)
        if grupo_pedido:
            return jsonify(grupo_pedido.serialize())
        return {'message': 'Grupo de pedido no encontrado'}, 404

    def put(self, id):
        data = request.get_json()
        grupo_pedido = GrupoPedidoService.update_grupo_pedido(id, **data)
        if grupo_pedido:
            return jsonify(grupo_pedido.serialize())
        return {'message': 'Grupo de pedido no encontrado'}, 404

    def delete(self, id):
        if GrupoPedidoService.delete_grupo_pedido(id):
            return {'message': 'Grupo de pedido eliminado'}, 200
        return {'message': 'Grupo de pedido no encontrado'}, 404

class GrupoPedidoListResource(Resource):
    def get(self):
        grupos_pedidos = GrupoPedidoService.get_all_grupos_pedidos()
        return jsonify([grupo_pedido.serialize() for grupo_pedido in grupos_pedidos])
        
    def post(self):
        data = request.get_json()
        grupo_pedido = GrupoPedidoService.create_grupo_pedido(**data)
        return jsonify(grupo_pedido.serialize())

api.add_resource(GrupoPedidoResource, '/grupos-pedidos/<int:id>')
api.add_resource(GrupoPedidoListResource, '/grupos-pedidos')