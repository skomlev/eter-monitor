#!/usr/bin/env python3
from flask import Flask
from api.views import blueprints
from api.models import db
# import os


def create_app():

    app = Flask(__name__)

    app.config['MQTT_KEEPALIVE'] = 5
    app.config['MQTT_TLS_ENABLED'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/db_manager.db"

    for bp in blueprints:
        app.register_blueprint(bp)

    db.init_app(app)
    db.create_all(app=app)

    return app
