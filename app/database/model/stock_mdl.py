from app.database.db import db
from app.database.mixins import UuidPrimaryKeyMixin, CreatedUpdatedTimestampMixin

class Stock(UuidPrimaryKeyMixin, CreatedUpdatedTimestampMixin, db.Model):
  name = db.Column(db.String, nullable=False)

  items = db.relationship(
    'StockItem',
    lazy=True,
    backref=db.backref('stock', lazy=False)
  )

  maintainers = db.relationship(
    'Maintainer',
    lazy=True,
    secondary='stock_maintainer',
    backref=db.backref('stocks', lazy=False)
  )