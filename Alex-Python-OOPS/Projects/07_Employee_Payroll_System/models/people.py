from dataclasses import dataclass
@dataclass(frozen=True)
class Employee:
    """One person participating in the employee payroll workflow."""
    person_id: int
    name: str
    email: str
