from sqlalchemy.dialects.postgresql import UUID
from app.database.db import db

item_tag = db.Table('item_tag',
  db.Column('item_id', UUID, db.ForeignKey('item.id'), primary_key=True),
  db.Column('tag_id', UUID, db.ForeignKey('tag.id'), primary_key=True)
)

