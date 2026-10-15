# Project 02 – Hospital Management System

## Level

**Intermediate → Advanced**

## Domain

**Hospital / Healthcare Management**

---

## 1. Project Overview

The **Hospital Management System** is a Python-based application designed to manage common hospital operations.

The project demonstrates how Python OOP concepts can be combined with a practical multi-module application.

The system manages:

* Patients
* Doctors
* Departments
* Appointments
* Medical Records
* Hospital Bills
* Payments
* Custom Exceptions
* Business Services

The project is intentionally built using a **clean and simple architecture** without unnecessary directories.

---

# 2. Project Objectives

This project demonstrates:

* Python Object-Oriented Programming
* Classes and Objects
* Inheritance
* Composition
* Association
* Encapsulation
* Dataclasses
* Service Layer
* Custom Exceptions
* Exception Hierarchy
* Type-oriented design
* Modular Python packages
* Separation of responsibilities
* Menu-driven application
* Basic unit testing
* Clean project organization

---

# 3. Project Folder Structure

```text
02_Hospital_Management_System/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── patient.py
│   ├── doctor.py
│   ├── department.py
│   ├── appointment.py
│   ├── medical_record.py
│   └── bill.py
│
├── services/
│   ├── __init__.py
│   ├── patient_service.py
│   ├── doctor_service.py
│   ├── appointment_service.py
│   └── billing_service.py
│
├── exceptions/
│   ├── __init__.py
│   └── hospital_exceptions.py
│
├── tests/
│   ├── test_patient.py
│   ├── test_doctor.py
│   └── test_appointment.py
│
├── requirements.txt
└── README.md
```

---

# 4. Architecture

The project follows a simple layered architecture.

```text
                    main.py
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       Services      Models      Exceptions
          │            │
          │            │
          ▼            ▼
    Business Logic   Data Objects
```

## Main Layers

### Models

Represent hospital entities.

```text
Person
Patient
Doctor
Department
Appointment
MedicalRecord
Bill
```

### Services

Contain business operations.

```text
PatientService
DoctorService
AppointmentService
BillingService
```

### Exceptions

Contain application-specific errors.

```text
HospitalError
PatientNotFoundError
DoctorNotFoundError
DepartmentNotFoundError
AppointmentNotFoundError
BillNotFoundError
InvalidAmountError
InvalidAppointmentError
```

### Main

`main.py` provides:

* Menu
* User input
* Service calls
* Error handling
* Application entry point

---

# 5. Domain Model

The main relationships are:

```text
Person
│
├── Patient
│    ├── Appointments
│    ├── Medical Records
│    └── Bills
│
└── Doctor
     └── Appointments

Department
└── Doctors

Patient ───── Appointment ───── Doctor
```

---

# 6. Person

`Person` is the base class.

It contains common information shared by patients and doctors.

```python
class Person:

    def __init__(self, person_id, name, age, phone):

        self.person_id = person_id
        self.name = name
        self.age = age
        self.phone = phone
```

Common information:

* ID
* Name
* Age
* Phone

---

# 7. Inheritance

`Patient` and `Doctor` inherit from `Person`.

```text
             Person
              /  \
             /    \
            /      \
       Patient     Doctor
```

Example:

```python
class Patient(Person):

    def __init__(
        self,
        patient_id,
        name,
        age,
        phone,
        blood_group
    ):

        super().__init__(
            patient_id,
            name,
            age,
            phone
        )

        self.blood_group = blood_group
```

This demonstrates:

* Inheritance
* Code reuse
* `super()`
* Base class design

---

# 8. Patient

A patient contains:

```text
Patient
│
├── ID
├── Name
├── Age
├── Phone
├── Blood Group
├── Appointments
├── Medical Records
└── Bills
```

Example:

```python
patient = Patient(
    patient_id=1,
    name="Alex",
    age=45,
    phone="9876543210",
    blood_group="O+"
)
```

---

# 9. Doctor

A doctor contains:

```text
Doctor
│
├── ID
├── Name
├── Age
├── Phone
├── Specialization
└── Appointments
```

Example:

```python
doctor = Doctor(
    doctor_id=1,
    name="Dr. Ravi",
    age=45,
    phone="9999999999",
    specialization="Cardiology"
)
```

---

# 10. Department

A department groups doctors.

Examples:

```text
Cardiology
Neurology
Orthopedics
Pediatrics
General Medicine
```

Example:

```python
department = Department(
    department_id=1,
    name="Cardiology"
)

department.add_doctor(doctor)
```

Relationship:

```text
Department
    │
    ├── Doctor
    ├── Doctor
    └── Doctor
```

---

# 11. Appointment

An appointment connects a patient and doctor.

```python
from dataclasses import dataclass


@dataclass
class Appointment:

    appointment_id: int
    patient_id: int
    doctor_id: int
    date: str
    time: str
    status: str = "Scheduled"
```

Possible statuses:

```text
Scheduled
Cancelled
Completed
```

Operations:

```python
appointment.cancel()
```

```python
appointment.complete()
```

---

# 12. Medical Record

A medical record stores information about a patient's treatment.

```python
from dataclasses import dataclass


@dataclass
class MedicalRecord:

    record_id: int
    patient_id: int
    doctor_id: int
    diagnosis: str
    treatment: str
    date: str
```

Example:

```text
Diagnosis : Fever
Treatment : Medication
Date      : 2026-08-08
```

---

# 13. Bill

A bill represents a hospital charge.

```python
from dataclasses import dataclass


@dataclass
class Bill:

    bill_id: int
    patient_id: int
    amount: float
    description: str
    status: str = "Pending"
```

Payment:

```python
bill.pay()
```

Status changes:

```text
Pending
   ↓
Paid
```

---

# 14. Patient Service

`PatientService` manages patient-related operations.

Main responsibilities:

```text
register_patient()
find_patient()
add_medical_record()
get_medical_records()
create_bill()
get_patient_bills()
display_patient()
display_patients()
```

Example:

```python
patient_service = PatientService()

patient = patient_service.register_patient(
    "Alex",
    45,
    "9876543210",
    "O+"
)
```

---

# 15. Doctor Service

`DoctorService` manages doctors and departments.

Responsibilities:

```text
register_doctor()
find_doctor()
create_department()
find_department()
assign_doctor_to_department()
get_doctors_by_department()
display_doctor()
display_doctors()
display_department()
display_departments()
```

Example:

```python
doctor = doctor_service.register_doctor(
    "Dr. Ravi",
    45,
    "9999999999",
    "Cardiology"
)
```

Create department:

```python
department = doctor_service.create_department(
    "Cardiology"
)
```

Assign doctor:

```python
doctor_service.assign_doctor_to_department(
    doctor.doctor_id,
    department.department_id
)
```

---

# 16. Appointment Service

`AppointmentService` manages appointments.

Responsibilities:

```text
create_appointment()
find_appointment()
cancel_appointment()
complete_appointment()
get_patient_appointments()
get_doctor_appointments()
display_appointment()
display_appointments()
```

Example:

```python
appointment = appointment_service.create_appointment(
    patient_service,
    doctor_service,
    patient_id=1,
    doctor_id=1,
    date="2026-08-10",
    time="10:00 AM"
)
```

---

# 17. Billing Service

`BillingService` manages hospital bills.

Responsibilities:

```text
create_bill()
find_bill()
pay_bill()
get_patient_bills()
calculate_total()
calculate_pending_total()
display_bill()
display_patient_bills()
display_all_bills()
```

Example:

```python
bill = billing_service.create_bill(
    patient_id=1,
    amount=5000,
    description="Consultation"
)
```

Pay:

```python
billing_service.pay_bill(
    bill.bill_id
)
```

---

# 18. Custom Exceptions

The project uses a custom exception hierarchy.

```text
HospitalError
│
├── PatientNotFoundError
├── DoctorNotFoundError
├── DepartmentNotFoundError
├── AppointmentNotFoundError
├── BillNotFoundError
├── InvalidAmountError
└── InvalidAppointmentError
```

Base exception:

```python
class HospitalError(Exception):

    pass
```

Example:

```python
class PatientNotFoundError(HospitalError):

    def __init__(self, patient_id):

        super().__init__(
            f"Patient not found: {patient_id}"
        )
```

---

# 19. Exception Handling

The application handles business errors centrally.

```python
try:

    patient_service.find_patient(100)

except HospitalError as error:

    print("Hospital Error:", error)
```

This is better than allowing the program to crash.

---

# 20. Main Application Flow

The application starts from:

```python
if __name__ == "__main__":

    main()
```

The main menu provides operations such as:

```text
1.  Register Patient
2.  View Patients
3.  View Patient

4.  Register Doctor
5.  View Doctors

6.  Create Department
7.  Assign Doctor to Department
8.  View Departments

9.  Create Appointment
10. View Appointments
11. Cancel Appointment
12. Complete Appointment

13. Add Medical Record
14. View Medical Records

15. Create Bill
16. Pay Bill
17. View Patient Bills
18. View All Bills

0. Exit
```

---

# 21. Complete Application Flow

Example:

```text
Start
  │
  ▼
Register Patient
  │
  ▼
Register Doctor
  │
  ▼
Create Department
  │
  ▼
Assign Doctor
  │
  ▼
Create Appointment
  │
  ▼
Add Medical Record
  │
  ▼
Create Bill
  │
  ▼
Pay Bill
  │
  ▼
View Patient Information
```

---

# 22. Example Usage

Register patient:

```python
patient = patient_service.register_patient(
    name="Alex",
    age=45,
    phone="9876543210",
    blood_group="O+"
)
```

Register doctor:

```python
doctor = doctor_service.register_doctor(
    name="Dr. Ravi",
    age=45,
    phone="9999999999",
    specialization="Cardiology"
)
```

Create department:

```python
department = doctor_service.create_department(
    "Cardiology"
)
```

Assign doctor:

```python
doctor_service.assign_doctor_to_department(
    doctor.doctor_id,
    department.department_id
)
```

Create appointment:

```python
appointment_service.create_appointment(
    patient_service,
    doctor_service,
    patient.patient_id,
    doctor.doctor_id,
    "2026-08-10",
    "10:00 AM"
)
```

Add medical record:

```python
patient_service.add_medical_record(
    patient_id=patient.patient_id,
    doctor_id=doctor.doctor_id,
    diagnosis="Fever",
    treatment="Medication",
    date="2026-08-10"
)
```

Create bill:

```python
bill = billing_service.create_bill(
    patient_id=patient.patient_id,
    amount=5000,
    description="Consultation"
)
```

Pay bill:

```python
billing_service.pay_bill(
    bill.bill_id
)
```

---

# 23. OOP Concepts Demonstrated

| Concept             | Where Used                           |
| ------------------- | ------------------------------------ |
| Class               | All model classes                    |
| Object              | Patient, Doctor, Bill, etc.          |
| Encapsulation       | Model attributes                     |
| Inheritance         | Patient/Doctor → Person              |
| Composition         | Patient → appointments/records/bills |
| Association         | Patient ↔ Appointment ↔ Doctor       |
| Polymorphism        | Overridden `display()` / `__str__()` |
| Abstraction         | Service responsibilities             |
| Dataclass           | Appointment, MedicalRecord, Bill     |
| Exception Hierarchy | Hospital exceptions                  |
| Modular Design      | Separate packages                    |

---

# 24. SOLID Concepts

The project introduces practical SOLID thinking.

## Single Responsibility Principle

Each service has a focused responsibility.

```text
PatientService
    → Patient operations

DoctorService
    → Doctor and department operations

AppointmentService
    → Appointment operations

BillingService
    → Billing operations
```

---

## Dependency Separation

`main.py` does not directly manipulate every model.

Instead:

```text
main.py
   ↓
Service
   ↓
Model
```

This keeps the application easier to maintain.

---

# 25. Why Services?

Without services, `main.py` could become:

```python
patient = Patient(...)
doctor = Doctor(...)
appointment = Appointment(...)
bill = Bill(...)

# hundreds of lines of business logic
```

Instead:

```python
patient_service.register_patient(...)
doctor_service.register_doctor(...)
appointment_service.create_appointment(...)
billing_service.create_bill(...)
```

The business logic stays inside the appropriate service.

---

# 26. Testing

Tests are placed inside:

```text
tests/
│
├── test_patient.py
├── test_doctor.py
└── test_appointment.py
```

The project can use Python's built-in:

```python
unittest
```

Example:

```python
import unittest

from models.patient import Patient


class TestPatient(unittest.TestCase):

    def test_patient_creation(self):

        patient = Patient(
            1,
            "Alex",
            45,
            "9876543210",
            "O+"
        )

        self.assertEqual(
            patient.name,
            "Alex"
        )


if __name__ == "__main__":

    unittest.main()
```

---

# 27. Running the Application

From the project directory:

```powershell
python main.py
```

---

# 28. Running Tests

Run all tests:

```powershell
python -m unittest discover
```

Run a specific test:

```powershell
python -m unittest tests.test_patient
```

---

# 29. Requirements

The current project uses only the Python standard library.

Therefore:

```text
No external packages are required.
```

The minimum recommended Python version is:

```text
Python 3.10+
```

---

# 30. Learning Outcomes

After completing this project, you should understand how to build a multi-module Python application using:

```text
Python
  │
  ├── OOP
  ├── Inheritance
  ├── Composition
  ├── Association
  ├── Dataclasses
  ├── Services
  ├── Custom Exceptions
  ├── Exception Handling
  ├── Unit Testing
  └── Modular Architecture
```

---

# 31. Project Complexity

This project is intentionally more than a collection of isolated classes.

It demonstrates the transition:

```text
Python Basics
      ↓
OOP
      ↓
Multiple Classes
      ↓
Object Relationships
      ↓
Services
      ↓
Custom Exceptions
      ↓
Testing
      ↓
Real Application Structure
```

The goal is to understand **how OOP is actually used in an application**, rather than learning classes and inheritance only as individual concepts.

---

# 32. Future Enhancements

The current version uses in-memory data.

Possible future enhancements:

```text
Database
   ↓
SQLite / MySQL

Logging
   ↓
Application logs

Authentication
   ↓
Admin / Doctor / Receptionist

REST API
   ↓
Flask / FastAPI

Frontend
   ↓
HTML / CSS / JavaScript

Testing
   ↓
pytest

Deployment
   ↓
Cloud / Server
```

These are intentionally kept outside the current project so that the core OOP architecture remains easy to understand.

---

# 33. Final Architecture

```text
02_Hospital_Management_System
│
├── main.py
│
├── models
│   ├── Person
│   │
│   ├── Patient
│   │   ├── Appointment
│   │   ├── MedicalRecord
│   │   └── Bill
│   │
│   ├── Doctor
│   │   └── Appointment
│   │
│   └── Department
│       └── Doctor
│
├── services
│   ├── PatientService
│   ├── DoctorService
│   ├── AppointmentService
│   └── BillingService
│
├── exceptions
│   └── HospitalError
│       ├── PatientNotFoundError
│       ├── DoctorNotFoundError
│       ├── DepartmentNotFoundError
│       ├── AppointmentNotFoundError
│       ├── BillNotFoundError
│       └── InvalidAmountError
│
└── tests
    ├── Patient Tests
    ├── Doctor Tests
    └── Appointment Tests
```

---

# 34. Key Principle

The main lesson of this project is:

```text
Do not put everything inside main.py.

        main.py
           ↓
      Services
           ↓
        Models

Errors → Exceptions
Tests  → Tests
```

This structure makes the application easier to:

* Understand
* Test
* Extend
* Maintain
* Refactor

---

# Project Status

```text
Project 02 – Hospital Management System

Models       : Complete
Services     : Complete
Exceptions   : Complete
Main         : Complete
Requirements : Complete
README       : Complete
Tests        : Structure Ready

Status       : Ready for Testing
```
