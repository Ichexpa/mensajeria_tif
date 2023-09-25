from flask import Blueprint

from ..controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario_bp', __name__)

usuario_bp.route('/profile', methods=['GET'])(UsuarioController.show_usuario)

usuario_bp.route('/<int:id_usuario>', methods=['GET'])(UsuarioController.get_usuario)

usuario_bp.route('/login',methods=['POST'])(UsuarioController.login)

usuario_bp.route('/logout',methods=['GET'])(UsuarioController.logout)

usuario_bp.route('/register',methods=['POST'])(UsuarioController.registrar_usuario)

usuario_bp.route('/update',methods=['PUT'])(UsuarioController.update_usuario)

usuario_bp.route('/delete',methods=['DELETE'])(UsuarioController.delete_usuario)
