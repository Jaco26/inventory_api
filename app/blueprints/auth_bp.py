from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import (
  jwt_required,
  create_access_token,
  get_raw_jwt,
  get_jwt_identity
)
from app.util.json_schema import create_schema, should_look_like
from app.util.json_schema.predicates import coerce

auth_bp = Blueprint('auth_bp', __name__)

credentials_schema = create_schema({
  'username': coerce(str)
})

@auth_bp.route('/register')
def register():
  pass
  


@auth_bp.route('/login')
def login():
  pass


@auth_bp.route('/logout')
def logout():
  pass