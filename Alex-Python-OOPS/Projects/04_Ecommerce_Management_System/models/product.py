from dataclasses import dataclass
from decimal import Decimal
from exceptions.errors import InvalidQuantityError, InsufficientStockError
@dataclass
class Product:
    product_id: int
    name: str
    price: Decimal
    stock: int
    def reserve(self, quantity):
        # Only Product changes its stock: encapsulation.
        if quantity <= 0: raise InvalidQuantityError('Quantity must be positive')
        if quantity > self.stock: raise InsufficientStockError('Not enough stock')
        self.stock -= quantity
    def restock(self, quantity):
        if quantity <= 0: raise InvalidQuantityError('Quantity must be positive')
        self.stock += quantity
