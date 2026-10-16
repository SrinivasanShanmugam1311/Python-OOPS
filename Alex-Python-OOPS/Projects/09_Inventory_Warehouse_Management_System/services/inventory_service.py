from datetime import datetime
from decimal import Decimal
from models.product import Product
from models.warehouse import Warehouse
from models.movement import StockMovement
from exceptions.inventory_exceptions import (ProductNotFoundError, WarehouseNotFoundError,
    InvalidQuantityError, InsufficientStockError, TransferError)
class InventoryService:
    """Coordinates products, warehouses and stock movements."""
    def __init__(self):
        self.products = {}
        self.warehouses = {}
        self.movements = []
        self.next_product_id = 1
        self.next_warehouse_id = 1
        self.next_movement_id = 1
    def create_product(self, sku, name, unit_price):
        price = Decimal(str(unit_price))
        if price < 0: raise ValueError('Price cannot be negative')
        if any(p.sku == sku for p in self.products.values()):
            raise ValueError('SKU must be unique')
        product = Product(self.next_product_id, sku, name, price)
        self.products[product.product_id] = product
        self.next_product_id += 1
        return product
    def create_warehouse(self, name):
        warehouse = Warehouse(self.next_warehouse_id, name)
        self.warehouses[warehouse.warehouse_id] = warehouse
        self.next_warehouse_id += 1
        return warehouse
    def _lookup(self, warehouse_id, product_id):
        if product_id not in self.products: raise ProductNotFoundError(product_id)
        if warehouse_id not in self.warehouses: raise WarehouseNotFoundError(warehouse_id)
        return self.warehouses[warehouse_id]
    def _record(self, kind, product_id, quantity, source, destination):
        movement = StockMovement(self.next_movement_id, kind, product_id, quantity,
                                 source, destination, datetime.now())
        self.movements.append(movement)
        self.next_movement_id += 1
        return movement
    def receive_stock(self, warehouse_id, product_id, quantity):
        warehouse = self._lookup(warehouse_id, product_id)
        warehouse.receive(product_id, quantity)
        return self._record('RECEIVE', product_id, quantity, None, warehouse_id)
    def dispatch_stock(self, warehouse_id, product_id, quantity):
        warehouse = self._lookup(warehouse_id, product_id)
        warehouse.dispatch(product_id, quantity)
        return self._record('DISPATCH', product_id, quantity, warehouse_id, None)
    def transfer_stock(self, source_id, destination_id, product_id, quantity):
        source = self._lookup(source_id, product_id)
        destination = self._lookup(destination_id, product_id)
        if source_id == destination_id: raise TransferError('Source and destination must differ')
        if quantity <= 0: raise InvalidQuantityError('Quantity must be positive')
        if source.quantity_of(product_id) < quantity:
            raise InsufficientStockError('Not enough stock for transfer')
        # Both warehouse IDs and the source stock were validated first.
        source.dispatch(product_id, quantity)
        destination.receive(product_id, quantity)
        return self._record('TRANSFER', product_id, quantity, source_id, destination_id)
    def get_quantity(self, warehouse_id, product_id):
        return self._lookup(warehouse_id, product_id).quantity_of(product_id)
    def total_quantity(self, product_id):
        if product_id not in self.products: raise ProductNotFoundError(product_id)
        return sum(w.quantity_of(product_id) for w in self.warehouses.values())
    def low_stock_report(self, threshold):
        if threshold < 0: raise InvalidQuantityError('Threshold cannot be negative')
        return [(w.name, p.name, w.quantity_of(p.product_id))
                for w in self.warehouses.values() for p in self.products.values()
                if w.quantity_of(p.product_id) <= threshold]
    def inventory_value(self, warehouse_id):
        if warehouse_id not in self.warehouses: raise WarehouseNotFoundError(warehouse_id)
        warehouse = self.warehouses[warehouse_id]
        return sum((p.unit_price * warehouse.quantity_of(p.product_id)
                    for p in self.products.values()), Decimal('0'))
