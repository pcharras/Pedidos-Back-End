from app import db

class Zona(db.Model):
    __tablename__ = 'zonas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)

    def serialize(self):
        print(self)
        return {
            "id": self.id,
            "nombre": self.nombre
        }
    
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"<Zona {self.id}: {self.nombre}>"