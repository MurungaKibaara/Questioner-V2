'''Register Blueprints'''
import os
from flask import Flask
from dotenv import load_dotenv
from instance.config import APP_CONFIG, TestingConfig, DevelopmentConfig
from app.api.V2.views.user_views import REGISTRATION, LOGIN
from app.api.V2.views.question_views import POSTQUESTION, GETQUESTIONS, VOTE
from app.api.V2.views.comment_views import POSTCOMMENTS, GETCOMMENTS
from app.api.V2.views.meetup_views import POSTMEETUP, GETMEETUPS
from app.api.V2.models.postgres import init_db, create_tables


def create_app(config_name):
    '''create app'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(REGISTRATION, url_prefix='/api/V2')
    app.register_blueprint(LOGIN, url_prefix='/api/V2')
    app.register_blueprint(POSTQUESTION, url_prefix='/api/V2')
    app.register_blueprint(VOTE, url_prefix='/api/V2')
    app.register_blueprint(GETQUESTIONS, url_prefix='/api/V2')
    app.register_blueprint(POSTCOMMENTS, url_prefix='/api/V2')
    app.register_blueprint(GETCOMMENTS, url_prefix='/api/V2')
    app.register_blueprint(POSTMEETUP, url_prefix='/api/V2')
    app.register_blueprint(GETMEETUPS, url_prefix='/api/V2')

    with app.app_context():
        #Questioner().connect_db(app.config["DATABASE_URL"]))
        #Questioner.connect_db(app.config["DATABASE_URL"])
        init_db()
        create_tables()

    return app


APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
DOTENV_PATH = os.path.join(APP_ROOT, '.env')
load_dotenv(DOTENV_PATH)
