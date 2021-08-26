# blueprints/documented_endpoints/__init__.py
from flask import Blueprint
from flask_restplus import Api
from blueprints.documented_endpoints.hello_world import namespace as hello_world_ns
from blueprints.documented_endpoints.entities import namespace as entities_ns
from blueprints.documented_endpoints.proyecto import namespace as proyecto

blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='Flask RESTplus Demo',
    version='1.0',
    description='Aplicaciones de ciencias de datos 2',
    doc='/doc'
)

#api_extension.add_namespace(hello_world_ns)
#api_extension.add_namespace(entities_ns)
api_extension.add_namespace(proyecto)
