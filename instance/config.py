'''App Configurations'''
import os

class Config(object):
    """Main Configurations"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = '\xd8$\x12\xe2@\xf5\x04' #Generated using os.urandom(24)


class DevelopmentConfig(Config):
    """Development Configurations"""
    DEBUG = True
    DATABASE_NAME = "questionerversion2"
    DATABASE_URL = os.getenv("DATABASE")


class TestingConfig(Config):
    """Testing Configurations"""
    TESTING = True
    DEBUG = True
    DATABASE_NAME = "test_questioner"
    DATABASE_URL = os.getenv("TEST_DATABASE")


class ProductionConfig(Config):
    """Production Configurations"""
    DEBUG = False
    TESTING = False


APP_CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
