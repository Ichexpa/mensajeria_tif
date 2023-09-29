#MANEJA LOS EVENTOS DE NOTIFICACION
# Importa las bibliotecas necesarias
from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit, join_room, leave_room

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Establece una clave secreta para la aplicación
app.config['SECRET_KEY'] = 'secret!'

# Crea una instancia de SocketIO y la vincula a la aplicación Flask
socketio = SocketIO(app)

# Manejador de eventos para unirse a un servidor
@socketio.on('join_server')
def on_join_server(data):
    # Obtiene el nombre de usuario de la sesión
    username = session.get('username')
    
    # Obtiene el ID del servidor de los datos enviados por el cliente
    server_id = data['server_id']
    
    # Une al usuario a la sala del servidor
    join_room(server_id)
    
    # Emite un evento 'server_joined' a la sala del servidor para notificar a los usuarios
    emit('server_joined', {'username': username}, room=server_id)

# Manejador de eventos para salir de un servidor
@socketio.on('leave_server')
def on_leave_server(data):
    # Obtiene el nombre de usuario de la sesión
    username = session.get('username')
    
    # Obtiene el ID del servidor de los datos enviados por el cliente
    server_id = data['server_id']
    
    # Saca al usuario de la sala del servidor
    leave_room(server_id)
    
    # Emite un evento 'server_left' a la sala del servidor para notificar a los usuarios
    emit('server_left', {'username': username}, room=server_id)

# Manejador de eventos para enviar una invitación a un servidor
@socketio.on('invite_to_server')
def on_invite_to_server(data):
    # Obtiene el nombre de usuario de la sesión
    username = session.get('username')
    
    # Obtiene el ID del servidor y el destinatario de los datos enviados por el cliente
    server_id = data['server_id']
    recipient = data['recipient']
    
    # Emite un evento 'server_invitation' al destinatario con detalles de la invitación
    emit('server_invitation', {'username': username, 'server_id': server_id}, room=recipient)

# Inicia la aplicación Flask con SocketIO
if __name__ == '__main__':
    socketio.run(app)
