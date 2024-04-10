from app import db

class Parametro(db.Model):
    __tablename__ = 'parametros'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    valor = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "valor": self.valor
        }
    
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

    def __repr__(self):
        return f"<Parametro {self.id}: {self.nombre} = {self.valor}>"