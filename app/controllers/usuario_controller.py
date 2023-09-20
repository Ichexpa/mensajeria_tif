from ..models.usuario_model import Usuario
from ..models.exceptions import UserNotFound, UserDataError
from flask import request, session
class UsuarioController:
    
    @classmethod
    def login(cls):
        data = request.json
        usuario = Usuario(nickname = data.get("nickname"),
                       contrasenia = data.get("contrasenia")
        )
        
        if Usuario.is_registered(usuario):
            session['nickname'] = data.get("nickname")
            return {"message":"Sesión Iniciada"},200
        
        raise UserNotFound("Usuario o contraseña incorrectos")
        
    @classmethod
    def show_usuario(cls):
        usuario_buscado = Usuario(nickname = session.get("nickname"))
        usuario_result = Usuario.get_usuario(usuario_buscado)
        if usuario_result is not None:
            return usuario_result.serialize(),200 
        raise UserDataError("Usuario no encontrado.")
    
    @classmethod
    def logout(cls):
        session.pop('nickname',None)
        return {"message":"Sesión cerrada"},200
    
    @classmethod
    def registrar_usuario(cls):
        data = request.json
        usuario = Usuario(
            email = data.get('email'),
            contrasenia = data.get('contrasenia'),
            nombre = data.get('nombre'),
            apellido = data.get('apellido'),
            fecha_nac = data.get('fecha_nac'),
            avatar = data.get('avatar'),
            nickname = data.get('nickname')
        )
        if not usuario.exists():    
            Usuario.create_usuario(usuario)
            return {"message":"Registro exitoso"},201
        return {"message":"El usuario ya existe"},400
    
    @classmethod
    def update_usuario(cls):
        data = request.json
        usuario_buscado = Usuario(nickname = session.get("nickname"))
        usuario_result = Usuario.get_usuario(usuario_buscado)
        if usuario_result is not None:
            usuario_result.email = data.get("email")
            usuario_result.contrasenia = data.get("contrasenia")
            usuario_result.nombre = data.get("nombre")
            usuario_result.apellido = data.get("apellido")
            usuario_result.fecha_nac = data.get("fecha_nac")
            usuario_result.avatar = data.get("avatar")
            usuario_result.nickname =data.get("nickname")
            Usuario.update_usuario(usuario_result)
            return {"message":"Usuario actualizado correctamente"},200
        raise UserDataError("Usuario no encontrado")
    
    @classmethod
    def delete_usuario(cls):
        usuario_buscado = Usuario(nickname = session.get("nickname"))
        usuario_result = Usuario.get_usuario(usuario_buscado)
        if usuario_result is not None:
            Usuario.delete_usuario(usuario_result)
            return {"message":"El usuario ha sido eliminadi"},200
        raise UserDataError("Usuario no encontrado")