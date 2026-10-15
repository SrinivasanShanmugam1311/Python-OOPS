# Project 06 – Online Course Platform

## File Name

```
06_Online_Course_Platform.md
```

---

# Level

```
Intermediate → Advanced
```

---

# Domain

```
E-Learning / Learning Management System (LMS)
```

---

# Project Overview

A real-world online learning platform developed using Python OOP principles.

The system manages:

- Students
- Instructors
- Courses
- Lessons
- Enrollments
- Payments
- Progress Tracking
- Certificates
- Notifications

This project focuses on:

- Abstract Classes
- Interfaces
- Composition
- Inheritance
- Polymorphism
- SOLID Principles
- Plugin Architecture

---

# 1. Project Objective

Build a scalable Learning Management System using:

- Python Object-Oriented Programming
- Clean Architecture
- Design Patterns
- Exception Handling
- Testing

---

# 2. Real World Problem

An online education platform contains:

```
Platform

    |

    |

Courses

    |

    |

Lessons

    |

    |

Students

    |

    |

Progress

    |

    |

Certificates
```

The system should support:

```
Different Users

Different Course Types

Different Payment Methods

Different Learning Rules
```

---

# 3. Project Features

---

# User Management

User Types:

```
Student

Instructor

Admin
```

Features:

- Register User
- Login
- Manage Profile
- Role Based Access

---

# Course Management

Features:

- Create Course
- Update Course
- Publish Course
- Delete Course


Course Information:

```
Course ID

Title

Description

Instructor

Lessons

Price
```

---

# Lesson Management

Features:

- Add Lesson
- Remove Lesson
- Track Completion


Lesson:

```
Lesson ID

Title

Video URL

Duration

Status
```

---

# Student Enrollment

Features:

- Browse Courses
- Enroll Course
- View Purchased Courses
- Track Progress


Enrollment:

```
Student

Course

Date

Progress
```

---

# Payment System

Payment Methods:

```
Credit Card

UPI

Subscription

Wallet
```

---

# Certificate System

Generate certificate after:

```
100% Completion
```

---

# Notification System

Notifications:

```
Course Published

Enrollment Success

Certificate Generated
```

---

# 4. OOP Concepts Used

| Concept | Usage |
|-|-|
| Classes | Student, Course, Lesson |
| Encapsulation | Progress control |
| Inheritance | User hierarchy |
| Polymorphism | Payment methods |
| Abstraction | Course interface |
| Composition | Course contains lessons |
| Dataclass | Course data |
| Protocol | Plugin system |

---

# 5. Object Relationships

---

# Instructor → Courses

One-to-Many

```
Instructor

 |

 |---- Course

 |---- Course
```

---

# Course → Lessons

Composition

```
Course

 |

 |---- Lesson

 |---- Lesson
```

---

# Student ↔ Course

Many-to-Many

```
Student

 |

Enrollment

 |

Course
```

---

# Student → Certificate

One-to-One

```
Student

 |

Certificate
```

---

# 6. Design Principles Used

---

# Single Responsibility

Separate:

```
User Service

Course Service

Enrollment Service

Payment Service

Certificate Service
```

---

# Open Closed Principle

New course types:

```
Video Course

Live Course

Workshop Course
```

can be added easily.

---

# Interface Segregation

Different interfaces:

```
Payment Interface

Notification Interface

Content Interface
```

---

# Dependency Inversion

Services depend on abstractions.

---

# 7. Design Patterns Used

---

# Factory Pattern

Create users:

```
UserFactory

       |

----------------

Student

Instructor

Admin
```

---

# Strategy Pattern

Payment processing:

```
PaymentStrategy

       |

----------------

UPI

Card

Subscription
```

---

# Observer Pattern

Course updates:

```
New Lesson Added

        |

Students Notified
```

---

# Builder Pattern

Create complex courses:

```
Course Builder

Title

Lessons

Instructor

Pricing
```

---

# Plugin Architecture

Add new learning modules:

```
Plugin

 |

Quiz Plugin

Assignment Plugin

Discussion Plugin
```

---

# 8. Project Folder Structure

```
06_Online_Course_Platform/

│
├── main.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── student.py
│   ├── instructor.py
│   ├── admin.py
│   ├── course.py
│   ├── lesson.py
│   ├── enrollment.py
│   ├── certificate.py
│   └── progress.py
│
├── services/
│   ├── __init__.py
│   ├── user_service.py
│   ├── course_service.py
│   ├── enrollment_service.py
│   ├── payment_service.py
│   └── certificate_service.py
│
├── factories/
│   └── user_factory.py
│
├── strategies/
│   └── payment_strategy.py
│
├── builders/
│   └── course_builder.py
│
├── plugins/
│   ├── base_plugin.py
│   ├── quiz_plugin.py
│   └── assignment_plugin.py
│
├── observers/
│   └── notification.py
│
├── exceptions/
│   └── course_exceptions.py
│
├── utils/
│   ├── logger.py
│   └── validator.py
│
├── database/
│   └── courses.json
│
├── tests/
│   ├── test_course.py
│   ├── test_enrollment.py
│   └── test_payment.py
│
├── requirements.txt
│
└── README.md
```

---

# 9. File Responsibilities

| File | Responsibility |
|-|-|
| user.py | Base user class |
| student.py | Student operations |
| instructor.py | Course creation |
| course.py | Course entity |
| lesson.py | Course content |
| enrollment.py | Student enrollment |
| progress.py | Learning tracking |
| certificate.py | Completion certificate |
| services | Business logic |
| plugins | Extensible features |

---

# 10. Code Implementation

---

# models/user.py

```python
from abc import ABC, abstractmethod


class User(ABC):


    def __init__(
        self,
        user_id,
        name
    ):

        self.user_id = user_id

        self.name = name



    @abstractmethod
    def role(self):

        pass
```

---

# models/student.py

```python
from models.user import User



class Student(User):


    def role(self):

        return "Student"



    def enroll(
        self,
        course
    ):

        print(
            f"{self.name} enrolled {course.title}"
        )
```

---

# models/instructor.py

```python
from models.user import User



class Instructor(User):


    def role(self):

        return "Instructor"



    def create_course(
        self,
        course
    ):

        print(
            f"{self.name} created {course.title}"
        )
```

---

# models/course.py

```python
from dataclasses import dataclass,field



@dataclass
class Course:


    id:int

    title:str

    price:float

    lessons:list = field(
        default_factory=list
    )



    def add_lesson(
        self,
        lesson
    ):

        self.lessons.append(
            lesson
        )
```

---

# models/lesson.py

```python
from dataclasses import dataclass



@dataclass
class Lesson:


    id:int

    title:str

    duration:int
```

---

# 11. Payment Strategy

---

# strategies/payment_strategy.py

```python
from abc import ABC,abstractmethod



class PaymentStrategy(ABC):


    @abstractmethod
    def pay(self,amount):

        pass



class UPIPayment(
    PaymentStrategy
):


    def pay(self,amount):

        print(
            f"UPI Paid {amount}"
        )



class CardPayment(
    PaymentStrategy
):


    def pay(self,amount):

        print(
            f"Card Paid {amount}"
        )
```

---

# 12. Course Builder

---

# builders/course_builder.py

```python
class CourseBuilder:


    def __init__(self):

        self.data={}



    def title(
        self,
        title
    ):

        self.data["title"]=title

        return self



    def price(
        self,
        price
    ):

        self.data["price"]=price

        return self



    def build(self):

        return self.data
```

---

# 13. Plugin Architecture

---

# plugins/base_plugin.py

```python
from abc import ABC,abstractmethod



class Plugin(ABC):


    @abstractmethod
    def execute(self):

        pass
```

---

# plugins/quiz_plugin.py

```python
from plugins.base_plugin import Plugin



class QuizPlugin(Plugin):


    def execute(self):

        print(
            "Quiz Started"
        )
```

---

# 14. Enrollment Service

---

# services/enrollment_service.py

```python
class EnrollmentService:


    def enroll(
        self,
        student,
        course
    ):


        student.enroll(course)


        print(
            "Enrollment Completed"
        )
```

---

# 15. Main Application

---

# main.py

```python
from models.student import Student

from models.course import Course

from models.lesson import Lesson

from services.enrollment_service import EnrollmentService



student = Student(

    1,

    "Alex"

)



course = Course(

    101,

    "Python OOP",

    5000

)



lesson = Lesson(

    1,

    "Classes",

    60

)



course.add_lesson(
    lesson
)



service = EnrollmentService()


service.enroll(

    student,

    course

)



print(course)
```

---

# Output

```
Alex enrolled Python OOP

Enrollment Completed
```

---

# 16. Testing

## tests/test_course.py

```python
import unittest

from models.course import Course



class TestCourse(unittest.TestCase):


    def test_course_creation(self):


        course = Course(

            1,

            "Python",

            1000

        )


        self.assertEqual(

            course.title,

            "Python"

        )


if __name__=="__main__":

    unittest.main()
```

---

# 17. Execution Flow

```
Student

 |

Enrollment Service

 |

Course

 |

Lessons

 |

Payment

 |

Certificate
```

---

# 18. Future Enhancements

Add:

```
Video Streaming

AI Recommendation

Discussion Forum

Live Classes

Quiz Engine

Mobile Application API

Cloud Storage
```

---

# 19. Learning Outcome

After completing this project:

You understand:

✅ Abstract Classes

✅ Interfaces

✅ Composition

✅ Plugin Architecture

✅ Strategy Pattern

✅ Builder Pattern

✅ Observer Pattern

✅ Learning Platform Architecture

---

# Project Completion Level

```
Python OOP              ⭐⭐⭐⭐⭐

Architecture             ⭐⭐⭐⭐⭐

Design Patterns           ⭐⭐⭐⭐⭐

Extensibility             ⭐⭐⭐⭐⭐

Real Application          ⭐⭐⭐⭐⭐
```

---

# Next Project

```
07_Employee_Payroll_System.md
```

Focus:

- Employee Hierarchy
- Salary Processing
- Attendance
- Reports
- Tax Calculation
- Strategy Pattern
