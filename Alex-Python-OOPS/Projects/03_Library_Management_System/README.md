# Project 03 – Library Management

**Level:** Intermediate Python OOPS simulation (in-memory, not production-ready).

## Purpose
Member borrows and returns a book. Learn to represent real-world entities using multiple classes and a service layer.

## Mental model
```text
User -> main.py -> LibraryService -> Member
                               -> Book (abstract)
                                  |-- PrintedBook
                                  `-- ReferenceBook
                               -> Record
                  -> DomainError subclasses
```

## OOPS concepts
- **Class/object:** Each Member and Book is a distinct object.
- **Encapsulation:** `Book` keeps `__capacity` private; `allocate()` and `release()` validate changes.
- **Abstraction:** `Book` declares the `description()` interface.
- **Inheritance:** `PrintedBook` and `ReferenceBook` extend `Book`.
- **Polymorphism:** Each subclass implements `description()` differently.
- **Composition and coordination:** `LibraryService` manages people, resources and records.
- **Dataclasses:** Person and Record have automatically generated initializers.
- **Exceptions:** Specific errors explain why operations fail.
- **Separation of concerns:** `main.py` only demonstrates the application; business logic is in `services/`.

## Core operations
1. `register_person(name, email)` — create a member.
2. `create_resource(name, capacity, premium=False)` — create a book.
3. `borrow(person_id, resource_id, units)` — allocate capacity and create a record.
4. `return_item(record_id)` — close record and restore capacity.
5. `get_capacity(resource_id)` — read remaining capacity.
6. `history(person_id)` — view the person's records.

## Simulation
```text
Starting copies: 5
borrow(units=2) -> remaining: 3
return_item() -> remaining: 5
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
This is a **simplified OOPS exercise**, not a complete library management application.
The shared capacity model is deliberately educational: actual domain rules differ and would need
dedicated implementations (for example: bank ledgers, medical records, fines, dates, payroll taxes,
fare rules). Data disappears when the process exits; there is no database, login, REST API,
concurrency control or external integration. A production version would require domain-specific
rules, persistence, security, logging, tests for concurrent operations, and integration tests.

## Learning path
Classes -> Objects -> Encapsulation -> Inheritance -> Polymorphism -> Abstraction
-> Dataclasses -> Service layer -> Exceptions -> Unit testing -> Real architecture
