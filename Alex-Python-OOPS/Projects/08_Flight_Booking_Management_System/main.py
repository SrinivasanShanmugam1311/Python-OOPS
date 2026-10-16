from services.domain_service import FlightService
from exceptions.domain_errors import DomainError
def main():
    app = FlightService()
    person = app.register_person('Alex', 'alex@example.com')
    item = app.create_resource('Demo Flight', 10)
    try:
        record = app.book_ticket(person.person_id, item.resource_id, 2)
        print('Flight Booking:', record.status, 'Remaining:', app.get_capacity(item.resource_id))
        app.cancel_ticket(record.record_id)
        print('After reversal:', record.status, 'Remaining:', app.get_capacity(item.resource_id))
    except DomainError as error:
        print('Operation failed:', error)
if __name__ == '__main__': main()
