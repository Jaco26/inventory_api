def init_app(app):
  from . import db

  db.init_app(app)