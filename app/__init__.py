import os
from flask import Flask, Blueprint
from flask_restful import Api, Resource

version2 = Blueprint('api', __name__, url_prefix='/api/v2')
api = Api(version2)

api.add_resource(Register, '/register')
api.add_resource( UserLogin, '/login')
