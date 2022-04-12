import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    tbl_args = {"schema": "kd_o_bonde"}
    conn = {
        'driver': 'postgres',
        'username': 'postgres',
        'password': 'jrjr',
        'host': '127.0.0.1',
        'database': 'kd_o_bonde',
        'schema': 'kd_o_bonde',
        'port': '5432'
    }

    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(conn['username'], conn['password'], conn['host'],
                                                                conn['database'])


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
