from flask import Blueprint, request, jsonify, abort
from voluptuous.error import Error as VoluptuousError
from app.database.controller import StockDbController
from app.util.json_schema import create_schema, should_look_like
from app.util.json_schema.predicates import bool_from_str, coerce, is_uuid

stock_bp = Blueprint('stock_bp', __name__)

stock_qs_schema = create_schema({
  'include_items': bool_from_str,
  'include_maintainers': bool_from_str,
  'stock_id': is_uuid,
  'maintainer_id': is_uuid,
  'stock_name': coerce(str)
})


@stock_bp.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def stock():
  try:
    args = should_look_like(stock_qs_schema, request.args)
  except VoluptuousError as exc:
    abort(400)

  if request.method == 'GET':
    if args['stock_id']:
      return StockDbController.get_stock_by_stock_id(stock_id=args['stock_id'])
    elif args['maintainer_id']:
      return StockDbController.get_stocks_by_maintainer_id(maintainer_id=args['maintainer_id'])
    else:
      abort(400)

  elif request.method == 'POST':
    if args['stock_name']:
      StockDbController.create_stock(stock_name=args['stock_name'])
      return 'Success', 201
    else:
      abort(400)

  elif request.method == 'PUT':
    pass

  elif request.method == 'DELETE':
    pass
  


  
@stock_bp.route('/item')
def stock_item():
  return 'stock item'


@stock_bp.route('/item/snapshot')
def stock_item_snapshot():
  return 'stock item snapshot'


@stock_bp.route('/maintainer')
def stock_maintainer():
  return 'stock maintainer'