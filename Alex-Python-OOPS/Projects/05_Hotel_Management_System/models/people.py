from dataclasses import dataclass
@dataclass(frozen=True)
class Guest:
    """One person participating in the hotel management workflow."""
    person_id: int
    name: str
    email: str
