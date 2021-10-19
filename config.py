
class DevelopmentConfig(object):
    """Base configuration."""

    # main config
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    DEBUG = True

class ProductionConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
