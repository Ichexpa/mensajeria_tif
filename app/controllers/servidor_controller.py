from ..models.servidor_model import Servidor
from flask import request
from config import Config
import os

class ServidorController:

    @classmethod
    def get_servidores(cls):
        listado_servidores=Servidor.get_servidores();
        respuesta={"servidores":[]}
        if listado_servidores:
            for servidor in listado_servidores:
                respuesta["servidores"].append(servidor.serializar())
        return respuesta,200
    

    
    @classmethod
    def create_servidor(cls):
        ruta_servidor_imagenes=Config.SERVIDOR_IMAGENES
        nombre_imagen=None
        #Compruebo que en el form se haya mandando un valor con identficador "imagen"
        if "imagen" in request.files:
            #OBTENGO LA IMAGEN
            imagen=request.files["imagen"]
            #DESPUES MEJORAR PARA QUE SEA UNICA
            #OBTENGO EL NOMBRE
            nombre_imagen=imagen.filename
            if(nombre_imagen != ""):
                #CREO UNA RUTA TOMANDO COMO BASE LA QUE ESTA EN CONFIG UNIENDOLA CON EL NOMBRE DE LA IMAGEN ENVIADA
                ruta_archivo = os.path.join(ruta_servidor_imagenes, nombre_imagen)
                #GUARDO LA IMAGEN EN LA RUTA ANTERIOR
                imagen.save(ruta_archivo)
            else:
                nombre_imagen=None
        servidor=Servidor(nombre=request.form.get("nombre"),
                          descripcion=request.form.get("descripcion"),
                          imagen=nombre_imagen)
        print(servidor.imagen)
        Servidor.create_servidor(servidor)
        return {"message":"servidor creado correctamente"},201
    
    @classmethod
    def get_servidor_Xid(cls,id_servidor):
        resultado=Servidor.get_servidor_Xid(Servidor(id_servidor=id_servidor))
        if(resultado is None):
            #DESPUES IMPLEMENTAR EL ERROR
            return {"mensaje":"No se encontro el servidor"},404
        return  resultado.serializar(),200