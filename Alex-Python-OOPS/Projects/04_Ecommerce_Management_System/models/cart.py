from dataclasses import dataclass,field
from exceptions.errors import InvalidQuantityError
@dataclass
class Cart:
    customer_id: int
    items: dict[int,int] = field(default_factory=dict)
    def add_item(self, product_id, quantity):
        if quantity <= 0: raise InvalidQuantityError('Quantity must be positive')
        self.items[product_id] = self.items.get(product_id,0) + quantity
    def clear(self): self.items.clear()
