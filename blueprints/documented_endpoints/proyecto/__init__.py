# blueprints/documented_endpoints/entities/__init__.py
from flask import request
from flask_restplus import Namespace, Resource, fields
from http import HTTPStatus

namespace = Namespace('predicciones', 'Proyecto 4')

entity_model = namespace.model('Entity', {
    'id': fields.Integer(
        readonly=True,
        description='Identificador indexado'
    ),
    'score': fields.String(
        required=True,
        description='Score de la predicción'
    ),
    'fecha': fields.String(
         required=True,
         description='Fecha de la predicción'
     )
})

entity_list_model = namespace.model('EntityList', {
    'entities': fields.Nested(
        entity_model,
        description='List of entities',
        as_list=True
    ),
    'total_records': fields.Integer(
        description='Total number of entities',
    ),
})

entity_example = {'id': 1, 'name': 'Entity name'}


@namespace.route('/prediction_id/<int:prediccion_id>')
class entity(Resource):
    '''Obtener predicción por id'''

    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_with(entity_model)
    def get(self, entity_id):
        '''Obetner predicción a través de su id'''

        return entity_example

@namespace.route('/predictions_date/<string:prediccion_date>')
class entity(Resource):
	'''Obtener predicción por fecha'''
	@namespace.response(404, 'Predicción no encontrada')
	@namespace.response(500, 'Error interno')
	@namespace.marshal_with(entity_model)
	def get(self, entity_date):
		'''Obtener predicciones por fecha'''
		return entity_example
