from flask import Blueprint
from app.database.controller import stock_ctl

stock_bp = Blueprint('stock_bp', __name__)

@stock_bp.route('/')
def get_all_stocks():
  '''Get all stocks associated with the maintainer in the JWT (not implemented)'''
  