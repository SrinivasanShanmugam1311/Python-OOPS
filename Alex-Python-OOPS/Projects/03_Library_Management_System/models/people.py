from dataclasses import dataclass
@dataclass(frozen=True)
class Member:
    """One person participating in the library management workflow."""
    person_id: int
    name: str
    email: str
