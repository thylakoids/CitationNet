class Config:
    DEBUG = False
    citationNet_databasename = 'citationNet.db'
    pubmed_tablename = 'pubmed'
    email = 'jwlygr98235@chacuo.net'
    logfile = 'flask.log'
    host = '0.0.0.0'


class DevelopmentConfig(Config):
    DEBUG = True
    logfile = 'flask_development.log'
    host = '127.0.0.1'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    logfile = 'flask_testing.log'
    host = '127.0.0.1'


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
