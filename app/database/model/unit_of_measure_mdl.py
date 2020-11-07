from app.database.db import db
from app.database.mixins import SerialPrimaryKeyMixin

class UnitOfMeasure(SerialPrimaryKeyMixin, db.Model):
  name = db.Column(db.String, nullable=False, unique=True)