from app.database.model_actions import save, delete
from app.database.model import Stock, Maintainer

class StockMaintainerDbController:

  @classmethod
  def add_stock_maintainer(cls, **kwargs):
    stock = Stock.query.get(kwargs['stock_id'])
    maintainer = Maintainer.query.get(kwargs['maintainer_id'])
    stock.maintainers.append(maintainer)
    save(stock)


  @classmethod
  def remove_stock_maintainer(cls, **kwargs):
    stock = Stock.query.get(kwargs['stock_id'])
    maintainer = Maintainer.query.get(kwargs['maintainer_id'])
    stock.maintainers.remove(maintainer)
    save(stock)