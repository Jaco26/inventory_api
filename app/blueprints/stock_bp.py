from flask import Blueprint, request, jsonify
from app.database.controller import StockDbController

stock_bp = Blueprint('stock_bp', __name__)


def qs_bool(key):
  val = request.args.get(key, False)
  if val == False or val == '0' or val.lower() == 'false' or val.lower() == 'f':
    return False
  return True

@stock_bp.route('/')
def stock():
  return jsonify(request.args)
  

# @stock_bp.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
# @stock_bp.route('/<stock_id>')
# def get_all_stocks():
#   '''Get all stocks associated with the maintainer in the JWT (not implemented)'''
#   # include_items = boolean(request.args.get('include_items', False))
#   include_items = qs_bool('include_items')

#   StockDbController.create_stock()

#   return jsonify({ 'include_items': include_items })
