from flask_restful import Resource


class HomeResource(Resource):

    def get(self):
        return str("Measure ALIVE....")
