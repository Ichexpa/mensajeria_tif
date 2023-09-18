from ..database import DatabaseConnection

class Mensaje:

    def __init__(self,**kwarg):
        print(kwarg)
        self.id_mensaje=kwarg.get("id_mensaje")
        self.contenido=kwarg.get("contenido")
        self.id_usuario=kwarg.get("id_usuario")
        self.id_canal=kwarg.get("id_canal")
        self.fecha_hora=kwarg.get("fecha_hora")

    @classmethod
    def create_mensaje(cls,mensaje):
        query="INSERT INTO mensajeria_tif.mensajes(contenido,id_usuario,id_canal,fecha_hora) VALUE(%s,%s,%s,%s)"
        mensaje_parametros=(mensaje.contenido,mensaje.id_usuario,mensaje.id_canal,mensaje.fecha_hora)
        DatabaseConnection.execute_query(query, mensaje_parametros)
        DatabaseConnection.close_connection()
    
    @classmethod
    def delete_mensaje(cls, mensaje):
        try:
            query = "DELETE FROM mensajeria_tif.mensajes WHERE id_mensaje=%s"
            mensaje_parametro = mensaje.id_mensaje,
            DatabaseConnection.execute_query(query,mensaje_parametro)
            return True
        except Exception:
            return False
        finally:
            DatabaseConnection.close_connection()

    @classmethod
    def exist_mensaje(cls,mensaje):
        query="SELECT id_mensaje FROM mensajeria_tif.mensajes WHERE id_mensaje=%s"
        mensaje_parametro=mensaje.id_mensaje,
        resultado=DatabaseConnection.fetch_one(query,mensaje_parametro)
        DatabaseConnection.close_connection()
        if(resultado is None):
            return False
        return True

    @classmethod
    def update_mensaje(cls, mensaje):
        try:
            query="UPDATE mensajeria_tif.mensajes SET contenido=%s WHERE id_mensaje=%s"
            mensaje_parametro=(mensaje.contenido,mensaje.id_mensaje)
            DatabaseConnection.execute_query(query,mensaje_parametro)
            return True
        except Exception:
            return False
        finally:
            DatabaseConnection.close_connection()


""" diccionario={"id_mensaje":23,"contenido":"testConstructor","id_canal":{"id_canal":1,"nombre":"test"}}
test = Mensaje(**diccionario)
print(test) """
