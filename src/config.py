class Config(object):
    tbl_args = {"schema": "kd_o_bonde", "extend_existing": True}
    conn = {
        'driver': 'postgres',
        'username': 'postgres',
        'password': 'jrjr',
        'host': '51.79.51.190',
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
