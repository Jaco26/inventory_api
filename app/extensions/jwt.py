def init_app(app):
  import functools
  from flask_jwt_extended import JWTManager
  from app.database.model import RevokedJWT

  jwt = JWTManager(app)

  @jwt.token_in_blacklist_loader
  def is_jwt_revoked(decrypted_jwt):
    jti = decrypted_jwt.get('jti')
    return bool(RevokedJWT.query.get(jti))