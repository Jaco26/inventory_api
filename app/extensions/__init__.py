def init_app(app):
  from . import db, jwt

  db.init_app(app)
  jwt.init_app(app)