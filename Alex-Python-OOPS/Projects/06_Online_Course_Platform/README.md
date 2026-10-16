# Project 06 – Online Course Platform

**Level:** Intermediate Python OOPS simulation (in-memory, not production-ready).

## Purpose
Learner enrolls in a course. Learn to represent real-world entities using multiple classes and a service layer.

## Mental model
```text
User -> main.py -> CourseService -> Learner
                               -> Course (abstract)
                                  |-- FreeCourse
                                  `-- PaidCourse
                               -> Record
                  -> DomainError subclasses
```

## OOPS concepts
- **Class/object:** Each Learner and Course is a distinct object.
- **Encapsulation:** `Course` keeps `__capacity` private; `allocate()` and `release()` validate changes.
- **Abstraction:** `Course` declares the `description()` interface.
- **Inheritance:** `FreeCourse` and `PaidCourse` extend `Course`.
- **Polymorphism:** Each subclass implements `description()` differently.
- **Composition and coordination:** `CourseService` manages people, resources and records.
- **Dataclasses:** Person and Record have automatically generated initializers.
- **Exceptions:** Specific errors explain why operations fail.
- **Separation of concerns:** `main.py` only demonstrates the application; business logic is in `services/`.

## Core operations
1. `register_person(name, email)` — create a learner.
2. `create_resource(name, capacity, premium=False)` — create a course.
3. `enroll(person_id, resource_id, units)` — allocate capacity and create a record.
4. `unenroll(record_id)` — close record and restore capacity.
5. `get_capacity(resource_id)` — read remaining capacity.
6. `history(person_id)` — view the person's records.

## Simulation
```text
Starting seats: 5
enroll(units=2) -> remaining: 3
unenroll() -> remaining: 5
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
This is a **simplified OOPS exercise**, not a complete online course platform application.
The shared capacity model is deliberately educational: actual domain rules differ and would need
dedicated implementations (for example: bank ledgers, medical records, fines, dates, payroll taxes,
fare rules). Data disappears when the process exits; there is no database, login, REST API,
concurrency control or external integration. A production version would require domain-specific
rules, persistence, security, logging, tests for concurrent operations, and integration tests.

## Learning path
Classes -> Objects -> Encapsulation -> Inheritance -> Polymorphism -> Abstraction
-> Dataclasses -> Service layer -> Exceptions -> Unit testing -> Real architecture
