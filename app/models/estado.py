from app import db

class Estado(db.Model):
    __tablename__ = 'estados'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)  # Nuevo campo

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "is_deleted": self.is_deleted  # Nuevo campo en la serialización
        }

    def __init__(self, nombre):
        self.nombre = nombre
        self.is_deleted = False  # Valor predeterminado

    def __repr__(self):
        return f"<Estado {self.id}: {self.nombre}, {'Eliminado' if self.is_deleted else 'No Eliminado'}>"
