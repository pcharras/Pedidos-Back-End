import os
import requests
from shapely.geometry import Point, Polygon
from app.models import Zona, PuntoPoligonoZona
from app import db

class ZonaService:
    @staticmethod
    def get_zona_by_id(zona_id):
        """Retrieves a zona by its ID from the database."""
        return Zona.query.get(zona_id)

    @staticmethod
    def create_zona(nombre, layer=None):
        """Creates a new zona and adds it to the database."""
        new_zona = Zona(nombre=nombre, layer=layer)
        db.session.add(new_zona)
        db.session.commit()
        return new_zona

    @staticmethod
    def update_zona(zona_id, nombre=None, layer=None):
        """Updates the name and layer of an existing zona."""
        zona = ZonaService.get_zona_by_id(zona_id)
        if zona:
            if nombre is not None:
                zona.nombre = nombre
            if layer is not None:
                zona.layer = layer
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
        api_key = os.getenv('GOOGLE_API_KEY')  
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        endpoint = f"{base_url}?address={address}&key={api_key}"
        response = requests.get(endpoint)
        if response.status_code != 200:
            raise Exception("Error al obtener la ubicación, intenta nuevamente más tarde")
        result = response.json().get('results', [])
        if not result:
            raise Exception("No se encontraron resultados para la dirección proporcionada")
        location = result[0].get('geometry', {}).get('location')
        if not location:
            raise Exception("No se pudo obtener la ubicación para la dirección proporcionada")
        return location.get('lat'), location.get('lng')

    @staticmethod
    def is_point_in_polygon(lat, lng, polygon_points):
        """Checks if a given point is inside a given polygon."""
        point = Point(lat, lng)
        polygon = Polygon(polygon_points)
        return polygon.contains(point)

    @staticmethod
    def find_zone_for_address(address=None, lat=None, lng=None, layer=None):
        """Determines which zona a given address or set of coordinates falls into."""
        if address:
            lat, lng = ZonaService.get_coordinates(address)
        if lat is None or lng is None:
            raise ValueError("Latitud y longitud no pueden ser nulas")

        zonas = ZonaService.get_all_zonas()
        for zona in zonas:
            if zona.layer != layer:
                continue
            puntos = [(pt.latitud, pt.longitud) for pt in zona.puntos]
            if ZonaService.is_point_in_polygon(lat, lng, puntos):
                return zona.serialize()

        return {"error": "No se encontró una zona para la ubicación proporcionada"}