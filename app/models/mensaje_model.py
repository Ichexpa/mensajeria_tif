from ..database import DatabaseConnection
from ..models.usuario_model import Usuario

class Mensaje:

    def __init__(self,**kwarg):
        self.id_mensaje=kwarg.get("id_mensaje")
        self.contenido=kwarg.get("contenido")
        self.usuario=kwarg.get("usuario")
        self.id_canal=kwarg.get("id_canal")
        self.fecha_hora=kwarg.get("fecha_hora")

    def serializar(self):
        return {"id_mensaje":self.id_mensaje,
                "contenido":self.contenido,
                "usuario": self.usuario.serialize(),
                "id_canal":self.id_canal,
                "fecha_hora":self.fecha_hora}

    @classmethod
    def create_mensaje(cls,mensaje):
        query="INSERT INTO mensajeria_tif.mensajes(contenido,id_usuario,id_canal) VALUE(%s,%s,%s)"
        print(mensaje)
        mensaje_parametros=(mensaje.contenido,Usuario(**mensaje.usuario).id_usuario,mensaje.id_canal)
        cursor=DatabaseConnection.execute_query(query, mensaje_parametros)
        mensaje_id=cursor.lastrowid
        DatabaseConnection.close_connection()
        return mensaje_id
    
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

    @classmethod
    def get_mensajes_x_canal(cls,canal):
        query = """SELECT m.*,u.avatar,u.nickname FROM 
                mensajeria_tif.mensajes m INNER JOIN mensajeria_tif.usuarios u 
                ON m.id_usuario=u.id_usuario WHERE m.id_canal=%s"""
        parametros=canal.id_canal,
        resultados=DatabaseConnection.fetch_all(query,parametros)
        listado_mensajes=[]
        if resultados:
            for mensaje in resultados:
                listado_mensajes.append(Mensaje(id_mensaje=mensaje[0],
                                                contenido=mensaje[1],
                                                usuario=Usuario(id_usuario=mensaje[2],
                                                                avatar=mensaje[5],
                                                                nickname=mensaje[6]
                                                                ),
                                                id_canal=mensaje[3],
                                                fecha_hora=mensaje[4]))

        return listado_mensajes
    @classmethod
    def get_mensaje_x_id(cls, mensaje):
        query = """SELECT m.*,u.avatar,u.nickname FROM 
                mensajeria_tif.mensajes m INNER JOIN mensajeria_tif.usuarios u 
                ON m.id_usuario=u.id_usuario WHERE m.id_mensaje=%s"""
        mensaje_parametro = mensaje.id_mensaje,
        resultado = DatabaseConnection.fetch_one(query, mensaje_parametro)
        DatabaseConnection.close_connection()
        if (resultado is not None):
            return Mensaje(id_mensaje=resultado[0],
                           contenido=resultado[1],
                           usuario=Usuario(id_usuario=resultado[2],
                                           avatar=resultado[5],
                                           nickname=resultado[6]
                                    ),
                           id_canal=resultado[3],
                           fecha_hora=resultado[4])
        return None
""" diccionario={"id_mensaje":23,"contenido":"testConstructor","id_canal":{"id_canal":1,"nombre":"test"}}
test = Mensaje(**diccionario)
print(test) """
