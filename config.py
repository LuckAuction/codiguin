import os
from dotenv import load_dotenv


# Carrega variáveis do .env, se existir
load_dotenv()

import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_secret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config:
SECRET_KEY = os.getenv('SECRET_KEY', 'dev_secret')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = True


class DevelopmentConfig(Config):
DEBUG = True


class ProductionConfig(Config):
DEBUG = False
SESSION_COOKIE_SECURE = True
REMEMBER_COOKIE_SECURE = True