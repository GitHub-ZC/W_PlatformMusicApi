from flask import Blueprint
from flask_cors import CORS
from flask_restful import Api

from routes.migu.index import Index

blue_migu = Blueprint('blue_migu', __name__, url_prefix='/migu')
api = Api(blue_migu)
CORS(blue_migu)

api.add_resource(Index, '/')
