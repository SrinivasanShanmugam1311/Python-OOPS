import unittest
from services.domain_service import HotelService
from models.resources import StandardRoom, DeluxeRoom
from exceptions.domain_errors import (NotFoundError, InvalidAmountError,
    InsufficientCapacityError, InvalidStateError)
class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.app = HotelService()
        self.person = self.app.register_person('Alex','alex@example.com')
        self.item = self.app.create_resource('Example', 5)
    def test_registration(self): self.assertEqual(self.person.name,'Alex')
    def test_unique_ids(self):
        p = self.app.register_person('Anu','anu@example.com')
        self.assertNotEqual(self.person.person_id,p.person_id)
    def test_invalid_email(self):
        with self.assertRaises(ValueError): self.app.register_person('Alex','bad')
    def test_resource_subclasses(self):
        premium = self.app.create_resource('Premium',3,premium=True)
        self.assertIsInstance(self.item,StandardRoom)
        self.assertIsInstance(premium,DeluxeRoom)
        self.assertNotEqual(self.item.description(),premium.description())
    def test_negative_capacity(self):
        with self.assertRaises(InvalidAmountError): self.app.create_resource('Bad',-1)
    def test_action(self):
        r = self.app.reserve(self.person.person_id,self.item.resource_id,2)
        self.assertEqual(r.status,'ACTIVE')
        self.assertEqual(self.app.get_capacity(self.item.resource_id),3)
    def test_reversal(self):
        r = self.app.reserve(self.person.person_id,self.item.resource_id,2)
        self.app.checkout(r.record_id)
        self.assertEqual(self.app.get_capacity(self.item.resource_id),5)
    def test_double_reversal_rejected(self):
        r = self.app.reserve(self.person.person_id,self.item.resource_id)
        self.app.checkout(r.record_id)
        with self.assertRaises(InvalidStateError): self.app.checkout(r.record_id)
    def test_insufficient_capacity(self):
        with self.assertRaises(InsufficientCapacityError): self.app.reserve(self.person.person_id,self.item.resource_id,6)
        self.assertEqual(self.app.get_capacity(self.item.resource_id),5)
    def test_zero_units(self):
        with self.assertRaises(InvalidAmountError): self.app.reserve(self.person.person_id,self.item.resource_id,0)
    def test_missing_person(self):
        with self.assertRaises(NotFoundError): self.app.reserve(999,self.item.resource_id)
    def test_missing_resource(self):
        with self.assertRaises(NotFoundError): self.app.reserve(self.person.person_id,999)
    def test_missing_record(self):
        with self.assertRaises(NotFoundError): self.app.checkout(999)
    def test_history(self):
        self.app.reserve(self.person.person_id,self.item.resource_id,2)
        self.assertEqual(len(self.app.history(self.person.person_id)),1)
    def test_multiple_actions(self):
        self.app.reserve(self.person.person_id,self.item.resource_id,2)
        self.app.reserve(self.person.person_id,self.item.resource_id,1)
        self.assertEqual(self.app.get_capacity(self.item.resource_id),2)
if __name__ == '__main__': unittest.main()
