
from .zona_api import zona_api_blueprint
from .punto_poligono_zona_api import punto_poligono_zona_api_blueprint
from .cadete_api import cadete_api_blueprint
from .estado_api import estado_api_blueprint
from .grupo_pedido_api import grupo_pedido_api_blueprint
from .pedido_api import pedido_api_blueprint
from .parametro_api import parametro_api_blueprint
from .email_api import email_api_blueprint

def init_api(app):
    app.register_blueprint(zona_api_blueprint, url_prefix='/api')
