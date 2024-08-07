from app import db

class Parametro(db.Model):
    __tablename__ = 'parametros'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    valor = db.Column(db.String(255), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)  # Nuevo campo

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "valor": self.valor,
            "is_deleted": self.is_deleted  # Nuevo campo en la serialización
        }

    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
        self.is_deleted = False  # Valor predeterminado

    def __repr__(self):
        return f"<Parametro {self.id}: {self.nombre} = {self.valor}, {'Eliminado' if self.is_deleted else 'No Eliminado'}>"
