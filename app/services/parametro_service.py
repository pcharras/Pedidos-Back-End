from app.models import Parametro
from app import db

class ParametroService:
    @staticmethod
    def get_parametro_by_id(parametro_id):
        return Parametro.query.get(parametro_id)

    @staticmethod
    def create_parametro(nombre, valor):
        new_parametro = Parametro(nombre=nombre, valor=valor)
        db.session.add(new_parametro)
        db.session.commit()
        return new_parametro

    @staticmethod
    def update_parametro(parametro_id, nombre=None, valor=None):
        parametro = ParametroService.get_parametro_by_id(parametro_id)
        if parametro:
            if nombre is not None:
                parametro.nombre = nombre
            if valor is not None:
                parametro.valor = valor
            db.session.commit()
        return parametro

    @staticmethod
    def delete_parametro(parametro_id):
        parametro = ParametroService.get_parametro_by_id(parametro_id)
        if parametro:
            db.session.delete(parametro)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_parametros():
        return Parametro.query.all()