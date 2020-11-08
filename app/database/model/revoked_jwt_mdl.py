from sqlalchemy.dialects.postgresql import UUID
from app.database.db import db

class RevokedJWT(db.Model):
  jti = db.Column(UUID(as_uuid=True), primary_key=True)