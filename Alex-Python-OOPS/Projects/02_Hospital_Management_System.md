# Project 02 – Hospital Management System

## File Name

```
02_Hospital_Management_System.md
```

---

# Level

```
Intermediate → Advanced
```

---

# Domain

```
Healthcare Application
```

---

# Project Overview

A real-world hospital management application developed using Python OOP principles.

The system manages:

- Patients
- Doctors
- Departments
- Appointments
- Medical Records
- Billing
- Prescriptions

This project focuses heavily on:

- Object Relationships
- Composition
- Association
- Polymorphism
- Service Layer Architecture

---

# 1. Project Objective

Build a scalable hospital management system using:

- Object-Oriented Programming
- Class Relationships
- SOLID Principles
- Exception Handling
- Logging
- Testing

---

# 2. Real World Problem

A hospital contains multiple entities:

```
Hospital

   |

   |

Departments

   |

   |

Doctors

   |

   |

Patients

   |

   |

Appointments

   |

   |

Medical Records
```

A good design should represent real-world relationships.

---

# 3. Project Features

---

# Patient Management

Features:

- Register Patient
- Update Patient Details
- View Patient History
- Assign Doctor

Patient Data:

```
Patient ID

Name

Age

Gender

Phone

Medical History
```

---

# Doctor Management

Features:

- Add Doctor
- Assign Department
- View Availability
- Manage Appointments


Doctor Data:

```
Doctor ID

Name

Specialization

Experience
```

---

# Appointment Management

Features:

- Book Appointment
- Cancel Appointment
- View Schedule


Appointment Contains:

```
Patient

Doctor

Date

Time

Status
```

---

# Medical Records

Stores:

```
Diagnosis

Prescription

Test Results

Doctor Notes
```

---

# Billing System

Features:

- Generate Bill
- Add Treatment Charges
- Payment Status

---

# 4. OOP Concepts Used

| Concept | Usage |
|-|-|
| Classes | Patient, Doctor, Appointment |
| Encapsulation | Patient data protection |
| Composition | Hospital contains departments |
| Association | Doctor and Patient relationship |
| Inheritance | Different staff types |
| Polymorphism | Different billing methods |
| Abstraction | Staff interface |
| Dataclass | Medical records |

---

# 5. Object Relationships

## Hospital → Department

One-to-Many

```
Hospital

 |

 |---- Cardiology

 |---- Neurology

 |---- Orthopedics
```

---

## Department → Doctor

One-to-Many

```
Department

 |

 |---- Doctor

 |---- Doctor
```

---

## Doctor ↔ Patient

Many-to-Many

```
Doctor

 |

Patients
```

---

## Patient → Medical Record

One-to-One

```
Patient

 |

Medical Record
```

---

# 6. Design Principles Used

---

# Single Responsibility

Separate:

```
Patient Service

Doctor Service

Billing Service

Appointment Service
```

---

# Open Closed Principle

Adding new staff:

```
Doctor

Nurse

Receptionist
```

without changing existing classes.

---

# Dependency Inversion

Services depend on interfaces.

---

# 7. Design Patterns Used

---

# Factory Pattern

Create staff:

```
StaffFactory

     |

----------------

Doctor

Nurse

Receptionist
```

---

# Strategy Pattern

Billing calculation:

```
Billing Strategy

      |

----------------

Insurance

Cash

Card
```

---

# Observer Pattern

Appointment notification:

```
Appointment Created

        |

----------------

Patient

Doctor
```

---

# 8. Project Folder Structure

```
02_Hospital_Management_System/

│
├── main.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
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
├── repositories/
│   ├── patient_repository.py
│   └── doctor_repository.py
│
├── factories/
│   └── staff_factory.py
│
├── strategies/
│   └── payment_strategy.py
│
├── exceptions/
│   └── hospital_exceptions.py
│
├── utils/
│   ├── logger.py
│   └── validator.py
│
├── database/
│   └── hospital.json
│
├── tests/
│   ├── test_patient.py
│   ├── test_doctor.py
│   └── test_appointment.py
│
├── requirements.txt
│
└── README.md
```

---

# 9. File Responsibilities

| File | Responsibility |
|-|-|
| person.py | Base person class |
| patient.py | Patient entity |
| doctor.py | Doctor entity |
| department.py | Hospital department |
| appointment.py | Appointment handling |
| medical_record.py | Patient history |
| bill.py | Billing model |
| services | Business logic |
| repositories | Data management |
| factories | Object creation |

---

# 10. Code Implementation

---

# models/person.py

```python
from abc import ABC


class Person(ABC):


    def __init__(
        self,
        name,
        age
    ):

        self.name = name

        self.age = age
```

---

# models/patient.py

```python
from models.person import Person



class Patient(Person):


    def __init__(
        self,
        patient_id,
        name,
        age
    ):

        super().__init__(
            name,
            age
        )


        self.patient_id = patient_id

        self.records = []



    def add_record(
        self,
        record
    ):

        self.records.append(record)
```

---

# models/doctor.py

```python
from models.person import Person



class Doctor(Person):


    def __init__(
        self,
        doctor_id,
        name,
        specialization
    ):

        super().__init__(
            name,
            30
        )


        self.doctor_id = doctor_id

        self.specialization = specialization



    def diagnose(
        self,
        patient
    ):

        print(
            f"{self.name} treating {patient.name}"
        )
```

---

# models/appointment.py

```python
from dataclasses import dataclass



@dataclass
class Appointment:


    doctor: object

    patient: object

    date: str

    status: str = "Booked"
```

---

# models/medical_record.py

```python
from dataclasses import dataclass



@dataclass
class MedicalRecord:


    diagnosis:str

    prescription:str

    notes:str
```

---

# 11. Service Layer

---

# services/appointment_service.py

```python
class AppointmentService:


    def book(
        self,
        doctor,
        patient,
        date
    ):


        print(
            "Appointment Booked"
        )


        return {

            "doctor":doctor.name,

            "patient":patient.name,

            "date":date

        }
```

---

# 12. Factory Pattern

---

# factories/staff_factory.py

```python
from models.doctor import Doctor



class StaffFactory:


    @staticmethod
    def create_staff(
        staff_type,
        id,
        name
    ):


        if staff_type=="doctor":

            return Doctor(
                id,
                name,
                "Cardiology"
            )


        raise Exception(
            "Invalid Staff"
        )
```

---

# 13. Strategy Pattern

---

# strategies/payment_strategy.py

```python
from abc import ABC,abstractmethod



class PaymentStrategy(ABC):


    @abstractmethod
    def pay(self,amount):

        pass



class CashPayment(
    PaymentStrategy
):


    def pay(self,amount):

        print(
            f"Cash Paid {amount}"
        )



class InsurancePayment(
    PaymentStrategy
):


    def pay(self,amount):

        print(
            f"Insurance Paid {amount}"
        )
```

---

# 14. Main Application

---

# main.py

```python
from models.patient import Patient

from factories.staff_factory import StaffFactory

from services.appointment_service import AppointmentService



patient = Patient(

    101,

    "Alex",

    45

)



doctor = StaffFactory.create_staff(

    "doctor",

    1,

    "Dr Kumar"

)



doctor.diagnose(patient)



service = AppointmentService()


appointment = service.book(

    doctor,

    patient,

    "10-Aug-2026"

)


print(appointment)
```

---

# Output

```
Dr Kumar treating Alex

Appointment Booked

{
 doctor:'Dr Kumar',
 patient:'Alex',
 date:'10-Aug-2026'
}
```

---

# 15. Testing

## tests/test_patient.py

```python
import unittest

from models.patient import Patient



class TestPatient(unittest.TestCase):


    def test_patient_creation(self):


        patient = Patient(

            1,

            "Alex",

            45

        )


        self.assertEqual(

            patient.name,

            "Alex"

        )


if __name__=="__main__":

    unittest.main()
```

---

# 16. Execution Flow

```
main.py

 |

Patient

 |

Doctor

 |

Appointment Service

 |

Medical Record

 |

Billing
```

---

# 17. Future Enhancements

Add:

```
Database Integration

Doctor Login

Patient Portal

Online Appointment

Insurance API

Hospital Dashboard
```

---

# 18. Learning Outcome

After completing this project:

You understand:

✅ Complex Object Relationships

✅ Composition vs Inheritance

✅ Healthcare Domain Modeling

✅ Service Layer Design

✅ Factory Pattern

✅ Strategy Pattern

✅ Real-world Python Architecture

---

# Project Completion Level

```
Python OOP              ⭐⭐⭐⭐⭐

Relationships           ⭐⭐⭐⭐⭐

SOLID Design            ⭐⭐⭐⭐

Design Patterns         ⭐⭐⭐⭐

Real Application        ⭐⭐⭐⭐⭐
```

---

# Next Project

```
03_Library_Management_System.md
```

Focus:

- Book Management
- Member Management
- Borrow/Return Workflow
- Search System
- Collection Classes
- Iterator & Magic Methods
