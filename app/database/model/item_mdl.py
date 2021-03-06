from app.database.db import db
from app.database.mixins import UuidPrimaryKeyMixin, CreatedUpdatedTimestampMixin

class Item(UuidPrimaryKeyMixin, CreatedUpdatedTimestampMixin, db.Model):
  name = db.Column(db.String, nullable=False)
  description = db.Column(db.String)

  tags = db.relationship(
    'Tag',
    lazy=False,
    secondary='item_tag',
    backref=db.backref('items', lazy=True)
  )

  instances = db.relationship(
    'StockItem',
    lazy=True,
    backref=db.backref('item', lazy=False)
  )
