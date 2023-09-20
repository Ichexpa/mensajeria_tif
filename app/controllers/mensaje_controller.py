from ..models.mensaje_model import Mensaje
from ..models.canal_model import Canal
from ..models.exceptions import MensajeNotFound

from flask import request

class MensajeController:

    
    @classmethod
    def get_mensajes_x_canal(cls,id_canal):
        canal=Canal(id_canal=id_canal)
        listado_mensajes=Mensaje.get_mensajes_x_canal(canal)
        respuesta_listado=[]
        if listado_mensajes:
            for mensaje in listado_mensajes:
                respuesta_listado.append(mensaje.serializar())
        
        return {"mensajes": respuesta_listado},200

    
    @classmethod
    def create_mensaje(cls):
        request_user=request.json
        mensaje=Mensaje(**request_user)
        Mensaje.create_mensaje(mensaje)
        return {"message":"mensaje creado exitosamente"},201
    
    @classmethod
    def delete_mensaje(cls,id_mensaje):
        mensaje=Mensaje(id_mensaje=id_mensaje)
        if(not Mensaje.exist_mensaje(mensaje)):
            raise MensajeNotFound(description=f'No se encontro el mensaje con id {mensaje.id_mensaje}')
        Mensaje.delete_mensaje(mensaje)
        return {"message":"mensaje eliminado exitosamente"},204

    @classmethod
    def update_mensaje(cls,id_mensaje):
        mensaje=Mensaje(id_mensaje=id_mensaje)
        if(not Mensaje.exist_mensaje(mensaje)):
            raise MensajeNotFound(description=f'No se encontro el mensaje con id {mensaje.id_mensaje}')
        mensaje=Mensaje(id_mensaje=id_mensaje,**request.json)
        Mensaje.update_mensaje(mensaje)
        return {"message":"mensaje actualizado correctamente"},200