from services.domain_service import PayrollService
from exceptions.domain_errors import DomainError
def main():
    app = PayrollService()
    person = app.register_person('Alex', 'alex@example.com')
    item = app.create_resource('Demo Period', 10)
    try:
        record = app.process_payroll(person.person_id, item.resource_id, 2)
        print('Employee Payroll:', record.status, 'Remaining:', app.get_capacity(item.resource_id))
        app.reverse_payroll(record.record_id)
        print('After reversal:', record.status, 'Remaining:', app.get_capacity(item.resource_id))
    except DomainError as error:
        print('Operation failed:', error)
if __name__ == '__main__': main()
