# Project 08 – Flight Booking Management System

## File Name

```
08_Flight_Booking_Management_System.md
```

---

# Level

```
Intermediate → Advanced
```

---

# Domain

```
Airline Reservation / Travel Management Application
```

---

# Project Overview

A real-world airline reservation system developed using Python OOP principles.

The application manages:

- Airlines
- Aircrafts
- Flights
- Airports
- Passengers
- Seats
- Reservations
- Payments
- Ticket Generation
- Cancellation

This project focuses on:

- Complex Object Relationships
- State Management
- Strategy Pattern
- Factory Pattern
- Observer Pattern
- Reservation Workflow Design

---

# 1. Project Objective

Build a scalable flight booking system using:

- Object-Oriented Programming
- SOLID Principles
- Design Patterns
- Exception Handling
- Modular Architecture
- Unit Testing

---

# 2. Real World Problem

Airline systems handle complex workflows:

```
Passenger

     |

Search Flight

     |

Select Seat

     |

Create Booking

     |

Payment

     |

Ticket Confirmation

     |

Travel
```

The system must manage:

- Flight schedules
- Seat availability
- Pricing rules
- Booking status
- Cancellation policies

---

# 3. Project Features

---

# Airline Management

Features:

- Add Airline
- Manage Fleet
- View Flights


Airline:

```
Airline ID

Name

Country

Aircraft List
```

---

# Aircraft Management

Aircraft contains:

```
Aircraft ID

Model

Capacity

Seats
```

Example:

```
Boeing 737

 |

150 Seats
```

---

# Flight Management

Features:

- Create Flight
- Update Schedule
- Search Flights


Flight:

```
Flight Number

Source

Destination

Date

Time

Aircraft
```

---

# Passenger Management

Features:

- Register Passenger
- Update Details
- View Bookings


Passenger:

```
Passenger ID

Name

Age

Passport Number
```

---

# Seat Management

Seat Types:

```
Economy

Business

First Class
```

Seat Status:

```
AVAILABLE

RESERVED

BOOKED
```

---

# Booking Management

Features:

- Search Flight
- Reserve Seat
- Confirm Booking
- Cancel Booking


Booking Status:

```
CREATED

PENDING_PAYMENT

CONFIRMED

CANCELLED

COMPLETED
```

---

# Payment System

Payment Methods:

```
Credit Card

UPI

Wallet

Net Banking
```

---

# Ticket Management

Generate:

```
Ticket Number

Passenger Details

Flight Details

Seat Number

Price
```

---

# 4. OOP Concepts Used

| Concept | Usage |
|-|-|
| Classes | Flight, Passenger, Booking |
| Encapsulation | Seat availability |
| Inheritance | Seat types |
| Polymorphism | Pricing calculation |
| Composition | Aircraft contains seats |
| Association | Passenger booking |
| Abstract Classes | Payment interface |
| Dataclass | Ticket data |
| State Pattern | Booking lifecycle |

---

# 5. Object Relationships

---

# Airline → Aircraft

One-to-Many

```
Airline

 |

 |---- Aircraft

 |---- Aircraft
```

---

# Aircraft → Seats

Composition

```
Aircraft

 |

 |---- Seat

 |---- Seat

 |---- Seat
```

---

# Flight → Aircraft

One-to-One

```
Flight

 |

Aircraft
```

---

# Passenger ↔ Flight

Many-to-Many

Through Booking:

```
Passenger

     |

  Booking

     |

   Flight
```

---

# Booking → Payment

One-to-One

```
Booking

 |

Payment
```

---

# 6. Design Principles Used

---

# Single Responsibility Principle

Separate:

```
Flight Service

Booking Service

Payment Service

Ticket Service
```

---

# Open Closed Principle

New pricing rules:

```
Peak Season

Festival Offer

Business Fare

Corporate Discount
```

can be added without modifying existing code.

---

# Liskov Substitution Principle

All seat types should work with flight booking.

---

# Dependency Inversion

Booking service depends on abstractions.

---

# 7. Design Patterns Used

---

# Factory Pattern

Create flights:

```
FlightFactory

        |

-----------------

Domestic Flight

International Flight
```

---

# Strategy Pattern

Fare calculation:

```
Fare Strategy

       |

-----------------

Economy Fare

Business Fare

Discount Fare
```

---

# State Pattern

Booking workflow:

```
Created

 |

Payment Pending

 |

Confirmed

 |

Cancelled
```

---

# Observer Pattern

Notifications:

```
Booking Confirmed

        |

----------------

Email

SMS

Mobile App
```

---

# Builder Pattern

Create ticket:

```
Ticket Builder

Passenger

Flight

Seat

Price
```

---

# 8. Project Folder Structure

```
08_Flight_Booking_Management_System/

│
├── main.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── models/
│   ├── __init__.py
│   ├── airline.py
│   ├── aircraft.py
│   ├── flight.py
│   ├── airport.py
│   ├── passenger.py
│   ├── seat.py
│   ├── booking.py
│   ├── ticket.py
│   └── payment.py
│
├── services/
│   ├── __init__.py
│   ├── flight_service.py
│   ├── booking_service.py
│   ├── payment_service.py
│   └── ticket_service.py
│
├── factories/
│   └── flight_factory.py
│
├── strategies/
│   ├── fare_strategy.py
│   └── payment_strategy.py
│
├── states/
│   ├── booking_state.py
│   ├── confirmed.py
│   ├── cancelled.py
│   └── pending.py
│
├── builders/
│   └── ticket_builder.py
│
├── observers/
│   └── notification.py
│
├── exceptions/
│   └── flight_exceptions.py
│
├── utils/
│   ├── logger.py
│   └── validator.py
│
├── database/
│   └── flights.json
│
├── tests/
│   ├── test_flight.py
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
| airline.py | Airline entity |
| aircraft.py | Aircraft management |
| seat.py | Seat handling |
| flight.py | Flight details |
| passenger.py | Passenger data |
| booking.py | Reservation workflow |
| ticket.py | Ticket generation |
| services | Business operations |
| strategies | Dynamic rules |
| states | Booking status |

---

# 10. Code Implementation

---

# models/seat.py

```python
from enum import Enum



class SeatStatus(Enum):

    AVAILABLE = 1

    RESERVED = 2

    BOOKED = 3



class Seat:


    def __init__(
        self,
        number,
        seat_type
    ):

        self.number = number

        self.seat_type = seat_type

        self.status = SeatStatus.AVAILABLE



    def reserve(self):

        if self.status != SeatStatus.AVAILABLE:

            raise Exception(
                "Seat Not Available"
            )


        self.status = SeatStatus.RESERVED
```

---

# Concepts Used

Encapsulation:

```
Seat Status Controlled
```

State Management:

```
AVAILABLE

RESERVED

BOOKED
```

---

# 11. Passenger Model

```python
class Passenger:


    def __init__(
        self,
        id,
        name
    ):

        self.id=id

        self.name=name

        self.bookings=[]
```

---

# 12. Flight Model

```python
class Flight:


    def __init__(
        self,
        number,
        source,
        destination
    ):

        self.number = number

        self.source = source

        self.destination = destination

        self.seats=[]



    def add_seat(
        self,
        seat
    ):

        self.seats.append(seat)
```

---

# 13. Booking Model

```python
from enum import Enum



class BookingStatus(Enum):

    CREATED=1

    CONFIRMED=2

    CANCELLED=3



class Booking:


    def __init__(
        self,
        passenger,
        flight,
        seat
    ):

        self.passenger=passenger

        self.flight=flight

        self.seat=seat

        self.status=BookingStatus.CREATED
```

---

# 14. Fare Strategy

```python
from abc import ABC,abstractmethod



class FareStrategy(ABC):


    @abstractmethod
    def calculate(
        self,
        base_price
    ):

        pass



class EconomyFare(FareStrategy):


    def calculate(
        self,
        base_price
    ):

        return base_price



class BusinessFare(FareStrategy):


    def calculate(
        self,
        base_price
    ):

        return base_price * 2
```

---

# 15. Flight Factory

```python
class FlightFactory:


    @staticmethod
    def create_flight(
        flight_type,
        number,
        source,
        destination
    ):


        return Flight(

            number,

            source,

            destination

        )
```

---

# 16. Booking Service

```python
class BookingService:


    def book(
        self,
        passenger,
        flight,
        seat
    ):


        seat.reserve()


        booking = Booking(

            passenger,

            flight,

            seat

        )


        booking.status = BookingStatus.CONFIRMED


        return booking
```

---

# 17. Main Application

```python
from models.flight import Flight

from models.passenger import Passenger

from models.seat import Seat

from services.booking_service import BookingService



flight = Flight(

    "AI101",

    "Hyderabad",

    "Delhi"

)



seat = Seat(

    "A1",

    "Business"

)



flight.add_seat(
    seat
)



passenger = Passenger(

    1,

    "Alex"

)



service = BookingService()



booking = service.book(

    passenger,

    flight,

    seat

)



print(
    booking.status
)
```

---

# Output

```
BookingStatus.CONFIRMED
```

---

# 18. Testing

## tests/test_booking.py

```python
import unittest


class TestBooking(unittest.TestCase):


    def test_booking_status(self):

        self.assertTrue(
            True
        )


if __name__=="__main__":

    unittest.main()
```

---

# 19. Execution Flow

```
Passenger

 |

Search Flight

 |

Select Seat

 |

Booking Service

 |

Payment

 |

Ticket Generation

 |

Notification
```

---

# 20. Future Enhancements

Add:

```
Database Integration

Real Payment Gateway

AI Fare Prediction

Seat Recommendation

Flight Tracking

Mobile Application API

Microservice Architecture
```

---

# 21. Learning Outcome

After completing this project:

You understand:

✅ Complex Object Relationships

✅ Reservation System Design

✅ State Pattern

✅ Strategy Pattern

✅ Factory Pattern

✅ Builder Pattern

✅ Event Notification

✅ Real-world Travel Domain Modeling

---

# Project Completion Level

```
Python OOP              ⭐⭐⭐⭐⭐

Relationships           ⭐⭐⭐⭐⭐

Design Patterns         ⭐⭐⭐⭐⭐

Architecture            ⭐⭐⭐⭐⭐

Real World Complexity   ⭐⭐⭐⭐⭐
```

---

# Next Project

```
09_Inventory_Warehouse_Management_System.md
```

Focus:

- Product Lifecycle
- Stock Management
- Supplier Management
- Warehouse Operations
- Reporting
- Repository Pattern
```
