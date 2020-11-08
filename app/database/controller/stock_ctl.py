from app.database.model_actions import save, delete, cols_dict
from app.database.model import Stock, Maintainer

class StockDbController:

  @classmethod
  def _package_stock(cls, stock, **kwargs):
    rv = cols_dict(stock)
    if kwargs['include_items']:
      rv['items'] = stock.items
    if kwargs['include_maintainers']:
      rv['maintainers'] = stock.maintainers
    return rv


  @classmethod
  def get_stocks_by_maintainer_id(cls, **kwargs):
    '''Get a list of `Stock` records associated with a given maintainer.
    
    kwargs:
      maintainer_id: str - The maintainer id.
    '''
    maintainer = Maintainer.query.get(kwargs['maintainer_id'])
    return [cls._package_stock(stock, **kwargs) for stock in maintainer.stocks]


  @classmethod
  def get_stock_by_stock_id(cls, **kwargs):
    '''Get the `Stock` record associated with a given stock id.

    kwargs:
      stock_id: str - The stock id.
    '''
    stock = Stock.query.get(kwargs['stock_id'])
    return cls._package_stock(stock, **kwargs)


  @classmethod
  def create_stock(cls, **kwargs):
    '''Create a new `Stock` record
    
    kwargs:
      stock_name: str - The name of the stock.
    '''
    stock = Stock(name=kwargs['stock_name'])
    save(stock)


  @classmethod
  def update_stock(cls, **kwargs):
    '''Update a `Stock` record associated with a given stock id.
    
    kwargs:
      stock_id: str - The id of the stock record to update.
      stock_name: str (optional) - The name of the stock.
    
    Discussion:
      If any optional kwarg is not provided, that column value will remain unchanged 
    '''
    stock = Stock.query.get(kwargs['stock_id'])
    stock.name = kwargs.get('stock_name', stock.name)
    save(stock)


  @classmethod
  def delete_stock(cls, **kwargs):
    '''Delete a `Stock` record associated with a given stock id
    
    kwargs:
      stock_id: str - The id of the stock record to delete
    '''
    stock = Stock.query.get(kwargs['stock_id'])
    delete(stock)
