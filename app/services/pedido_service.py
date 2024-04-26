from app.models import Pedido
from app import db

class PedidoService:
    @staticmethod
    def get_pedido_by_id(pedido_id):
        return Pedido.query.get(pedido_id)

    @staticmethod
    def get_pedidos_by_grupo(id_grupo):
        return Pedido.query.filter_by(id_grupo=id_grupo).all()

    @staticmethod
    def create_pedido(id_grupo, direccion, latitud, longitud, id_estado, cliente, pedido, telefono):
        new_pedido = Pedido(
            id_grupo=id_grupo,
            direccion=direccion,
            latitud=latitud,
            longitud=longitud,
            id_estado=id_estado,
            cliente=cliente,
            pedido=pedido,
            telefono=telefono
        )
        db.session.add(new_pedido)
        db.session.commit()
        return new_pedido

    @staticmethod
    def update_pedido(pedido_id, id_grupo=None, direccion=None, latitud=None, longitud=None, id_estado=None, cliente=None, pedido=None, telefono=None):
        pedido = PedidoService.get_pedido_by_id(pedido_id)
        if pedido:
            if id_grupo is not None:
                pedido.id_grupo = id_grupo
            if direccion is not None:
                pedido.direccion = direccion
            if latitud is not None:
                pedido.latitud = latitud
            if longitud is not None:
                pedido.longitud = longitud
            if id_estado is not None:
                pedido.id_estado = id_estado
            if cliente is not None:
                pedido.cliente = cliente
            if pedido is not None:
                pedido.pedido = pedido
            if telefono is not None:
                pedido.telefono = telefono
            db.session.commit()
        return pedido

    @staticmethod
    def delete_pedido(pedido_id):
        pedido = PedidoService.get_pedido_by_id(pedido_id)
        if pedido:
            db.session.delete(pedido)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_pedidos():
        return Pedido.query.all()