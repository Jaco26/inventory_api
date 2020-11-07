from app.database.model_actions import save
from app.database.model import StockItemSnapshot


class StockItemSnapshotDbController:

  @classmethod
  def create_snapshot(cls, **kwargs):
    snapshot = StockItemSnapshot(
      stock_item_id=kwargs['stock_item_id'],
      maintainer_id=kwargs['maintainer_id'],
      unit_of_measure_id=kwargs['unit_of_measure_id'],
      quantity=kwargs['quantity']
    )
    save(snapshot)