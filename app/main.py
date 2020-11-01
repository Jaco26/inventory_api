from flask import Flask
from app import extensions


def create_app(config=None):
  app = Flask(__name__)
  
  if config:
    app.config.from_object(config)

  extensions.init_app(app)
  
  @app.route('/')
  @app.route('/<name>')
  def index(name='World'):
    return 'Hello {}!'.format(name)

  return app