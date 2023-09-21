from ..models.usuario_servidor_model import UsuarioServidor
from ..models.usuario_model import Usuario
from ..models.servidor_model import Servidor
from flask import request

class UsuarioServidorController:

    @classmethod
    def ingresar_a_servidor(cls):
        peticion=request.json
        usuario=Usuario(id_usuario=peticion.get("id_usuario"))
        servidor=Servidor(id_servidor=peticion.get("id_servidor"))
        UsuarioServidor.ingresar_a_servidor(usuario,servidor)
        return {"message": "El usuario ingreso de forma exitosa al servidor"},201
    
    @classmethod
    def get_servidores_X_idUsuario(cls,id_usuario):
        usuario=Usuario(id_usuario=id_usuario)
        resultado = UsuarioServidor.get_servidores_X_idUsuario(usuario)
        listado_servidores=[]
        if resultado:
            for usuario_servidor in resultado:
                listado_servidores.append(usuario_servidor.serializar())
        
        return {"servidores_usuario":listado_servidores},200

    @classmethod
    def abandonar_servidor(cls, id_usuario_servidor):
        servidor_usuario= UsuarioServidor(id_usuario_servidor=id_usuario_servidor)
        if UsuarioServidor.abandonar_servidor(servidor_usuario):

            return {"message":"se abandono el servidor de forma exitosa"},204
        
        return {"message":"ocurrio un error al abandonar el servidor"},505
