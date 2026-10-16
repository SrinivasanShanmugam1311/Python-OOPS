import unittest
from decimal import Decimal
from services.inventory_service import InventoryService
from models.alert import ConsoleAlert, EmailAlert
from exceptions.inventory_exceptions import (InsufficientStockError, InvalidQuantityError,
    ProductNotFoundError, TransferError)
class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.s = InventoryService()
        self.p = self.s.create_product('SKU1','Mouse','500')
        self.a = self.s.create_warehouse('A')
        self.b = self.s.create_warehouse('B')
    def test_receive(self):
        self.s.receive_stock(self.a.warehouse_id,self.p.product_id,10)
        self.assertEqual(self.s.get_quantity(self.a.warehouse_id,self.p.product_id),10)
    def test_dispatch(self):
        self.s.receive_stock(1,1,10); self.s.dispatch_stock(1,1,4)
        self.assertEqual(self.s.get_quantity(1,1),6)
    def test_insufficient_stock(self):
        with self.assertRaises(InsufficientStockError): self.s.dispatch_stock(1,1,1)
        self.assertEqual(self.s.get_quantity(1,1),0)
    def test_transfer(self):
        self.s.receive_stock(1,1,10); self.s.transfer_stock(1,2,1,3)
        self.assertEqual((self.s.get_quantity(1,1),self.s.get_quantity(2,1)),(7,3))
        self.assertEqual(self.s.total_quantity(1),10)
    def test_failed_transfer_does_not_change_stock(self):
        self.s.receive_stock(1,1,2)
        with self.assertRaises(InsufficientStockError): self.s.transfer_stock(1,2,1,3)
        self.assertEqual((self.s.get_quantity(1,1),self.s.get_quantity(2,1)),(2,0))
    def test_invalid_quantity(self):
        with self.assertRaises(InvalidQuantityError): self.s.receive_stock(1,1,-1)
    def test_same_warehouse_transfer(self):
        with self.assertRaises(TransferError): self.s.transfer_stock(1,1,1,1)
    def test_unknown_product(self):
        with self.assertRaises(ProductNotFoundError): self.s.get_quantity(1,999)
    def test_inventory_value(self):
        self.s.receive_stock(1,1,3)
        self.assertEqual(self.s.inventory_value(1),Decimal('1500'))
    def test_low_stock(self):
        self.assertEqual(self.s.low_stock_report(2),[('A','Mouse',0),('B','Mouse',0)])
    def test_encapsulation_snapshot(self):
        self.s.receive_stock(1,1,5)
        snapshot=self.a.stock_snapshot(); snapshot[1]=1000
        self.assertEqual(self.a.quantity_of(1),5)
    def test_alert_polymorphism(self):
        self.assertIn('CONSOLE',ConsoleAlert().notify('Low'))
        self.assertIn('EMAIL',EmailAlert().notify('Low'))
    def test_movements(self):
        self.s.receive_stock(1,1,5); self.s.dispatch_stock(1,1,2)
        self.assertEqual([m.movement_type for m in self.s.movements],['RECEIVE','DISPATCH'])
if __name__=='__main__': unittest.main()
