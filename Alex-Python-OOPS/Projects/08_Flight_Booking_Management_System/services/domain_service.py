from datetime import datetime
from models.people import Passenger
from models.resources import Flight, DomesticFlight, InternationalFlight
from models.records import Record
from exceptions.domain_errors import (NotFoundError, InvalidAmountError, InvalidStateError)
class FlightService:
    """Coordinates objects; models own the rules for their own data."""
    def __init__(self):
        self.people = {}
        self.resources = {}
        self.records = {}
        self.next_person_id = 1
        self.next_resource_id = 1
        self.next_record_id = 1
    def register_person(self, name, email):
        if not name.strip() or '@' not in email: raise ValueError('Valid name/email required')
        person = Passenger(self.next_person_id, name, email)
        self.people[person.person_id] = person
        self.next_person_id += 1
        return person
    def create_resource(self, name, capacity, premium=False):
        resource_type = InternationalFlight if premium else DomesticFlight
        item = resource_type(self.next_resource_id, name, capacity)
        self.resources[item.resource_id] = item
        self.next_resource_id += 1
        return item
    def book_ticket(self, person_id, resource_id, units=1):
        if person_id not in self.people: raise NotFoundError('Person not found')
        if resource_id not in self.resources: raise NotFoundError('Resource not found')
        # Check all requirements BEFORE modifying the resource.
        item = self.resources[resource_id]
        item.allocate(units)
        record = Record(self.next_record_id, person_id, resource_id, units, datetime.now())
        self.records[record.record_id] = record
        self.next_record_id += 1
        return record
    def cancel_ticket(self, record_id):
        record = self.records.get(record_id)
        if record is None: raise NotFoundError('Record not found')
        if record.status != 'ACTIVE': raise InvalidStateError('Record already closed')
        self.resources[record.resource_id].release(record.units)
        record.status = 'CLOSED'
        return record
    def get_capacity(self, resource_id):
        if resource_id not in self.resources: raise NotFoundError('Resource not found')
        return self.resources[resource_id].capacity
    def history(self, person_id):
        if person_id not in self.people: raise NotFoundError('Person not found')
        return [r for r in self.records.values() if r.person_id == person_id]
