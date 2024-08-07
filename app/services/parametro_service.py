from app.models import Parametro
from app import db
from app.backup.backup_scheduler import schedule_backup

class ParametroService:
    @staticmethod
    def get_parametro_by_id(parametro_id):
        return Parametro.query.filter_by(id=parametro_id, is_deleted=False).first()
    
    @staticmethod
    def get_parametro_by_nombre(nombre):
        return Parametro.query.filter_by(nombre=nombre, is_deleted=False).first()

    @staticmethod
    def create_parametro(nombre, valor):
        new_parametro = Parametro(nombre=nombre, valor=valor)
        db.session.add(new_parametro)
        db.session.commit()
        return new_parametro

    @staticmethod
    def update_parametro(parametro_id, nombre=None, valor=None):
        parametro = ParametroService.get_parametro_by_id(parametro_id)
        if parametro:
            if nombre is not None:
                parametro.nombre = nombre
            if valor is not None:
                parametro.valor = valor
            db.session.commit()

            # Verificar si el parámetro actualizado es Hora_Backup y, si lo es, actualizar la programación
            if parametro.nombre == "Hora_Backup":
                schedule_backup()

        return parametro

    @staticmethod
    def delete_parametro(parametro_id):
        parametro = ParametroService.get_parametro_by_id(parametro_id)
        if parametro:
            parametro.is_deleted = True  # Borrado lógico
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_parametros():
        return Parametro.query.filter_by(is_deleted=False).all()
