from app import db
import json

class Zona(db.Model):
    __tablename__ = 'zonas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    layer = db.Column(db.JSON)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "layer": json.loads(self.layer) if self.layer else None
        }
    
    def __init__(self, nombre, layer=None):
        self.nombre = nombre
        self.layer = json.dumps(layer) if layer else None

    def __repr__(self):
        return f"<Zona {self.id}: {self.nombre}>"