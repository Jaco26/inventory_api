from app.database.model_actions import save, delete, cols_dict
from app.database.model import (
  Stock,
  Maintainer,
  StockItem,
  stock_maintainer,
)


def get_stock_by_maintainer_id(**kwargs):
  maintainer = Maintainer.query.get(kwargs['maintainer_id'])
  if kwargs['include_items']:
    rv = []
    for stock in maintainer.stocks:
      rv.append({
        **cols_dict(stock),
        'items': stock.items.all()
      })
    return rv
  return [cols_dict(stock) for stock in maintainer.stocks]


def get_stock_by_stock_id(**kwargs):
  stock = Stock.query.get(kwargs['stock_id'])
  rv = cols_dict(stock)
  if kwargs['include_items']:
    rv['items'] = stock.items.all()
  if kwargs['include_maintainers']:
    rv['maintainers'] = stock.maintainers.all()
  return rv

def update_stock(**kwargs):
  stock = Stock.query.get(kwargs['stock_id'])
  stock.name = kwargs.get('name', stock.name)
  save(stock)

def create_stock(**kwargs):
  stock = Stock(**kwargs)
  save(stock)

def delete_stock(**kwargs):
  stock = Stock.query.get(kwargs['id'])
  delete(stock)

def add_stock_maintainer(**kwargs):
  stock = Stock.query.get(kwargs['stock_id'])
  maintainer = Maintainer.query.get(kwargs['maintainer_id'])
  stock.maintainers.append(maintainer)
  save(stock)

def add_stock_item(**kwargs):
  stock_item = StockItem(**kwargs)
  save(stock_item)

def remove_stock_maintainer(**kwargs):
  stock = Stock.query.get(kwargs['stock_id'])
  maintainer = Maintainer.query.get(kwargs['maintainer_id'])
  stock.maintainers.remove(maintainer)
  save(stock)

def remove_stock_item(**kwargs):
  stock_item = StockItem.query.get(kwargs['stock_item_id'])
  delete(stock_item)