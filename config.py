import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuração Base - Configurações comuns a todos os ambientes."""
   
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("ERRO: SECRET_KEY não definida. Use um valor aleatório e forte.")

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///dev.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    WTF_CSRF_ENABLED = True
    
    MAIL_SERVER = 'smtp.example.com'
   

class DevelopmentConfig(Config):
    """Configuração para Ambiente de Desenvolvimento."""
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///dev.sqlite3'


class TestingConfig(Config):
    """Configuração para Testes (Unitários, Integração)."""
    TESTING = True 
    DEBUG = False
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' 
    
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """Configuração para Ambiente de Produção."""
    DEBUG = False
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("ERRO: DATABASE_URL não definida para produção.")
        
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
    """Retorna a classe de configuração baseada no nome do ambiente."""
    return config_map.get(config_name, config_map['default'])
