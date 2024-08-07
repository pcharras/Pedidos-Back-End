from app import db

class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    id_grupo = db.Column(db.Integer, db.ForeignKey('grupos_pedidos.id'), nullable=False)
    direccion = db.Column(db.String(500), nullable=False)
    latitud = db.Column(db.Numeric(9,6), nullable=False)
    longitud = db.Column(db.Numeric(9,6), nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey('estados.id'), nullable=False)
    cliente = db.Column(db.String(250), nullable=False)  # Ajustado de ARRAY a VARCHAR(250)
    pedido = db.Column(db.String(600), nullable=False)
    telefono = db.Column(db.String(60), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)  # Nuevo campo

    # Relaciones
    grupo = db.relationship('GrupoPedido', backref=db.backref('pedidos', lazy=True))
    estado = db.relationship('Estado', backref=db.backref('pedidos', lazy=True))

    def __init__(self, id_grupo, direccion, latitud, longitud, id_estado, cliente, pedido, telefono):
        self.id_grupo = id_grupo
        self.direccion = direccion
        self.latitud = latitud
        self.longitud = longitud
        self.id_estado = id_estado
        self.cliente = cliente  # Ahora un string simple
        self.pedido = pedido
        self.telefono = telefono
        self.is_deleted = False  # Valor predeterminado

    def serialize(self):
        return {
            "id": self.id,
            "id_grupo": self.id_grupo,
            "direccion": self.direccion,
            "latitud": str(self.latitud),
            "longitud": str(self.longitud),
            "id_estado": self.id_estado,
            "cliente": self.cliente, 
            "pedido": self.pedido,
            "telefono": self.telefono,
            "is_deleted": self.is_deleted,  # Nuevo campo en la serialización
            "grupo": self.grupo.serialize() if self.grupo else None,
            "estado": self.estado.serialize() if self.estado else None,
        }
