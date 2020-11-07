from sqlalchemy.dialects.postgresql import UUID
from app.database.db import db
from app.database.mixins import UuidPrimaryKeyMixin, CreatedUpdatedTimestampMixin

class StockItemSnapshot(UuidPrimaryKeyMixin, CreatedUpdatedTimestampMixin, db.Model):
  '''Represents the state of an item at any given time'''
  stock_item_id = db.Column(UUID, db.ForeignKey('stock_item.id'), nullable=False)
  maintainer_id = db.Column(UUID, db.ForeignKey('maintainer.id'), nullable=False)
  unit_of_measure_id = db.Column(db.Integer, db.ForeignKey('unit_of_measure.id'), nullable=False)
  quantity = db.Column(db.Float, nullable=False, default=0.0)
