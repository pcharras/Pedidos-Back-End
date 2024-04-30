from app.models import Cadete
from app import db

class CadeteService:
    @staticmethod
    def get_cadete_by_id(cadete_id):
        return Cadete.query.get(cadete_id)

    @staticmethod
    def create_cadete(nombre, activo, telefono=None):
        new_cadete = Cadete(nombre=nombre, activo=activo, telefono=telefono)
        db.session.add(new_cadete)
        db.session.commit()
        return new_cadete

    @staticmethod
    def update_cadete(cadete_id, nombre=None, activo=None, telefono=None):
        cadete = CadeteService.get_cadete_by_id(cadete_id)
        if cadete:
            if nombre is not None:
                cadete.nombre = nombre
            if activo is not None:
                cadete.activo = activo
            if telefono is not None:
                cadete.telefono = telefono
            db.session.commit()
        return cadete

    @staticmethod
    def delete_cadete(cadete_id):
        cadete = CadeteService.get_cadete_by_id(cadete_id)
        if cadete:
            db.session.delete(cadete)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_cadetes():
        return Cadete.query.all()