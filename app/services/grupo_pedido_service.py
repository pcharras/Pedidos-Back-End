from app.models import GrupoPedido, Pedido
from app import db
from datetime import datetime

class GrupoPedidoService:
    @staticmethod
    def get_grupo_pedido_by_id(grupo_pedido_id):
        return GrupoPedido.query.get(grupo_pedido_id)

    @staticmethod
    def create_grupo_pedido(id_zona, fecha_hora_creacion, id_estado, id_cadete, fecha_hora_cierre=None, fecha_hora_envio=None):
        new_grupo_pedido = GrupoPedido(id_zona=id_zona, fecha_hora_creacion=fecha_hora_creacion, id_estado=id_estado, id_cadete=id_cadete, fecha_hora_cierre=fecha_hora_cierre, fecha_hora_envio=fecha_hora_envio)
        db.session.add(new_grupo_pedido)
        db.session.commit()
        return new_grupo_pedido

    @staticmethod
    def update_grupo_pedido(grupo_pedido_id, id_zona=None, fecha_hora_creacion=None, id_estado=None, id_cadete=None, fecha_hora_cierre=None, fecha_hora_envio=None):
        grupo_pedido = GrupoPedidoService.get_grupo_pedido_by_id(grupo_pedido_id)
        if grupo_pedido:
            if id_zona:
                grupo_pedido.id_zona = id_zona
            if fecha_hora_creacion:
                grupo_pedido.fecha_hora_creacion = fecha_hora_creacion
            if id_estado:
                grupo_pedido.id_estado = id_estado
            if id_cadete:
                grupo_pedido.id_cadete = id_cadete
            if fecha_hora_cierre:
                grupo_pedido.fecha_hora_cierre = fecha_hora_cierre
            if fecha_hora_envio:
                grupo_pedido.fecha_hora_envio = fecha_hora_envio
            db.session.commit()
        return grupo_pedido

    @staticmethod
    def delete_grupo_pedido(grupo_pedido_id):
        grupo_pedido = GrupoPedidoService.get_grupo_pedido_by_id(grupo_pedido_id)
        if grupo_pedido:
            db.session.delete(grupo_pedido)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_grupos_pedidos():
        return GrupoPedido.query.all()
    
    @staticmethod
    def get_all_grupos_pedidos_with_pedidos():
        grupos_pedidos = GrupoPedido.query.all()
        grupos_serializados = []
        for grupo_pedido in grupos_pedidos:
            # Obtener los pedidos asociados a este grupo de pedidos
            pedidos = Pedido.query.filter_by(id_grupo=grupo_pedido.id).all()
            # Serializar el grupo de pedidos y sus pedidos asociados
            grupo_serializado = {
                "id": grupo_pedido.id,
                "zona": {
                    "id": grupo_pedido.zona.id,
                    "nombre": grupo_pedido.zona.nombre
                },
                "fecha_hora_creacion": grupo_pedido.fecha_hora_creacion.isoformat() if grupo_pedido.fecha_hora_creacion else None,
                "fecha_hora_cierre": grupo_pedido.fecha_hora_cierre.isoformat() if grupo_pedido.fecha_hora_cierre else None,
                "fecha_hora_envio": grupo_pedido.fecha_hora_envio.isoformat() if grupo_pedido.fecha_hora_envio else None,
                "estado": {
                    "id": grupo_pedido.estado.id,
                    "nombre": grupo_pedido.estado.nombre
                },
                "cadete": {
                    "id": grupo_pedido.cadete.id if grupo_pedido.cadete else None,
                    "nombre": grupo_pedido.cadete.nombre if grupo_pedido.cadete else None,
                    "activo": grupo_pedido.cadete.activo if grupo_pedido.cadete else None
                },
                "pedidos": [pedido.serialize() for pedido in pedidos]
            }
            grupos_serializados.append(grupo_serializado)
        return grupos_serializados