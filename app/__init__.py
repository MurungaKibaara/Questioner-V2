'''Register Blueprints'''
import os
from flask import Flask, jsonify
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

    with app.app_context():
        init_db()
        create_tables()

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

    @app.errorhandler(404)
    def not_found(message):
        """ not found handler"""

        return jsonify({
            "status": 404,
            "message": str(message)
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(message):
        """ method not allowed error handler"""

        return jsonify({
            "status": 405,
            "message": str(message)
        }), 405

    @app.errorhandler(500)
    def internal_server_error(message):
        """ Internal server error handler """
        return jsonify({
            "status": 500,
            "message": str(message)
        }), 500

    app.register_error_handler(404, not_found)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(500, internal_server_error)

    return app


APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
DOTENV_PATH = os.path.join(APP_ROOT, '.env')
load_dotenv(DOTENV_PATH)
