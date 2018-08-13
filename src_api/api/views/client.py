from flask_restful import Resource, reqparse
from flask import request
from flask_restplus import inputs
from api.modules.user import (
    create_user, get_user, create_divice, get_divice,
    get_sensor, create_sensor
)


class UserResource(Resource):

    def get(self):
        return get_user(request.args)

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("password", required=True,
                            help="Need password field")
        parser.add_argument("email", required=True,
                            help="Need email field")
        parser.add_argument("name", required=True,
                            help="Need name field")
        args = parser.parse_args()
        data = create_user(args)
        return data


class DeviceResource(Resource):

    def get(self):
        return get_divice(request.args)

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("state",
                            required=True,
                            type=inputs.boolean,
                            help="Need state field")
        parser.add_argument("geolocation", required=True,
                            help="Need geolocation field")
        parser.add_argument("user_id", required=True,
                            help="Need user_id field")
        args = parser.parse_args()
        data = create_divice(args)
        return data


class SensorResource(Resource):

    def get(self):
        return get_sensor(request.args)

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("description", required=True,
                            help="Need description field")
        parser.add_argument("variable", required=True,
                            help="Need variable field")
        parser.add_argument("name", required=True,
                            help="Need name field")
        args = parser.parse_args()
        data = create_sensor(args)
        return data
