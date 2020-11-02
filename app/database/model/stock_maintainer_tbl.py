from sqlalchemy.dialects.postgresql import UUID
from app.database.db import db

stock_maintainer = db.Table('stock_maintainer',
  db.Column('stock_id', UUID, db.ForeignKey('stock.id'), primary_key=True),
  db.Column('maintainer_id', UUID, db.ForeignKey('maintainer.id'), primary_key=True)
)

