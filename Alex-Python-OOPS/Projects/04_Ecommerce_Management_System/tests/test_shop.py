import unittest
from decimal import Decimal
from services.shop_service import ShopService
from models.payment import UPIPayment,CardPayment
from exceptions.errors import InsufficientStockError,EmptyCartError,InvalidQuantityError,InvalidOrderStateError
class ShopTests(unittest.TestCase):
    def setUp(self):
        self.shop=ShopService()
        self.customer=self.shop.create_customer('Alex','alex@example.com')
        self.product=self.shop.add_product('Mouse','500',3)
    def test_checkout(self):
        self.shop.add_to_cart(self.customer.customer_id,self.product.product_id,2)
        order=self.shop.checkout(self.customer.customer_id,UPIPayment())
        self.assertEqual(order.total,Decimal('1000'))
        self.assertEqual(self.product.stock,1)
    def test_stock_validation(self):
        self.shop.add_to_cart(self.customer.customer_id,self.product.product_id,4)
        with self.assertRaises(InsufficientStockError): self.shop.checkout(self.customer.customer_id,UPIPayment())
        self.assertEqual(self.product.stock,3)
    def test_empty_cart(self):
        with self.assertRaises(EmptyCartError): self.shop.checkout(self.customer.customer_id,UPIPayment())
    def test_invalid_quantity(self):
        with self.assertRaises(InvalidQuantityError): self.shop.add_to_cart(self.customer.customer_id,self.product.product_id,-1)
    def test_cancel(self):
        self.shop.add_to_cart(self.customer.customer_id,self.product.product_id,1)
        order=self.shop.checkout(self.customer.customer_id,CardPayment())
        self.shop.cancel_order(order.order_id)
        self.assertEqual(self.product.stock,3)
        with self.assertRaises(InvalidOrderStateError): self.shop.cancel_order(order.order_id)
    def test_polymorphism(self):
        self.assertIn('UPI',UPIPayment().pay(Decimal('10')))
        self.assertIn('CARD',CardPayment().pay(Decimal('10')))
