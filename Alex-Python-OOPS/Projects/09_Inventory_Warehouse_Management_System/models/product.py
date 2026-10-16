from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class Product:
    product_id: int
    sku: str
    name: str
    unit_price: Decimal
