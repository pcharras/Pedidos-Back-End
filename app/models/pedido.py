from app import db

class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    id_grupo = db.Column(db.Integer, db.ForeignKey('grupos_pedidos.id'), nullable=False)
    direccion = db.Column(db.String(500), nullable=False)
    latitud = db.Column(db.Numeric(9,6), nullable=False)
    longitud = db.Column(db.Numeric(9,6), nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey('estados.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "id_grupo": self.id_grupo,
            "direccion": self.direccion,
            "latitud": str(self.latitud),
            "longitud": str(self.longitud),
            "id_estado": self.id_estado
        }
    
    def __init__(self, id_grupo, direccion, latitud, longitud, id_estado):
        self.id_grupo = id_grupo
        self.direccion = direccion
        self.latitud = latitud
        self.longitud = longitud
        self.id_estado = id_estado