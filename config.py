from distutils.debug import DEBUG
import os

class Config:
    '''
    Default Configs
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
    '''
    Development Configs
    '''

    DEBUG=True

class ProdConfig(Config):
    '''
    Production Configs
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
