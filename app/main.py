from flask import Flask
from app import extensions, blueprints

from app.database.model import *

def create_app():
  app = Flask(__name__)
  config_opts = {
    'development': 'ConfigDev',
    'staging': 'ConfigStage',
    'production': 'ConfigProd'
  }
  config_path = 'config'
  config_env = config_opts[app.config.get('ENV')]
  app.config.from_object(f'{config_path}.{config_env}')

  extensions.init_app(app)
  blueprints.init_app(app)
  
  @app.route('/')
  @app.route('/<name>')
  def index(name='World'):
    return f'Hello {name}'

  return app