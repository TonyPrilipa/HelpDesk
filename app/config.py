class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://hduser:hduser@localhost/HelpDesk'
    SQLALCHEMY_TRACK_MODIFICATONS = False
    SECRET_KEY = 'secret string'
