from app.database.model_actions import save, delete, cols_dict
from app.database.model import StockItem

class StockItemDbController:

  @classmethod
  def create_item(cls, **kwargs):
    stock_item = StockItem(stock_id=kwargs['stock_id'], item_id=kwargs['item_id'])
    save(stock_item)


  @classmethod
  def update_item(cls, **kwargs):
    stock_item = StockItem.query.get(kwargs['stock_item_id'])
    stock_item.stock_id = kwargs.get('stock_id', stock_item.stock_id)
    stock_item.item_id = kwargs.get('item_id', stock_item.item_id)
    save(stock_item)


  @classmethod
  def delete_item(cls, **kwargs):
    stock_item = StockItem.query.get(kwargs['stock_item_id'])
    delete(stock_item)

