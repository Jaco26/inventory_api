from flask import Flask
from app import extensions

from app.database.model import *

def create_app():
  app = Flask(__name__)
  app.config.from_object('config.Config')

  extensions.init_app(app)
  
  @app.route('/')
  @app.route('/<name>')
  def index(name='World'):
    return f'Hello {name}'

  return app