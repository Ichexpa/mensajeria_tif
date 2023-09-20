from flask import Blueprint
from ..controllers.mensaje_controller import MensajeController

mensaje_bp=Blueprint("mensaje_bp",__name__)

mensaje_bp.route("/",methods=["POST"])(MensajeController.create_mensaje)
mensaje_bp.route("/<int:id_mensaje>",methods=["DELETE"])(MensajeController.delete_mensaje)
mensaje_bp.route("/<int:id_mensaje>",methods=["PUT"])(MensajeController.update_mensaje)
mensaje_bp.route("/canal/<int:id_canal>",methods=["GET"])(MensajeController.get_mensajes_x_canal)