import os
import random
import string
from datetime import timedelta
import dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY') or ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=(random.randint(64,128))))
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    FLASK_ENV = os.getenv('FLASK_ENV')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = os.getenv('ENV') or 'development'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DATABASE_URI') or 'sqlite:///'+basedir+'dev-db.sqlite'
    PORT = 8080

class TestingConfig(Config):
    ENV = os.getenv('ENV') or 'development'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DATABASE_URI') or 'sqlite:///'+basedir+'test-db.sqlite'
    DEBUG = True
    PORT = 8081

class ProductionConfig(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DATABASE_URI')
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    PORT = 443



config = {
    'production': ProductionConfig,
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}