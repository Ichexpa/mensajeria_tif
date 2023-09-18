from flask import Blueprint
from ..models.exceptions import MensajeNotFound

errors=Blueprint("errors",__name__)

@errors.app_errorhandler(MensajeNotFound)
def handle_mensaje_not_found(error):
    return error.get_response()