from app import db

class GrupoPedido(db.Model):
    __tablename__ = 'grupos_pedidos'

    id = db.Column(db.Integer, primary_key=True)
    id_zona = db.Column(db.Integer, db.ForeignKey('zonas.id'), nullable=False)
    fecha_hora_creacion = db.Column(db.TIMESTAMP, nullable=False)
    fecha_hora_cierre = db.Column(db.TIMESTAMP)
    fecha_hora_envio = db.Column(db.TIMESTAMP)
    id_estado = db.Column(db.Integer, db.ForeignKey('estados.id'), nullable=False)
    id_cadete = db.Column(db.Integer, db.ForeignKey('cadetes.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "id_zona": self.id_zona,
            "fecha_hora_creacion": self.fecha_hora_creacion.isoformat() if self.fecha_hora_creacion else None,
            "fecha_hora_cierre": self.fecha_hora_cierre.isoformat() if self.fecha_hora_cierre else None,
            "fecha_hora_envio": self.fecha_hora_envio.isoformat() if self.fecha_hora_envio else None,
            "id_estado": self.id_estado,
            "id_cadete": self.id_cadete
        }
    
    def __init__(self, id_zona, fecha_hora_creacion, id_estado, id_cadete, fecha_hora_cierre=None, fecha_hora_envio=None):
        self.id_zona = id_zona
        self.fecha_hora_creacion = fecha_hora_creacion
        self.fecha_hora_cierre = fecha_hora_cierre
        self.fecha_hora_envio = fecha_hora_envio
        self.id_estado = id_estado
        self.id_cadete = id_cadete