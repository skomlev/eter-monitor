#!/usr/bin/env python3
from flask import Flask
from api.views import blueprints
from api.models import db
from config import DevelopmentConfig

# import os


def create_app(config_object=DevelopmentConfig):

    app = Flask(__name__)
    app.config.from_object(config_object)

    for bp in blueprints:
        app.register_blueprint(bp)

    db.init_app(app)
    db.create_all(app=app)

    return app
