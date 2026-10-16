from dataclasses import dataclass
from datetime import datetime
@dataclass(frozen=True)
class StockMovement:
    movement_id: int
    movement_type: str
    product_id: int
    quantity: int
    source_warehouse_id: int | None
    destination_warehouse_id: int | None
    timestamp: datetime
