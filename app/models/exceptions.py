from flask import jsonify

class CustomException(Exception):

    def __init__(self, status_code, name="Custom Error", description='Error'):
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code

        return response

class MensajeNotFound(CustomException):

    def __init__(self, status_code=404, name="MensajeNotFound", description='No se encontro el mensaje'):
        super().__init__(status_code, name, description)
        
class UserNotFound(CustomException):
    def __init__(self, description=''):
        status_code = 404
        name="User Found Error"
        super().__init__(status_code, name, description)
        
class UserDataError(CustomException):
    def __init__(self, description=''):
        status_code = 400
        name = "Invalid Data Error"
        super().__init__(status_code, name, description)