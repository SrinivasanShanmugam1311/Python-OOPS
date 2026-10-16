from exceptions.inventory_exceptions import InvalidQuantityError, InsufficientStockError
class Warehouse:
    """One warehouse HAS-A collection of product quantities."""
    def __init__(self, warehouse_id, name):
        self.warehouse_id = warehouse_id
        self.name = name
        self.__stock = {}  # Encapsulation: callers cannot freely change stock.
    def quantity_of(self, product_id):
        return self.__stock.get(product_id, 0)
    def receive(self, product_id, quantity):
        if quantity <= 0: raise InvalidQuantityError('Quantity must be positive')
        self.__stock[product_id] = self.quantity_of(product_id) + quantity
    def dispatch(self, product_id, quantity):
        if quantity <= 0: raise InvalidQuantityError('Quantity must be positive')
        if quantity > self.quantity_of(product_id):
            raise InsufficientStockError(f'Product {product_id}: available {self.quantity_of(product_id)}, requested {quantity}')
        self.__stock[product_id] -= quantity
    def stock_snapshot(self):
        return self.__stock.copy()  # Return a copy to protect internal data.
