'''Register Blueprints'''
import os
import datetime
from flask import Flask
from instance.config import APP_CONFIG
from app.api.V2.views.user_views import REGISTRATION, LOGIN
from app.api.V2.models.postgresqldatabase import create_tables

create_tables()

def create_app(config_name):
    '''create app'''
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(APP_CONFIG)
    app.config.from_pyfile('config.py')
    app.register_blueprint(REGISTRATION, url_prefix='/api/V2')
    app.register_blueprint(LOGIN, url_prefix='/api/V2')
    return app
