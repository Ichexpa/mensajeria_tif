from ..database import DatabaseConnection

class Canal:

    def __init__(self,**kwargs):
        self.id_canal=kwargs.get("id_canal")
        self.nombre=kwargs.get("nombre")
        self.descripcion=kwargs.get("descripcion")
        self.id_servidor=kwargs.get("id_servidor")

    def serializar(self):
        return {"id_canal": self.id_canal,
                "nombre": self.nombre,
                "descripcion": self.descripcion,
                "id_servidor": self.id_servidor}

    @classmethod
    def get_canales_por_id_servidor(cls,servidor):
        query="SELECT * FROM mensajeria_tif.canales WHERE id_servidor=%s"
        parametros=servidor.id_servidor,
        resultados=DatabaseConnection.fetch_all(query,parametros)
        DatabaseConnection.close_connection()
        listado_canales=[]
        if resultados:
            for canal in resultados:
                listado_canales.append(Canal(id_canal=canal[0],
                                             nombre=canal[1],
                                             descripcion=canal[2],
                                             id_servidor=canal[3]                       
                                            ))
        
        return listado_canales
    
    @classmethod
    def create_canal(cls,canal):
        query="INSERT INTO mensajeria_tif.canales(nombre,descripcion,id_servidor) VALUE(%s,%s,%s)"
        parametros=(canal.nombre,canal.descripcion,canal.id_servidor)
        DatabaseConnection.execute_query(query,parametros)
        DatabaseConnection.close_connection()
        
    @classmethod
    def delete_canal(cls,canal):
        try:
            query="DELETE FROM mensajeria_tif.canales WHERE id_canal=%s"
            parametros=canal.id_canal,
            DatabaseConnection.execute_query(query,parametros)
            return True
        except Exception:
            return False
        finally:
            DatabaseConnection.close_connection()

