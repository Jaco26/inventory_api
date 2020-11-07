from app.database.model_actions import save, delete, cols_dict
from app.database.model import Stock, Maintainer

class StockDbController:

  @classmethod
  def _package_stock(cls, stock, **kwargs):
    rv = cols_dict(stock)
    if kwargs['include_items']:
      rv['items'] = stock.items.all()
    if kwargs['include_maintainers']:
      rv['maintainers'] = stock.maintainers.all()
    return rv


  @classmethod
  def get_stocks_by_maintainer_id(cls, **kwargs):
    maintainer = Maintainer.query.get(kwargs['maintainer_id'])
    return [cls._package_stock(stock, **kwargs) for stock in maintainer.stocks]


  @classmethod
  def get_stock_by_stock_id(cls, **kwargs):
    stock = Stock.query.get(kwargs['stock_id'])
    return cls._package_stock(stock, **kwargs)


  @classmethod
  def create_stock(cls, **kwargs):
    stock = Stock(name=kwargs['stock_name'])
    save(stock)


  @classmethod
  def update_stock(cls, **kwargs):
    stock = Stock.query.get(kwargs['stock_id'])
    stock.name = kwargs.get('stock_name', stock.name)
    save(stock)


  @classmethod
  def delete_stock(cls, **kwargs):
    stock = Stock.query.get(kwargs['stock_id'])
    delete(stock)
