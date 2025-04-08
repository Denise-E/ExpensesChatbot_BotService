from flask import Blueprint, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os

SWAGGER_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'swagger'))

# Blueprint para servir el swagger.json
swagger_json_blueprint = Blueprint('swagger_json', __name__)


@swagger_json_blueprint.route('/swagger.json')
def swagger_json():
    return send_from_directory(SWAGGER_DIR, 'swagger.json')


# Configuración de Swagger UI
SWAGGER_URL = '/swagger'  # Ruta del frontend
API_URL = '/swagger.json'  # Donde lo va a ir a buscar

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Expense Tracker API"}
)
