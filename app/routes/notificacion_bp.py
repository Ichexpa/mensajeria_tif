from flask import Blueprint, render_template

# Crea un Blueprint llamado 'notificacion'
notificacion_bp = Blueprint('notificacion', __name__)

# Define las rutas y vistas relacionadas con notificaciones
@notificacion_bp.route('/join_server', methods=['GET'])
def join_server():
    return render_template('join_server.html')

@notificacion_bp.route('/leave_server', methods=['GET'])
def leave_server():
    return render_template('leave_server.html')

@notificacion_bp.route('/invite_to_server', methods=['GET'])
def invite_to_server():
    return render_template('invite_to_server.html')
