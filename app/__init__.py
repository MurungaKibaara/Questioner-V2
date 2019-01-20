'''Register Blueprints'''
import os
from flask import Flask
from instance.config import APP_CONFIG
from app.api.V2.views.user_views import REGISTRATION, LOGIN
from app.api.V2.views.question_views import POSTQUESTION, GETQUESTIONS
from app.api.V2.views.comment_views import POSTCOMMENTS, GETCOMMENTS
from app.api.V2.views.meetup_views import POSTMEETUP, GETMEETUPS
from app.api.V2.models.postgresqldatabase import create_tables

create_tables()

def create_app(config_name):
    '''create app'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG)
    app.config.from_pyfile('config.py')
    app.register_blueprint(REGISTRATION, url_prefix='/api/V2')
    app.register_blueprint(LOGIN, url_prefix='/api/V2')
    app.register_blueprint(POSTQUESTION, url_prefix='/api/V2')
    app.register_blueprint(GETQUESTIONS, url_prefix='/api/V2')
    app.register_blueprint(POSTCOMMENTS, url_prefix='/api/V2')
    app.register_blueprint(GETCOMMENTS, url_prefix='/api/V2')
    app.register_blueprint(POSTMEETUP, url_prefix='/api/V2')
    app.register_blueprint(GETMEETUPS, url_prefix='/api/V2')
    return app
