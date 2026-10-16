from dataclasses import dataclass
@dataclass(frozen=True)
class Passenger:
    """One person participating in the flight booking workflow."""
    person_id: int
    name: str
    email: str
