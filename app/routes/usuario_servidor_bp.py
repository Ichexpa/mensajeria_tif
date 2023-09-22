from ..controllers.usuario_servidor_controller import UsuarioServidorController
from flask import Blueprint

usuario_servidor_bp=Blueprint("usuario_servidor_bp",__name__)

usuario_servidor_bp.route("/",methods=["POST"])(UsuarioServidorController.ingresar_a_servidor)
usuario_servidor_bp.route("/<int:id_usuario>",methods=["GET"])(UsuarioServidorController.get_servidores_X_idUsuario)
usuario_servidor_bp.route("/<int:id_usuario_servidor>",methods=["DELETE"])(UsuarioServidorController.abandonar_servidor)