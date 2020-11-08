from app.database.db import db
from app.database.mixins import UuidPrimaryKeyMixin, CreatedUpdatedTimestampMixin

class Account(UuidPrimaryKeyMixin, CreatedUpdatedTimestampMixin, db.Model):
  email = db.Column(db.String, nullable=False, unique=True)
  password = db.Column(db.String, nullable=False)