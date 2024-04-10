from app.models import PuntoPoligonoZona
from app import db

class PuntoPoligonoZonaService:
    @staticmethod
    def get_punto_by_id(punto_id):
        return PuntoPoligonoZona.query.get(punto_id)

    @staticmethod
    def create_punto(latitud, longitud, zona_id):
        new_punto = PuntoPoligonoZona(latitud=latitud, longitud=longitud, zona_id=zona_id)
        db.session.add(new_punto)
        db.session.commit()
        return new_punto

    @staticmethod
    def update_punto(punto_id, latitud=None, longitud=None, zona_id=None):
        punto = PuntoPoligonoZonaService.get_punto_by_id(punto_id)
        if punto:
            if latitud is not None:
                punto.latitud = latitud
            if longitud is not None:
                punto.longitud = longitud
            if zona_id is not None:
                punto.zona_id = zona_id
            db.session.commit()
        return punto

    @staticmethod
    def delete_punto(punto_id):
        punto = PuntoPoligonoZonaService.get_punto_by_id(punto_id)
        if punto:
            db.session.delete(punto)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_puntos():
        return PuntoPoligonoZona.query.all()