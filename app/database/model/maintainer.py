from app.database.db import db
from app.database.mixins import UuidPrimaryKeyMixin, CreatedUpdatedTimestampMixin

class Maintainer(UuidPrimaryKeyMixin, CreatedUpdatedTimestampMixin, db.Model):
  name = db.Column(db.String, nullable=False)