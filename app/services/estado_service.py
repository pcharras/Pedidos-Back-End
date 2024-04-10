from app.models import Estado
from app import db

class EstadoService:
    @staticmethod
    def get_estado_by_id(estado_id):
        return Estado.query.get(estado_id)

    @staticmethod
    def create_estado(nombre):
        new_estado = Estado(nombre=nombre)
        db.session.add(new_estado)
        db.session.commit()
        return new_estado

    @staticmethod
    def update_estado(estado_id, nombre=None):
        estado = EstadoService.get_estado_by_id(estado_id)
        if estado and nombre is not None:
            estado.nombre = nombre
            db.session.commit()
        return estado

    @staticmethod
    def delete_estado(estado_id):
        estado = EstadoService.get_estado_by_id(estado_id)
        if estado:
            db.session.delete(estado)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_estados():
        return Estado.query.all()