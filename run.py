from app import create_app, db
from app.models import Estado
# Aquí puedes configurar el entorno o cualquier otro ajuste previo al lanzamiento
# Por ejemplo, puedes establecer variables de entorno

app = create_app()

with app.app_context():
    for estado_nombre in ["Abierto", "Cerrado", "Enviado", "Cancelado", "Pendiente", "Entregado"]:
        estado_existente = Estado.query.filter_by(nombre=estado_nombre).first()
        if not estado_existente:
            nuevo_estado = Estado(nombre=estado_nombre)
            db.session.add(nuevo_estado)
            db.session.commit()
    print('Estados cargados...')

if __name__ == '__main__':
    # Aquí puedes configurar opciones adicionales para la ejecución del servidor
    # como el puerto, el modo de depuración, etc.
    app.run(debug=True,host='127.0.0.1',port=8000) # Cambia debug a False en un entorno de producción
