# Project 05 – Hotel Management System

## File Name

```
05_Hotel_Management_System.md
```

---

# Level

```
Intermediate → Advanced
```

---

# Domain

```
Hospitality / Hotel Booking Application
```

---

# Project Overview

A real-world hotel management system developed using Python OOP principles.

The system manages:

- Hotels
- Rooms
- Customers
- Reservations
- Check-in / Check-out
- Billing
- Payments
- Room Availability

This project focuses on:

- Object Relationships
- State Management
- Strategy Pattern
- Factory Pattern
- Service Layer Architecture

---

# 1. Project Objective

Build a scalable hotel booking system using:

- Python Object-Oriented Programming
- SOLID Principles
- Design Patterns
- Exception Handling
- Testing

---

# 2. Real World Problem

A hotel system contains multiple entities:

```
Hotel

 |

 |

Rooms

 |

 |

Reservation

 |

 |

Customer

 |

 |

Payment
```

The system should handle:

- Multiple room types
- Availability checking
- Booking lifecycle
- Pricing rules
- Payment processing

---

# 3. Project Features

---

# Hotel Management

Features:

- Add Hotel
- Update Hotel Details
- View Hotel Information


Hotel Data:

```
Hotel ID

Name

Location

Rooms
```

---

# Room Management

Room Types:

```
Single Room

Double Room

Suite Room

Luxury Room
```

Room Information:

```
Room Number

Type

Price

Status
```

Room Status:

```
AVAILABLE

BOOKED

MAINTENANCE
```

---

# Customer Management

Features:

- Register Customer
- Update Profile
- View Booking History


Customer:

```
Customer ID

Name

Phone

Email
```

---

# Reservation Management

Features:

- Search Available Rooms
- Book Room
- Cancel Reservation
- Check-in
- Check-out


Reservation:

```
Reservation ID

Customer

Room

Date

Status
```

---

# Billing System

Features:

- Generate Bill
- Calculate Stay Charges
- Apply Discounts
- Process Payment

---

# 4. OOP Concepts Used

| Concept | Usage |
|-|-|
| Classes | Hotel, Room, Customer |
| Encapsulation | Room status protection |
| Composition | Hotel contains rooms |
| Association | Customer booking relationship |
| Inheritance | Different room types |
| Polymorphism | Pricing calculation |
| Abstract Classes | Payment interface |
| Dataclass | Reservation records |

---

# 5. Object Relationships

---

# Hotel → Rooms

One-to-Many

```
Hotel

 |

 |---- Room

 |---- Room

 |---- Room
```

---

# Customer → Reservations

One-to-Many

```
Customer

 |

 |---- Reservation

 |---- Reservation
```

---

# Reservation → Room

One-to-One

```
Reservation

 |

Room
```

---

# 6. Design Principles Used

---

# Single Responsibility Principle

Separate:

```
Room Service

Booking Service

Billing Service

Payment Service
```

---

# Open Closed Principle

New room types:

```
Standard Room

Premium Room

Villa Room
```

can be added without modifying existing pricing logic.

---

# Dependency Inversion

Services depend on abstractions.

---

# 7. Design Patterns Used

---

# Factory Pattern

Create rooms:

```
RoomFactory

      |

----------------

Single

Double

Suite
```

---

# Strategy Pattern

Pricing calculation:

```
PricingStrategy

        |

----------------

Normal Season

Peak Season

Festival Season
```

---

# State Pattern

Room status:

```
Available

Booked

Maintenance
```

---

# Observer Pattern

Reservation updates:

```
Booking Confirmed

        |

Customer Notification
```

---

# 8. Project Folder Structure

```
05_Hotel_Management_System/

│
├── main.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── models/
│   ├── __init__.py
│   ├── hotel.py
│   ├── room.py
│   ├── single_room.py
│   ├── double_room.py
│   ├── suite_room.py
│   ├── customer.py
│   ├── reservation.py
│   └── bill.py
│
├── services/
│   ├── __init__.py
│   ├── hotel_service.py
│   ├── room_service.py
│   ├── reservation_service.py
│   └── billing_service.py
│
├── factories/
│   └── room_factory.py
│
├── strategies/
│   ├── pricing_strategy.py
│   └── payment_strategy.py
│
├── states/
│   └── room_state.py
│
├── observers/
│   └── notification.py
│
├── exceptions/
│   └── hotel_exceptions.py
│
├── utils/
│   ├── logger.py
│   └── validator.py
│
├── database/
│   └── hotel.json
│
├── tests/
│   ├── test_room.py
│   ├── test_booking.py
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
| hotel.py | Hotel entity |
| room.py | Base room class |
| single_room.py | Single room rules |
| suite_room.py | Luxury room rules |
| customer.py | Guest details |
| reservation.py | Booking data |
| bill.py | Billing model |
| services | Business operations |
| factories | Object creation |
| strategies | Dynamic pricing |

---

# 10. Code Implementation

---

# models/room.py

```python
from abc import ABC, abstractmethod



class Room(ABC):


    def __init__(
        self,
        room_number,
        price
    ):

        self.room_number = room_number

        self.__available = True

        self.price = price



    def book(self):

        if not self.__available:

            raise Exception(
                "Room not available"
            )


        self.__available = False



    def release(self):

        self.__available = True



    def is_available(self):

        return self.__available



    @abstractmethod
    def calculate_price(
        self,
        days
    ):

        pass
```

---

# models/single_room.py

```python
from models.room import Room



class SingleRoom(Room):


    def calculate_price(
        self,
        days
    ):

        return self.price * days
```

---

# models/suite_room.py

```python
from models.room import Room



class SuiteRoom(Room):


    def calculate_price(
        self,
        days
    ):

        return (
            self.price *
            days *
            2
        )
```

---

# Concepts Used

Inheritance:

```
Room

 |

SingleRoom

 |

SuiteRoom
```

Polymorphism:

```
calculate_price()
```

Different behavior.

---

# 11. Customer Model

---

# models/customer.py

```python
class Customer:


    def __init__(
        self,
        id,
        name
    ):

        self.id=id

        self.name=name

        self.reservations=[]



    def add_reservation(
        self,
        reservation
    ):

        self.reservations.append(
            reservation
        )
```

---

# 12. Reservation Model

---

# models/reservation.py

```python
from dataclasses import dataclass



@dataclass
class Reservation:


    customer:object

    room:object

    days:int

    status:str="CONFIRMED"
```

---

# 13. Factory Pattern

---

# factories/room_factory.py

```python
from models.single_room import SingleRoom

from models.suite_room import SuiteRoom



class RoomFactory:


    @staticmethod
    def create_room(
        room_type,
        number,
        price
    ):


        if room_type=="single":

            return SingleRoom(
                number,
                price
            )


        elif room_type=="suite":

            return SuiteRoom(
                number,
                price
            )


        raise Exception(
            "Invalid Room Type"
        )
```

---

# 14. Pricing Strategy

---

# strategies/pricing_strategy.py

```python
from abc import ABC,abstractmethod



class PricingStrategy(ABC):


    @abstractmethod
    def calculate(
        self,
        price
    ):

        pass



class NormalPricing(
    PricingStrategy
):


    def calculate(
        self,
        price
    ):

        return price



class PeakSeasonPricing(
    PricingStrategy
):


    def calculate(
        self,
        price
    ):

        return price * 1.5
```

---

# 15. Reservation Service

---

# services/reservation_service.py

```python
class ReservationService:


    def book_room(
        self,
        customer,
        room,
        days
    ):


        room.book()


        print(
            "Room Booked"
        )


        return {

            "customer":customer.name,

            "room":room.room_number,

            "days":days

        }
```

---

# 16. Main Application

---

# main.py

```python
from factories.room_factory import RoomFactory

from models.customer import Customer

from services.reservation_service import ReservationService



room = RoomFactory.create_room(

    "single",

    101,

    2000

)



customer = Customer(

    1,

    "Alex"

)



service = ReservationService()



booking = service.book_room(

    customer,

    room,

    3

)



print(booking)



print(

room.calculate_price(3)

)
```

---

# Output

```
Room Booked

{
customer:'Alex',
room:101,
days:3
}

6000
```

---

# 17. Testing

## tests/test_room.py

```python
import unittest

from models.single_room import SingleRoom



class TestRoom(unittest.TestCase):


    def test_booking(self):


        room = SingleRoom(

            101,

            2000

        )


        room.book()


        self.assertFalse(

            room.is_available()

        )


if __name__=="__main__":

    unittest.main()
```

---

# 18. Execution Flow

```
main.py

 |

Room Factory

 |

Room Object

 |

Reservation Service

 |

Pricing Strategy

 |

Payment
```

---

# 19. Future Enhancements

Add:

```
Database Integration

Online Booking Portal

Payment Gateway

Customer Login

Room Recommendation

Mobile Application API
```

---

# 20. Learning Outcome

After completing this project:

You understand:

✅ Complex Object Relationships

✅ Composition

✅ Inheritance

✅ Polymorphism

✅ Factory Pattern

✅ Strategy Pattern

✅ State Management

✅ Real-world Booking System Design

---

# Project Completion Level

```
Python OOP              ⭐⭐⭐⭐⭐

Relationships           ⭐⭐⭐⭐⭐

Business Logic          ⭐⭐⭐⭐⭐

Design Patterns         ⭐⭐⭐⭐

Architecture            ⭐⭐⭐⭐⭐
```

---

# Next Project

```
06_Online_Course_Platform.md
```

Focus:

- Student Management
- Course Enrollment
- Instructor System
- Payment Subscription
- Learning Progress Tracking
- Plugin Architecture
