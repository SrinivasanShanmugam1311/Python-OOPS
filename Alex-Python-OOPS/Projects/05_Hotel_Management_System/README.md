# Project 05 – Hotel Management

**Level:** Intermediate Python OOPS simulation (in-memory, not production-ready).

## Purpose
Guest reserves and checks out of a room. Learn to represent real-world entities using multiple classes and a service layer.

## Mental model
```text
User -> main.py -> HotelService -> Guest
                               -> Room (abstract)
                                  |-- StandardRoom
                                  `-- DeluxeRoom
                               -> Record
                  -> DomainError subclasses
```

## OOPS concepts
- **Class/object:** Each Guest and Room is a distinct object.
- **Encapsulation:** `Room` keeps `__capacity` private; `allocate()` and `release()` validate changes.
- **Abstraction:** `Room` declares the `description()` interface.
- **Inheritance:** `StandardRoom` and `DeluxeRoom` extend `Room`.
- **Polymorphism:** Each subclass implements `description()` differently.
- **Composition and coordination:** `HotelService` manages people, resources and records.
- **Dataclasses:** Person and Record have automatically generated initializers.
- **Exceptions:** Specific errors explain why operations fail.
- **Separation of concerns:** `main.py` only demonstrates the application; business logic is in `services/`.

## Core operations
1. `register_person(name, email)` — create a guest.
2. `create_resource(name, capacity, premium=False)` — create a room.
3. `reserve(person_id, resource_id, units)` — allocate capacity and create a record.
4. `checkout(record_id)` — close record and restore capacity.
5. `get_capacity(resource_id)` — read remaining capacity.
6. `history(person_id)` — view the person's records.

## Simulation
```text
Starting availability: 5
reserve(units=2) -> remaining: 3
checkout() -> remaining: 5
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
This is a **simplified OOPS exercise**, not a complete hotel management application.
The shared capacity model is deliberately educational: actual domain rules differ and would need
dedicated implementations (for example: bank ledgers, medical records, fines, dates, payroll taxes,
fare rules). Data disappears when the process exits; there is no database, login, REST API,
concurrency control or external integration. A production version would require domain-specific
rules, persistence, security, logging, tests for concurrent operations, and integration tests.

## Learning path
Classes -> Objects -> Encapsulation -> Inheritance -> Polymorphism -> Abstraction
-> Dataclasses -> Service layer -> Exceptions -> Unit testing -> Real architecture
