class InventoryError(Exception):
    """Common parent for warehouse errors."""
class ProductNotFoundError(InventoryError): pass
class WarehouseNotFoundError(InventoryError): pass
class InvalidQuantityError(InventoryError): pass
class InsufficientStockError(InventoryError): pass
class TransferError(InventoryError): pass
