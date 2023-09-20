from ..models.canal_model import Canal
from ..models.servidor_model import Servidor
from flask import request
class CanalController:

    @classmethod
    def get_canales_por_id_servidor(cls,id_servidor):
        #AGREGAR CODIGO PARA..
        #comprobar que existe el servidor llamando a un metodo del controlador servidor sino lanzar excepcion
        servidor=Servidor(id_servidor=id_servidor)
        listado_canales = Canal.get_canales_por_id_servidor(servidor)
        canales=[]
        if listado_canales:
            for canal in listado_canales:
                canales.append(canal.serializar())
        
        return {"canales" : canales},200
    
    @classmethod
    def create_canal(cls):
        peticion_canal=request.json
        print(request.json)
        canal=Canal(**peticion_canal)
        Canal.create_canal(canal)
        return {"message": "canal creado correctamente"},201
    
    @classmethod
    def delete_canal(cls,id_canal):
        canal=Canal(id_canal=id_canal)
        if(Canal.delete_canal(canal)):
            return {"message": "canal eliminado correctamente"},204
        else:
            return {"message": "ocurrio un error al intentar eliminar el canal"},505
