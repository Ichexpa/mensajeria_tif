from flask import Blueprint
from ..controllers.canal_controller import CanalController

canal_bp=Blueprint("canal_bp",__name__)

canal_bp.route("/servidor/<int:id_servidor>",methods=["GET"])(CanalController.get_canales_por_id_servidor)
canal_bp.route("/",methods=["POST"])(CanalController.create_canal)
canal_bp.route("/<int:id_canal>",methods=["DELETE"])(CanalController.delete_canal)