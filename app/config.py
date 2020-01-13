class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///helpdesk.db'
    SQLALCHEMY_TRACK_MODIFICATONS = False
    SECRET_KEY = 'secret string'
