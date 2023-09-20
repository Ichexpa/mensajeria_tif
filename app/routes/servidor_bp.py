from flask import Blueprint
from ..controllers.servidor_controller import ServidorController

servidor_bp=Blueprint("servidor_bp",__name__)

servidor_bp.route("/all",methods=["GET"])(ServidorController.get_servidores)
servidor_bp.route("/",methods=["POST"])(ServidorController.create_servidor)
servidor_bp.route("/<int:id_servidor>",methods=["GET"])(ServidorController.get_servidor_Xid)