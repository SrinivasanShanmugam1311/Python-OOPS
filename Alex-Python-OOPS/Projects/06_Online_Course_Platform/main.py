from services.domain_service import CourseService
from exceptions.domain_errors import DomainError
def main():
    app = CourseService()
    person = app.register_person('Alex', 'alex@example.com')
    item = app.create_resource('Demo Course', 10)
    try:
        record = app.enroll(person.person_id, item.resource_id, 2)
        print('Online Course Platform:', record.status, 'Remaining:', app.get_capacity(item.resource_id))
        app.unenroll(record.record_id)
        print('After reversal:', record.status, 'Remaining:', app.get_capacity(item.resource_id))
    except DomainError as error:
        print('Operation failed:', error)
if __name__ == '__main__': main()
