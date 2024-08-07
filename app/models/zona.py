from app import db
import json

class Zona(db.Model):
    __tablename__ = 'zonas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    layer = db.Column(db.JSON)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)  # Nuevo campo

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "layer": json.loads(self.layer) if self.layer else None,
            "is_deleted": self.is_deleted  # Nuevo campo en la serialización
        }

    def __init__(self, nombre, layer=None):
        self.nombre = nombre
        self.layer = json.dumps(layer) if layer else None
        self.is_deleted = False  # Valor predeterminado

    def __repr__(self):
        return f"<Zona {self.id}: {self.nombre}, {'Eliminado' if self.is_deleted else 'No Eliminado'}>"
