from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# from flask_migrate import Migrate



# Instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Crear una instancia de Flask
    app = Flask(__name__)
    print("creo la app")
    # Configuración de la aplicación
    app.config.from_object('config.Config')
    
    # # Inicializar SQLAlchemy con la aplicación Flask
    db.init_app(app)
    
    # Inicializar Flask-Migrate con la aplicación Flask y la instancia de SQLAlchemy
    # migrate = Migrate(app, db)
    
    # # Habilitar CORS si es necesario
    CORS(app, resources={r"*": {"origins": "*"}})

    # # Importar e inicializar las rutas de la API
    from app.api.zona_api import zona_api_blueprint
    app.register_blueprint(zona_api_blueprint, url_prefix='/api')

    from app.api.punto_poligono_zona_api import punto_poligono_zona_api_blueprint
    app.register_blueprint(punto_poligono_zona_api_blueprint,url_prefix='/api')

    from app.api.cadete_api import cadete_api_blueprint
    app.register_blueprint(cadete_api_blueprint,url_prefix='/api')

    from app.api.estado_api import estado_api_blueprint
    app.register_blueprint(estado_api_blueprint,url_prefix='/api')

    from app.api.grupo_pedido_api import grupo_pedido_api_blueprint
    app.register_blueprint(grupo_pedido_api_blueprint,url_prefix='/api')

    from app.api.parametro_api import parametro_api_blueprint
    app.register_blueprint(parametro_api_blueprint,url_prefix='/api')
    
    from app.api.pedido_api import pedido_api_blueprint
    app.register_blueprint(pedido_api_blueprint,url_prefix='/api')
    
    from app.api.email_api import email_api_blueprint
    app.register_blueprint(email_api_blueprint, url_prefix='/api') 

    from app.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    # # Importar e inicializar los manejadores de errores
    #from app.common import error_handlers
    #error_handlers.init_app(app)
    with app.app_context():
        # db.drop_all()
        db.create_all()

    return app
