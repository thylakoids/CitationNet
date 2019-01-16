import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # mail config ,through localhost, not used
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@angular.com>'  # sender account
    FLASKY_ADMIN = 'admin@angular.com'  # receptor account

    DEBUG = False
    TESTING = False
    citationNet_databasename = 'citationNet.db'
    pubmed_tablename = 'pubmed'
    email = 'jwlygr98235@chacuo.net'
    logfile = 'flask.log'
    host = '127.0.0.1'
    port = '4000'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    logfile = 'flask-development.log'
    host = '127.0.0.1'


class TestingConfig(Config):
    TESTING = True
    logfile = 'flask-testing.log'
    host = '127.0.0.1'


class ProductionConfig(Config):
    host = '0.0.0.0'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
