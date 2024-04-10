from app.models import Zona
from app import db

class ZonaService:
    @staticmethod
    def get_zona_by_id(zona_id):
        return Zona.query.get(zona_id)

    @staticmethod
    def create_zona(nombre):
        new_zona = Zona(nombre=nombre)
        db.session.add(new_zona)
        db.session.commit()
        return new_zona

    @staticmethod
    def update_zona(zona_id, nombre=None):
        zona = ZonaService.get_zona_by_id(zona_id)
        if zona:
            if nombre is not None:
                zona.nombre = nombre
            db.session.commit()
        return zona

    @staticmethod
    def delete_zona(zona_id):
        zona = ZonaService.get_zona_by_id(zona_id)
        if zona:
            db.session.delete(zona)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_zonas():
        return Zona.query.all()