#!/usr/bin/env python3
from flask import Flask
from api.models import db
from config import DevelopmentConfig
from api.views import bp_api


def create_app(config_object=DevelopmentConfig):

    app = Flask(__name__)
    app.config.from_object(config_object)

    register_blueprints(app)
    db.init_app(app)
    db.create_all(app=app)

    return app


def register_blueprints(app):
    app.register_blueprint(bp_api, url_prefix="/api")
