from flask import Blueprint
from .home import HomeResource
from .client import UserResource, DeviceResource, SensorResource
from flask_restful import Api

bp_api = Blueprint('api', __name__)

api = Api(bp_api)

api.add_resource(HomeResource, '/')
api.add_resource(UserResource, '/user/<string:email>', "/user")
api.add_resource(DeviceResource, '/device/<string:id>', "/device")
api.add_resource(SensorResource, '/sensor/<string:id>', "/sensor")
