from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.usuario_bp import usuario_bp
from .routes.mensaje_bp import mensaje_bp
from .routes.servidor_bp import servidor_bp
from .routes.canal_bp import canal_bp
from .routes.usuario_servidor_bp import usuario_servidor_bp
from .routes.error_handlers import errors

from .database import DatabaseConnection

import os

def init_app():
    """Crea y configura la aplicación Flask"""

    app = Flask(__name__, static_folder=Config.STATIC_FOLDER,
                template_folder=Config.TEMPLATE_FOLDER)

    CORS(app, supports_credentials=True)
    app.config.from_object(Config)

    crear_ruta(app.config["SERVIDOR_IMAGENES"])

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(usuario_bp, url_prefix = '/usuario')
    app.register_blueprint(mensaje_bp, url_prefix='/mensaje')
    app.register_blueprint(servidor_bp,url_prefix='/servidor')
    app.register_blueprint(canal_bp,url_prefix='/canal')
    app.register_blueprint(usuario_servidor_bp,url_prefix="/usuario_servidor")
    app.register_blueprint(errors)

    return app

def crear_ruta(directorio):
    if not os.path.exists(directorio):
        os.makedirs(directorio) 