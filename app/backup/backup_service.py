import subprocess
import os
from datetime import datetime
from flask import current_app

def create_backup(app):
    with app.app_context():
        from app.services.parametro_service import ParametroService

        print("Ejecutando tarea de respaldo")

        try:
            backup_folder_param = ParametroService.get_parametro_by_nombre("Backup_Folder")
           
            if backup_folder_param is None:
                print("No se encontró ningún parámetro con el nombre 'Backup_Folder'. Usando valor predeterminado.")
                backup_folder = "C:\\"
            else:
                backup_folder = f"{backup_folder_param.valor}"
            print("Valor de backup_folder:", backup_folder)
            if not os.path.exists(backup_folder):
                print(f"La carpeta {backup_folder} no existe. Creándola...")
                os.makedirs(backup_folder)
           
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"backup_{timestamp}.sql"

            cmd = [r"C:\Program Files\PostgreSQL\15\bin\pg_dump.exe", "-U", "postgres", "-d", "PEDIDOS_DB", "-f", os.path.join(backup_folder, backup_filename)]
            
            result = subprocess.run(cmd, check=True, capture_output=True)  
            print(f"Backup creado correctamente en {os.path.join(backup_folder, backup_filename)}")
            ultimo_backup_param = ParametroService.get_parametro_by_nombre("Ultimo_Backup")
            if ultimo_backup_param is None:
                ParametroService.create_parametro("Ultimo_Backup", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            else:
                # Si existe, actualizar el valor
                ParametroService.update_parametro(ultimo_backup_param.id, valor=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            
            return True, f"Backup creado correctamente en {backup_folder}/{backup_filename}"

        except subprocess.CalledProcessError as e:
            print(f"Error al crear el backup: {e.stderr.decode()}")
            return False, f"Error al crear el backup: {e.stderr.decode()}"  # Decode error output
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            return False, f"Error inesperado: {str(e)}"
