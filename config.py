import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    WTF_CSRF_ENABLED = True 
    
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')


class DevelopmentConfig(Config):
    DEBUG = True
    
    if not os.environ.get('SECRET_KEY'):
        SECRET_KEY = 'dev_secret_inseguro_mas_ok_para_dev'
        
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///dev.sqlite3'


class TestingConfig(Config):
    TESTING = True 
    DEBUG = False
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  
    
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):

    DEBUG = False
    
    if not os.environ.get('SECRET_KEY'):
        raise ValueError("ERRO CRÍTICO: SECRET_KEY não definida no ambiente de produção.")
    
    if not os.environ.get('DATABASE_URL'):
        raise ValueError("ERRO CRÍTICO: DATABASE_URL não definida para produção.")
        
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    

config_map = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig 
}

def get_config(config_name):

    return config_map.get(config_name, config_map['default'])
