from uuid import uuid4
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from app.database.db import db


class SerialPrimaryKeyMixin:
  id = db.Column(db.Integer, primary_key=True)


class UuidPrimaryKeyMixin:
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)


class CreatedUpdatedTimestampMixin:
  date_created = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  date_updated = db.Column(TIMESTAMP(timezone=True), onupdate=datetime.utcnow)


