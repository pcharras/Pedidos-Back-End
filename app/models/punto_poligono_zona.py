from app import db

class PuntoPoligonoZona(db.Model):
    __tablename__ = 'puntos_poligono_zona'

    id = db.Column(db.Integer, primary_key=True)
    latitud = db.Column(db.Numeric(9,6), nullable=False)
    longitud = db.Column(db.Numeric(9,6), nullable=False)
    zona_id = db.Column(db.Integer, db.ForeignKey('zonas.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "latitud": str(self.latitud),
            "longitud": str(self.longitud),
            "zona_id": self.zona_id
        }
    
    def __init__(self, latitud, longitud, zona_id):
        self.latitud = latitud
        self.longitud = longitud
        self.zona_id = zona_id

    def __repr__(self):
        return f"<PuntoPoligonoZona {self.id}: Latitud={self.latitud}, Longitud={self.longitud}, Zona ID={self.zona_id}>"