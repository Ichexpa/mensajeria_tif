from ..controllers.usuario_servidor_controller import UsuarioServidorController
from flask import Blueprint

usuario_servidor_bp=Blueprint("usuario_servidor_bp",__name__)

usuario_servidor_bp.route("/",methods=["POST"])(UsuarioServidorController.ingresar_a_servidor)
usuario_servidor_bp.route("/usuario/<int:id_usuario>",methods=["GET"])(UsuarioServidorController.get_servidores_X_idUsuario)
usuario_servidor_bp.route("/<int:id_usuario_servidor>",methods=["DELETE"])(UsuarioServidorController.abandonar_servidor)
usuario_servidor_bp.route("/<int:id_usuario_servidor>",methods=["GET"])(UsuarioServidorController.get_servidor_usuario_X_id)
usuario_servidor_bp.route("/usuario_existe",methods=["GET"])(UsuarioServidorController.usuario_ya_esta_enServidor)