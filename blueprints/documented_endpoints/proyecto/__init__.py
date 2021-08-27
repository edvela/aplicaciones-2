# blueprints/documented_endpoints/entities/__init__.py
from flask import request
from flask_restplus import Namespace, Resource, fields, Api
from http import HTTPStatus
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:5718614@127.0.0.1:54638/aplicaciones"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
namespace = Api(app)
db = SQLAlchemy(app)


class Prediccion(db.Model):
	__table_args__= {'schema' : 'aplicaciones'}
	__tablename__ = 'pred'
	id = db.Column(db.Integer, primary_key=True)
	score_from = db.Column(db.Text)
	score = db.Column(db.Text)
	fecha = db.DateTime
	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

namespace = Namespace('predicciones', 'Proyecto 4')

entity_model = namespace.model('Entity', {
    'id': fields.Integer(
        readonly=True,
        description='Identificador indexado'
    ),
    'score_from': fields.String(
	required=True,
	description='score_from'
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


@namespace.route('/prediction_id/<int:id>')
class entity(Resource):
    '''Obtener predicción por id'''
    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_with(entity_model)
    def get(self, id):
        '''Obetner predicción a través de su id'''
        match = Prediccion.query.filter_by(id=id)
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
