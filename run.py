from app import create_app, db
from app.models import Estado, Parametro
# Aquí puedes configurar el entorno o cualquier otro ajuste previo al lanzamiento
# Por ejemplo, puedes establecer variables de entorno
parametros = [
    {"nombre": "MaxPedidosPorGrupo", "valor": "5"},
    {"nombre": "MaxEsperaPorGrupo", "valor": "40"},
    {"nombre": "Ciudad", "valor": "Carlos Paz"},
    {"nombre": "EmailInformes", "valor": "oaxacaappedidos@gmail.com"},
    {"nombre": "horasInformeDiario", "valor": "20"},
    {"nombre": "ultimoInforme", "valor": ""}
]
app = create_app()

with app.app_context():
    for estado_nombre in ["Abierto", "Cerrado", "Enviado", "Cancelado", "Pendiente", "Entregado"]:
        estado_existente = Estado.query.filter_by(nombre=estado_nombre).first()
        if not estado_existente:
            nuevo_estado = Estado(nombre=estado_nombre)
            db.session.add(nuevo_estado)
            db.session.commit()        
    print('Estados cargados...')
    for parametro_data in parametros:
        parametro_existente = Parametro.query.filter_by(nombre=parametro_data["nombre"]).first()
        if not parametro_existente:
            nuevo_parametro = Parametro(nombre=parametro_data["nombre"], valor=parametro_data["valor"])
            db.session.add(nuevo_parametro)
            db.session.commit()
    print('Parámetros cargados...')

if __name__ == '__main__':
    # Aquí puedes configurar opciones adicionales para la ejecución del servidor
    # como el puerto, el modo de depuración, etc.
    app.run(debug=True,host='127.0.0.1',port=8000) # Cambia debug a False en un entorno de producción
