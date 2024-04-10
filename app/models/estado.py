from app import db

class Estado(db.Model):
    __tablename__ = 'estados'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }
    
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"<Estado {self.id}: {self.nombre}>"