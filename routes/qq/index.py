from flask import make_response, Response
from flask_restful import Resource


class Index(Resource):
    def get(self):
        response: Response = make_response('qq index')
        response.set_cookie('zc', 'y')
        return response