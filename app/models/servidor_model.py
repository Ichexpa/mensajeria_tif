from ..database import DatabaseConnection

class Servidor:

    def __init__(self,**kwargs):
        self.id_servidor=kwargs.get("id_servidor")
        self.nombre=kwargs.get("nombre")
        self.descripcion=kwargs.get("descripcion")
        self.imagen=kwargs.get("imagen")
 
    def serializar(self):
        return {"id_servidor":self.id_servidor,
                "nombre":self.nombre,
                "descripcion":self.descripcion,
                "imagen":self.imagen
                }

    @classmethod
    def get_servidores(cls):
        query="SELECT * FROM mensajeria_tif.servidores"
        resultado=DatabaseConnection.fetch_all(query)
        DatabaseConnection.close_connection()
        print(resultado)
        listado_servidores=[]
        if resultado:
            for servidor in resultado:
                servidor_objeto=Servidor(id_servidor=servidor[0],
                                 nombre=servidor[1],
                                 descripcion=servidor[2],
                                 imagen=servidor[3])
                listado_servidores.append(servidor_objeto)
        return listado_servidores
    
    @classmethod
    def create_servidor(cls,servidor):
        if(servidor.imagen is None):            
            query = "INSERT INTO mensajeria_tif.servidores(nombre,descripcion) VALUE(%s,%s)"
            servidor = (servidor.nombre, servidor.descripcion)
        else:
            query = "INSERT INTO mensajeria_tif.servidores(nombre,descripcion,imagen) VALUE(%s,%s,%s)"
            servidor = (servidor.nombre, servidor.descripcion, servidor.imagen)

        cursor=DatabaseConnection.execute_query(query,servidor)
        return cursor.lastrowid
    
    @classmethod
    def get_servidor_Xid(cls,servidor):
        query="SELECT * FROM mensajeria_tif.servidores WHERE id_servidor=%s"
        servidor=servidor.id_servidor,
        resultado=DatabaseConnection.fetch_one(query,servidor)
        if resultado is not None:
            servidor=Servidor(id_servidor=resultado[0],
                            nombre=resultado[1],
                            descripcion=resultado[2],
                            imagen=resultado[3])
            return servidor
        return resultado
    
    @classmethod
    def get_servidor_Xnombre(cls,servidor):
        query="SELECT * FROM mensajeria_tif.servidores WHERE nombre LIKE %s"
        nombre_servidor="%"+servidor.nombre+"%",
        resultados=DatabaseConnection.fetch_all(query,nombre_servidor)
        listado_servidores=[]
        if resultados:
            for servidor in resultados:
                listado_servidores.append(Servidor(id_servidor=servidor[0],
                                                   nombre=servidor[1],
                                                   descripcion=servidor[2],
                                                   imagen=servidor[3]))
            return listado_servidores
        return None