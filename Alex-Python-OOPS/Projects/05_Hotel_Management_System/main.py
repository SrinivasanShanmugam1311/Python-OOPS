from services.domain_service import HotelService
from exceptions.domain_errors import DomainError
def main():
    app = HotelService()
    person = app.register_person('Alex', 'alex@example.com')
    item = app.create_resource('Demo Room', 10)
    try:
        record = app.reserve(person.person_id, item.resource_id, 2)
        print('Hotel Management:', record.status, 'Remaining:', app.get_capacity(item.resource_id))
        app.checkout(record.record_id)
        print('After reversal:', record.status, 'Remaining:', app.get_capacity(item.resource_id))
    except DomainError as error:
        print('Operation failed:', error)
if __name__ == '__main__': main()
