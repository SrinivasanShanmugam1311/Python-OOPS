# Project 10 – Real World Application Architecture

**Purpose:** A small task-management example demonstrating layered architecture, interfaces,
repository pattern, dependency injection, and separation of concerns.

```text
main.py (presentation)
   |
TaskService (business rules)
   |
TaskRepository (abstract interface)
   |
InMemoryTaskRepository (concrete implementation)
   |
Task (dataclass domain model)
```

**Why:** `TaskService` depends on an abstract repository interface, so a future SQLite repository
could replace the in-memory one without rewriting business logic.

**Features:** create a task, mark it complete, list tasks, validate empty titles,
reject unknown tasks and duplicate completion.

**Run:** `python main.py` and `python -m unittest discover -v`.

**Tests:** 8 automated tests.

**Limitations:** In-memory, no concurrency or persistence; this is an architectural learning example.
**Next steps:** SQLite repository, logging, FastAPI presentation layer, integration tests.
