from services.domain_service import LibraryService
from exceptions.domain_errors import DomainError
def main():
    app = LibraryService()
    person = app.register_person('Alex', 'alex@example.com')
    item = app.create_resource('Demo Book', 10)
    try:
        record = app.borrow(person.person_id, item.resource_id, 2)
        print('Library Management:', record.status, 'Remaining:', app.get_capacity(item.resource_id))
        app.return_item(record.record_id)
        print('After reversal:', record.status, 'Remaining:', app.get_capacity(item.resource_id))
    except DomainError as error:
        print('Operation failed:', error)
if __name__ == '__main__': main()
