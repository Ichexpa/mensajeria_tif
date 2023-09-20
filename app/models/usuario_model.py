from ..database import DatabaseConnection 
class Usuario:
    def __init__(self,**kwargs):
        self.id_usuario = kwargs.get("id_usuario")
        self.email = kwargs.get("email")
        self.contrasenia = kwargs.get("contrasenia")
        self.nombre = kwargs.get("nombre")
        self.apellido = kwargs.get("apellido")
        self.fecha_nac = kwargs.get("fecha_nac")
        self.avatar = kwargs.get("avatar")
        self.nickname = kwargs.get("nickname")
        
    def serialize(self):
        return {
            "id_usuario":self.id_usuario,
            "email":self.email,
            "contrasenia":self.contrasenia,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "fecha_nac":self.fecha_nac,
            "avatar":self.avatar,
            "nickname":self.nickname
        }
        
    def exists(self):
        query = "SELECT * FROM mensajeria_tif.usuarios WHERE email = %s;"
        params = self.email,
        result = DatabaseConnection.fetch_one(query,params=params)
        if result is not None:
            return True
        else:
            return False
    
    @classmethod
    def is_registered(cls,usuario):
        query = "SELECT * FROM mensajeria_tif.usuarios WHERE nickname = %s AND constrasenia = %s;"
        params = usuario.nickname,usuario.contrasenia,
        result = DatabaseConnection.fetch_one(query,params=params)
        if result is not None:
            return True
        else:
            return False
        
    @classmethod
    def get_usuario(cls,usuario):
        query = "SELECT * FROM mensajeria_tif.usuarios WHERE nickname = %s"
        params = usuario.nickname,
        result = DatabaseConnection.fetch_one(query,params=params)
        if result is not None:
            return Usuario(
                id_usuario = result[0],
                email = result[1],
                contrasenia = result[2],
                nombre = result[3],
                apellido = result[4],
                fecha_nac = str(result[5]),
                avatar = result[6],
                nickname = result[7]
            )
        else:
            return None
        
    @classmethod
    def create_usuario(cls,usuario):
        query = """
                INSERT INTO mensajeria_tif.usuarios
                (email,constrasenia,nombre,apellido,fecha_nac,avatar,nickname)
                VALUES(%s,%s,%s,%s,%s,%s,%s)
        """
        params = usuario.email,usuario.contrasenia,usuario.nombre,\
            usuario.apellido,usuario.fecha_nac,usuario.avatar,usuario.nickname  
            
        DatabaseConnection.execute_query(query,params=params)
        
    @classmethod
    def update_usuario(cls,usuario):
        allowed_columns = {'email', 'constrasenia', 'nombre',
                           'apellido', 'fecha_nac',
                           'avatar', 'nickname'}
        query_parts = []
        params = []
        for key, value in usuario.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(usuario.id_usuario)

        query = "UPDATE mensajeria_tif.usuarios SET " + ", ".join(query_parts) + " WHERE id_usuario = %s"
        DatabaseConnection.execute_query(query, params=params)
        
    @classmethod
    def delete_usuario(cls,usuario):
        query = "DELETE FROM mensajeria_tif.usuarios WHERE id_usuario = %s"
        params = usuario.id_usuario,
        DatabaseConnection.execute_query(query, params=params)