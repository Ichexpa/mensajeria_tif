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
        id_usuario_servidor=UsuarioServidor.ingresar_a_servidor(usuario,servidor)
        return {"message": "El usuario ingreso de forma exitosa al servidor",
                "usuario_servidor":{
                    "id_usuario_servidor": id_usuario_servidor
                }}, 201
    
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

    @classmethod
    def get_servidor_usuario_X_id(cls,id_usuario_servidor):
        usuario_servidor=UsuarioServidor(id_usuario_servidor=id_usuario_servidor)
        resultado=UsuarioServidor.get_servidor_usuario_X_id(usuario_servidor)
        if resultado is not None:
            return resultado.serializar(),200
        return {"error":"No se encontro el usuario"},404
"""     @classmethod
    def crear_ingresar_y_
    #CREO PRIMERO EL SERVIDOR Y DEVUEVLO EL ID CREADO
    #CON ESE ID INGRESO AL SERVIDOR TOMANDO COMO REFERENCIA EL ID DEL SERVIDOR Y DEL USUARIO
    #UNA VEZ CREADO DEVUELVO EN UN JSON UN OBJETO DE TIPO USUARIO_SERVIDOR SERIALIZADO """