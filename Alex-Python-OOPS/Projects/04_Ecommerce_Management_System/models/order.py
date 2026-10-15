from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime
@dataclass(frozen=True)
class OrderLine:
    product_id: int
    name: str
    quantity: int
    unit_price: Decimal
@dataclass
class Order:
    order_id: int
    customer_id: int
    lines: list[OrderLine]
    total: Decimal
    payment_reference: str
    created_at: datetime
    status: str = 'PAID'
