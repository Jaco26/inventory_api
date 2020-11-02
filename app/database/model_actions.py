from .db import db

def save(model):
  db.session.add(model)
  db.session.commit()

def delete(model):
  db.session.delete(model)
  db.session.commit()

def cols_dict(model):
  '''Return a dictionary of the `column` values from the model'''
  return { column.name: getattr(model, column.name) for column in model.__table__.columns }
