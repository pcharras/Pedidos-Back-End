from app import db

class GrupoPedido(db.Model):
    __tablename__ = 'grupos_pedidos'

    id = db.Column(db.Integer, primary_key=True)
    id_zona = db.Column(db.Integer, db.ForeignKey('zonas.id'), nullable=False)
    zona = db.relationship('Zona', backref='grupos_pedidos')
    fecha_hora_creacion = db.Column(db.TIMESTAMP, nullable=False)
    fecha_hora_cierre = db.Column(db.TIMESTAMP)
    fecha_hora_envio = db.Column(db.TIMESTAMP)
    id_estado = db.Column(db.Integer, db.ForeignKey('estados.id'), nullable=False)
    estado = db.relationship('Estado', backref='grupos_pedidos')
    id_cadete = db.Column(db.Integer, db.ForeignKey('cadetes.id'), nullable=True)
    cadete = db.relationship('Cadete', backref='grupos_pedidos')
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)  # Nuevo campo

    def serialize(self):
        return {
            "id": self.id,
            "zona": {
                "id": self.zona.id,
                "nombre": self.zona.nombre
            } if self.zona else None,
            "fecha_hora_creacion": self.fecha_hora_creacion.isoformat() if self.fecha_hora_creacion else None,
            "fecha_hora_cierre": self.fecha_hora_cierre.isoformat() if self.fecha_hora_cierre else None,
            "fecha_hora_envio": self.fecha_hora_envio.isoformat() if self.fecha_hora_envio else None,
            "estado": {
                "id": self.estado.id,
                "nombre": self.estado.nombre
            } if self.estado else None,
            "cadete": {
                "id": self.cadete.id if self.cadete else None,
                "nombre": self.cadete.nombre if self.cadete else None,
                "activo": self.cadete.activo if self.cadete else None
            } if self.cadete else None,
            "is_deleted": self.is_deleted  # Nuevo campo en la serialización
        }
    
    def __init__(self, id_zona, fecha_hora_creacion, id_estado, id_cadete, fecha_hora_cierre=None, fecha_hora_envio=None):
        self.id_zona = id_zona
        self.fecha_hora_creacion = fecha_hora_creacion
        self.fecha_hora_cierre = fecha_hora_cierre
        self.fecha_hora_envio = fecha_hora_envio
        self.id_estado = id_estado
        self.id_cadete = id_cadete
        self.is_deleted = False  # Valor predeterminado

    def __repr__(self):
        return f"<GrupoPedido {self.id}: Zona {self.id_zona}, Estado {self.id_estado}, {'Eliminado' if self.is_deleted else 'No Eliminado'}>"
