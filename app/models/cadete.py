from app import db

class Cadete(db.Model):
    __tablename__ = 'cadetes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    activo = db.Column(db.Boolean, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "activo": self.activo
        }
    
    def __init__(self, nombre, activo):
        self.nombre = nombre
        self.activo = activo

    def __repr__(self):
        return f"<Cadete {self.id}: {self.nombre}, {'Activo' if self.activo else 'Inactivo'}>"