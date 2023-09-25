from ..database import DatabaseConnection
from ..models.usuario_model import Usuario 
from ..models.servidor_model import Servidor
class UsuarioServidor:

    def __init__(self,**kwargs):
        self.id_usuario_servidor=kwargs.get("id_usuario_servidor")
        self.servidor=kwargs.get("servidor")
        self.id_usuario=kwargs.get("id_usuario")

    def serializar(self):
        return {"id_usuario_servidor": self.id_usuario_servidor,
                "servidor": self.servidor.serializar()
                }
    
    @classmethod
    def ingresar_a_servidor(cls,usuario,servidor):
        query = "INSERT INTO mensajeria_tif.usuarios_servidores(id_servidor,id_usuario) VALUE(%s,%s)"
        usuario_servidor = (servidor.id_servidor, usuario.id_usuario)
        cursor=DatabaseConnection.execute_query(query,usuario_servidor)
        id_servidor_ingresado=cursor.lastrowid
        DatabaseConnection.close_connection()
        return id_servidor_ingresado

    @classmethod
    def get_servidores_X_idUsuario(cls,usuario):
        query = """SELECT us.id_usuario_servidor,us.id_servidor,s.nombre,s.descripcion,s.imagen
                   FROM mensajeria_tif.usuarios_servidores us INNER JOIN mensajeria_tif.servidores
                   s ON us.id_servidor=s.id_servidor WHERE id_usuario=%s"""
        usuario=usuario.id_usuario,
        resultado=DatabaseConnection.fetch_all(query,usuario)
        DatabaseConnection.close_connection()
        listado_servidores=[]
        if resultado:
            for servidor in resultado:
                listado_servidores.append(UsuarioServidor(id_usuario_servidor=servidor[0],
                                                          servidor=Servidor(id_servidor=servidor[1],
                                                                            nombre=servidor[2],
                                                                            descripcion=servidor[3],
                                                                            imagen=servidor[4]
                                                                            )
                                                          ))
        return listado_servidores
    
    @classmethod
    def abandonar_servidor(cls,usuario_servidor):
        try:
            query="DELETE FROM mensajeria_tif.usuarios_servidores WHERE id_usuario_servidor=%s"
            parametros = usuario_servidor.id_usuario_servidor,
            DatabaseConnection.execute_query(query,parametros)
            return True
        except Exception:
            return False
        finally:
            DatabaseConnection.close_connection()
    
    @classmethod
    def get_servidor_usuario_X_id(cls, usuario_servidor):
        query = """SELECT us.id_usuario_servidor, us.id_servidor, s.nombre, s.descripcion, s.imagen
                   FROM mensajeria_tif.usuarios_servidores us INNER JOIN mensajeria_tif.servidores
                   s ON us.id_servidor = s.id_servidor WHERE us.id_usuario_servidor = %s """
        parametros = usuario_servidor.id_usuario_servidor,
        resultado=DatabaseConnection.fetch_one(query,parametros)
        if resultado is not None:
            return UsuarioServidor(id_usuario_servidor=resultado[0],
                                   servidor=Servidor(id_servidor=resultado[1],
                                                     nombre=resultado[2],
                                                     descripcion=resultado[3],
                                                     imagen=resultado[4]
                                                     )
                                                    )
        return None