class ShopError(Exception): pass
class NotFoundError(ShopError): pass
class InvalidQuantityError(ShopError): pass
class InsufficientStockError(ShopError): pass
class EmptyCartError(ShopError): pass
class InvalidOrderStateError(ShopError): pass
