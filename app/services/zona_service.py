# zona_service.py
import os
from app.models import Zona, PuntoPoligonoZona
from app import db
import requests 
from shapely.geometry import Point, Polygon
#from app.common.error_handlers import handle_invalid_usage

class ZonaService:
    @staticmethod
    def get_zona_by_id(zona_id):
        """Retrieves a zona by its ID from the database."""
        return Zona.query.get(zona_id)

    @staticmethod
    def create_zona(nombre):
        """Creates a new zona and adds it to the database."""
        new_zona = Zona(nombre=nombre)
        db.session.add(new_zona)
        db.session.commit()
        return new_zona

    @staticmethod
    def update_zona(zona_id, nombre=None):
        """Updates the name of an existing zona."""
        zona = ZonaService.get_zona_by_id(zona_id)
        if zona:
            if nombre is not None:
                zona.nombre = nombre
            db.session.commit()
            return zona
        return None

    @staticmethod
    def delete_zona(zona_id):
        """Deletes a zona from the database."""
        zona = ZonaService.get_zona_by_id(zona_id)
        if zona:
            db.session.delete(zona)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_zonas():
        """Retrieves all zonas from the database."""
        return Zona.query.all()

    @staticmethod
    def get_coordinates(address):
        """Uses the Google Maps API to convert a physical address to latitude and longitude."""
        print("entro por get_coordinates")
        api_key = os.getenv('GOOGLE_API_KEY')  
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        endpoint = f"{base_url}?address={address}&key={api_key}"
        print(endpoint)
        response = requests.get(endpoint)
        if response.status_code != 200 or 'error_message' in response.json():
            raise Exception("Error al obtener la ubicación, intenta nuevamente más tarde")
        result = response.json()['results'][0]
        return result['geometry']['location']['lat'], result['geometry']['location']['lng']

    @staticmethod
    def is_point_in_polygon(lat, lng, polygon_points):
        """Checks if a given point is inside a given polygon."""
        point = Point(lat, lng)
        polygon = Polygon(polygon_points)
        return polygon.contains(point)

    @staticmethod
    def find_zone_for_address(address=None, lat=None, lng=None):
        """Determines which zona a given address or set of coordinates falls into."""
        print("entro por find_zone_for_Address")
        if address:
            lat, lng = ZonaService.get_coordinates(address)
        if lat is None or lng is None:
            raise ValueError("Latitud y longitud no pueden ser nulas")

        zonas = ZonaService.get_all_zonas()
        print(zonas)
        for zona in zonas:
            puntos = [(pt.latitud, pt.longitud) for pt in PuntoPoligonoZona.query.filter_by(zona_id=zona.id)]
            print(puntos)
            if ZonaService.is_point_in_polygon(lat, lng, puntos):
                return zona.serialize()

        return {"error": "No se encontró una zona para la ubicación proporcionada"}

