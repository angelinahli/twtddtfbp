import os

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'foo')
    DEBUG = os.environ.get('FLASK_DEBUG', '') in ['True', '1', 1]
    ENVIRONMENT = os.environ.get('FLASK_ENV', 'production')

    SQLALCHEMY_DATABASE_URI = os.environ.get(
            'DATABASE_URL',
            'postgresql://localhost:5432/twtddtfbp_dev')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TWITTER_API_KEY=os.environ['TWITTER_API_KEY']
    TWITTER_API_SECRET=os.environ['TWITTER_API_SECRET']
