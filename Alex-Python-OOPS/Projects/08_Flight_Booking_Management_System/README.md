# Project 08 – Flight Booking

**Level:** Intermediate Python OOPS simulation (in-memory, not production-ready).

## Purpose
Passenger books and cancels a flight ticket. Learn to represent real-world entities using multiple classes and a service layer.

## Mental model
```text
User -> main.py -> FlightService -> Passenger
                               -> Flight (abstract)
                                  |-- DomesticFlight
                                  `-- InternationalFlight
                               -> Record
                  -> DomainError subclasses
```

## OOPS concepts
- **Class/object:** Each Passenger and Flight is a distinct object.
- **Encapsulation:** `Flight` keeps `__capacity` private; `allocate()` and `release()` validate changes.
- **Abstraction:** `Flight` declares the `description()` interface.
- **Inheritance:** `DomesticFlight` and `InternationalFlight` extend `Flight`.
- **Polymorphism:** Each subclass implements `description()` differently.
- **Composition and coordination:** `FlightService` manages people, resources and records.
- **Dataclasses:** Person and Record have automatically generated initializers.
- **Exceptions:** Specific errors explain why operations fail.
- **Separation of concerns:** `main.py` only demonstrates the application; business logic is in `services/`.

## Core operations
1. `register_person(name, email)` — create a passenger.
2. `create_resource(name, capacity, premium=False)` — create a flight.
3. `book_ticket(person_id, resource_id, units)` — allocate capacity and create a record.
4. `cancel_ticket(record_id)` — close record and restore capacity.
5. `get_capacity(resource_id)` — read remaining capacity.
6. `history(person_id)` — view the person's records.

## Simulation
```text
Starting seats: 5
book_ticket(units=2) -> remaining: 3
cancel_ticket() -> remaining: 5
```

## Run
```bash
python main.py
python -m unittest discover -v
```

## Test coverage
15 automated tests cover creation, IDs, invalid data, subclass behavior, allocation, reversal,
double reversal, insufficient capacity, invalid units, missing records, history and repeated actions.

## Limitations and future work
This is a **simplified OOPS exercise**, not a complete flight booking application.
The shared capacity model is deliberately educational: actual domain rules differ and would need
dedicated implementations (for example: bank ledgers, medical records, fines, dates, payroll taxes,
fare rules). Data disappears when the process exits; there is no database, login, REST API,
concurrency control or external integration. A production version would require domain-specific
rules, persistence, security, logging, tests for concurrent operations, and integration tests.

## Learning path
Classes -> Objects -> Encapsulation -> Inheritance -> Polymorphism -> Abstraction
-> Dataclasses -> Service layer -> Exceptions -> Unit testing -> Real architecture
