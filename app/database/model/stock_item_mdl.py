from sqlalchemy.dialects.postgresql import UUID
from app.database.db import db
from app.database.mixins import UuidPrimaryKeyMixin, CreatedUpdatedTimestampMixin

class StockItem(UuidPrimaryKeyMixin, CreatedUpdatedTimestampMixin, db.Model):
  stock_id = db.Column(UUID, db.ForeignKey('stock.id'), nullable=False)
  item_id = db.Column(UUID, db.ForeignKey('item.id'), nullable=False)
  