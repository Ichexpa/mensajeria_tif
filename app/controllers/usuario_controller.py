from ..models.usuario_model import Usuario
from ..models.exceptions import UserNotFound,UserDataError
from flask import request, session
from config import Config
import os
class UsuarioController:
    
    @classmethod
    def login(cls):
        data = request.json
        usuario = Usuario(nickname = data.get("nickname"),
                       email = data.get("email"),
                       contrasenia = data.get("contrasenia")
        )
        usuario_registrado = Usuario.is_registered(usuario)
        if usuario_registrado is not None:
            session['nickname'] = usuario_registrado.nickname
            session['email'] = usuario_registrado.email
            session['id_usuario'] = usuario_registrado.id_usuario
            return {"message":"Sesión Iniciada"},200
        else:
            raise UserNotFound("Usuario o contraseña incorrectos")
        
    @classmethod
    def show_usuario(cls):
        usuario_buscado = Usuario(nickname = session.get("nickname"),email=session.get("email"))
        usuario_result = Usuario.get_usuario(usuario_buscado)
        if usuario_result is None:   
            raise UserDataError("Usuario no encontrado.")
        else:
            return usuario_result.serialize(),200
        
    @classmethod
    def get_usuario(cls,id_usuario):
        usuario_buscado = Usuario(id_usuario = id_usuario)
        usuario_result = Usuario.get_usuario_id(usuario_buscado)
        if usuario_result is None:   
            raise UserDataError("Usuario no encontrado.")
        else:
            return usuario_result.serialize(),200
        
    @classmethod
    def logout(cls):
        session.pop('nickname',None)
        session.pop('email',None)
        session.pop('id_usuario',None)
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
        usuario_buscado = Usuario(nickname = session.get("nickname"),email=session.get("email"))
        usuario_result = Usuario.get_usuario(usuario_buscado)
        if usuario_result is not None:
            session["nickname"] = data.get("nickname")
            usuario_result.email = data.get("email")
            usuario_result.contrasenia = data.get("contrasenia")
            usuario_result.nombre = data.get("nombre")
            usuario_result.apellido = data.get("apellido")
            usuario_result.fecha_nac = data.get("fecha_nac")
            usuario_result.avatar = data.get("avatar")
            usuario_result.nickname =data.get("nickname")
            Usuario.update_usuario(usuario_result)
            return {"message":"Usuario actualizado correctamente"},200
        raise UserDataError("No se pudo actualizar los datos del usuario")
    
    
    @classmethod
    def actualizar_avatar(cls):
        ruta_avatar_imagenes="http://127.0.0.1:5000/assets/avatares/"
        nombre_imagen=None
        usuario_sesion = Usuario(nickname = session.get("nickname"),email=session.get("email"))
        usuario = Usuario.get_usuario(usuario_sesion)
        
        if usuario is not None:
            #Compruebo que en el form se haya mandando un valor con identficador "imagen"
            if "profile_imagen" in request.files:
                #OBTENGO LA IMAGEN
                profile_imagen=request.files["profile_imagen"]
                #DESPUES MEJORAR PARA QUE SEA UNICA
                #OBTENGO EL NOMBRE
                nombre_imagen=profile_imagen.filename
                if(nombre_imagen != ""):
                    #CREO UNA RUTA TOMANDO COMO BASE LA QUE ESTA EN CONFIG UNIENDOLA CON EL NOMBRE DE LA IMAGEN ENVIADA
                    ruta_archivo = os.path.join(ruta_avatar_imagenes, nombre_imagen)
                    #GUARDO LA IMAGEN EN LA RUTA ANTERIOR
                    profile_imagen.save(ruta_archivo)
                else:
                    nombre_imagen=None
                usuario_avatar = Usuario(avatar = ruta_archivo,id_usuario = usuario.id_usuario)
                Usuario.update_usuario(usuario_avatar)
                return {"message":"imagen actualizada"},201
            else:
                raise UserDataError("La llave no se encuentra en el request")
        raise UserNotFound("usuario no encontrado")
                    
    
    @classmethod
    def delete_usuario(cls):
        usuario_buscado = Usuario(nickname = session.get("nickname"))
        usuario_result = Usuario.get_usuario(usuario_buscado)
        if usuario_result is not None:
            Usuario.delete_usuario(usuario_result)
            return {"message":"El usuario ha sido eliminadi"},200
        raise UserDataError("Usuario no encontrado")
    