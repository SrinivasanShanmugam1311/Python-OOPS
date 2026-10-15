# Project 07 – Employee Payroll System

## File Name

```
07_Employee_Payroll_System.md
```

---

# Level

```
Intermediate → Advanced
```

---

# Domain

```
HR / Enterprise Payroll Application
```

---

# Project Overview

A real-world employee payroll management system developed using Python OOP principles.

The system manages:

- Employees
- Departments
- Roles
- Attendance
- Salary Calculation
- Tax Calculation
- Payslips
- Bonuses
- Reports

This project focuses on:

- Inheritance
- Polymorphism
- Abstract Classes
- Strategy Pattern
- Factory Pattern
- SOLID Principles
- Enterprise Application Design

---

# 1. Project Objective

Build a scalable payroll system using:

- Python OOP
- Clean Architecture
- Design Patterns
- Exception Handling
- Unit Testing

---

# 2. Real World Problem

A company payroll system contains:

```
Company

 |

Departments

 |

Employees

 |

Attendance

 |

Salary

 |

Payslip
```

Different employees have different rules:

```
Developer

Manager

HR

Contract Employee

Intern
```

The system should calculate salaries dynamically.

---

# 3. Project Features

---

# Employee Management

Features:

- Add Employee
- Remove Employee
- Update Employee
- Search Employee


Employee Data:

```
Employee ID

Name

Department

Designation

Joining Date
```

---

# Employee Types

```
Full Time Employee

Contract Employee

Intern

Manager

Developer
```

---

# Attendance Management

Features:

- Mark Attendance
- Calculate Working Days
- Leave Management


Attendance:

```
Employee

Month

Present Days

Leave Days
```

---

# Salary Management

Features:

- Calculate Salary
- Add Bonus
- Deduct Tax
- Generate Payslip


Salary Components:

```
Basic Salary

Allowance

Bonus

Tax

Deduction

Net Salary
```

---

# Tax Management

Supports:

```
Income Tax

Professional Tax

Insurance Deduction
```

---

# Reporting System

Reports:

```
Employee Report

Salary Report

Department Report

Attendance Report
```

---

# 4. OOP Concepts Used

| Concept | Usage |
|-|-|
| Classes | Employee, Salary |
| Encapsulation | Salary protection |
| Inheritance | Employee hierarchy |
| Polymorphism | Salary calculation |
| Abstract Classes | Employee interface |
| Composition | Employee has Salary |
| Dataclass | Payroll records |
| Strategy Pattern | Tax calculation |

---

# 5. Object Relationships

---

# Company → Departments

One-to-Many

```
Company

 |

 |---- IT

 |---- HR

 |---- Finance
```

---

# Department → Employees

One-to-Many

```
Department

 |

 |---- Employee

 |---- Employee
```

---

# Employee → Salary

One-to-One

```
Employee

 |

Salary
```

---

# Employee → Attendance

One-to-Many

```
Employee

 |

Attendance Records
```

---

# 6. Design Principles Used

---

# Single Responsibility Principle

Separate:

```
Employee Service

Attendance Service

Payroll Service

Tax Service
```

---

# Open Closed Principle

New employee types:

```
Freelancer

Consultant

Part-Time Employee
```

can be added easily.

---

# Liskov Substitution Principle

All employees should work with payroll system.

---

# Dependency Inversion

Payroll depends on salary calculation abstraction.

---

# 7. Design Patterns Used

---

# Factory Pattern

Employee creation:

```
EmployeeFactory

        |

-----------------

Developer

Manager

Intern
```

---

# Strategy Pattern

Salary calculation:

```
SalaryStrategy

        |

-----------------

Full Time Salary

Contract Salary

Intern Salary
```

---

# Strategy Pattern

Tax calculation:

```
TaxStrategy

        |

-----------------

Normal Tax

Corporate Tax

No Tax
```

---

# Observer Pattern

Salary updates:

```
Salary Generated

        |

Employee Notification
```

---

# Template Method Pattern

Payroll workflow:

```
Calculate Salary

     |

Calculate Tax

     |

Generate Payslip
```

---

# 8. Project Folder Structure

```
07_Employee_Payroll_System/

│
├── main.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── models/
│   ├── __init__.py
│   ├── employee.py
│   ├── developer.py
│   ├── manager.py
│   ├── intern.py
│   ├── department.py
│   ├── attendance.py
│   ├── salary.py
│   └── payslip.py
│
├── services/
│   ├── __init__.py
│   ├── employee_service.py
│   ├── attendance_service.py
│   ├── payroll_service.py
│   └── report_service.py
│
├── factories/
│   └── employee_factory.py
│
├── strategies/
│   ├── salary_strategy.py
│   └── tax_strategy.py
│
├── templates/
│   └── payroll_template.py
│
├── observers/
│   └── notification.py
│
├── exceptions/
│   └── payroll_exceptions.py
│
├── utils/
│   ├── logger.py
│   └── validator.py
│
├── database/
│   └── payroll.json
│
├── tests/
│   ├── test_employee.py
│   ├── test_salary.py
│   └── test_payroll.py
│
├── requirements.txt
│
└── README.md
```

---

# 9. File Responsibilities

| File | Responsibility |
|-|-|
| employee.py | Base employee |
| developer.py | Developer employee |
| manager.py | Manager employee |
| attendance.py | Attendance tracking |
| salary.py | Salary data |
| payslip.py | Salary output |
| services | Business logic |
| factories | Object creation |
| strategies | Salary rules |

---

# 10. Code Implementation

---

# models/employee.py

```python
from abc import ABC, abstractmethod



class Employee(ABC):


    def __init__(
        self,
        id,
        name,
        basic_salary
    ):

        self.id = id

        self.name = name

        self.__salary = basic_salary



    def get_salary(self):

        return self.__salary



    @abstractmethod
    def calculate_salary(self):

        pass
```

---

# models/developer.py

```python
from models.employee import Employee



class Developer(Employee):


    def calculate_salary(self):

        return (

            self.get_salary()

            +

            5000

        )
```

---

# models/manager.py

```python
from models.employee import Employee



class Manager(Employee):


    def calculate_salary(self):

        return (

            self.get_salary()

            +

            10000

        )
```

---

# Concepts Used

Inheritance:

```
Employee

 |

Developer

 |

Manager
```

Polymorphism:

```
calculate_salary()
```

---

# 11. Attendance Model

---

# models/attendance.py

```python
from dataclasses import dataclass



@dataclass
class Attendance:


    employee_id:int

    working_days:int

    leave_days:int
```

---

# 12. Salary Strategy

---

# strategies/salary_strategy.py

```python
from abc import ABC,abstractmethod



class SalaryStrategy(ABC):


    @abstractmethod
    def calculate(
        self,
        salary
    ):

        pass



class FullTimeSalary(
    SalaryStrategy
):


    def calculate(
        self,
        salary
    ):

        return salary * 1.1



class ContractSalary(
    SalaryStrategy
):


    def calculate(
        self,
        salary
    ):

        return salary
```

---

# 13. Tax Strategy

---

# strategies/tax_strategy.py

```python
class TaxStrategy:


    def calculate(
        self,
        salary
    ):

        return salary * 0.1
```

---

# 14. Employee Factory

---

# factories/employee_factory.py

```python
from models.developer import Developer

from models.manager import Manager



class EmployeeFactory:


    @staticmethod
    def create(
        employee_type,
        id,
        name,
        salary
    ):


        if employee_type=="developer":

            return Developer(
                id,
                name,
                salary
            )


        if employee_type=="manager":

            return Manager(
                id,
                name,
                salary
            )


        raise Exception(
            "Invalid Employee"
        )
```

---

# 15. Payroll Service

---

# services/payroll_service.py

```python
class PayrollService:


    def generate(
        self,
        employee
    ):


        salary = employee.calculate_salary()


        tax = salary * 0.1


        net_salary = salary-tax


        return {


            "employee":employee.name,


            "gross":salary,


            "tax":tax,


            "net":net_salary

        }
```

---

# 16. Main Application

---

# main.py

```python
from factories.employee_factory import EmployeeFactory

from services.payroll_service import PayrollService



employee = EmployeeFactory.create(

    "developer",

    1,

    "Alex",

    50000

)



service = PayrollService()



payslip = service.generate(

    employee

)



print(payslip)
```

---

# Output

```
{
employee:'Alex',
gross:55000,
tax:5500,
net:49500
}
```

---

# 17. Testing

## tests/test_employee.py

```python
import unittest

from models.developer import Developer



class TestEmployee(unittest.TestCase):


    def test_salary(self):


        emp = Developer(

            1,

            "Alex",

            50000

        )


        self.assertEqual(

            emp.calculate_salary(),

            55000

        )


if __name__=="__main__":

    unittest.main()
```

---

# 18. Execution Flow

```
Employee Factory

        |

Employee Object

        |

Payroll Service

        |

Salary Strategy

        |

Tax Calculation

        |

Payslip
```

---

# 19. Future Enhancements

Add:

```
Database Integration

Employee Login

Attendance Device Integration

Cloud Payroll

Email Payslip

HR Dashboard

REST API
```

---

# 20. Learning Outcome

After completing this project:

You understand:

✅ Enterprise OOP Design

✅ Inheritance Hierarchy

✅ Abstract Classes

✅ Runtime Polymorphism

✅ Strategy Pattern

✅ Factory Pattern

✅ Template Workflow

✅ Payroll Architecture

---

# Project Completion Level

```
Python OOP              ⭐⭐⭐⭐⭐

Inheritance             ⭐⭐⭐⭐⭐

Polymorphism            ⭐⭐⭐⭐⭐

SOLID Principles        ⭐⭐⭐⭐⭐

Enterprise Design       ⭐⭐⭐⭐⭐
```

---

# Next Project

```
08_Banking_Transaction_System.md
```

Focus:

- Account Management
- Transactions
- Security
- Authentication
- Exception Handling
- Data Protection
