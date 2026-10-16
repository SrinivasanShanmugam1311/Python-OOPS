from dataclasses import dataclass
@dataclass(frozen=True)
class Learner:
    """One person participating in the online course platform workflow."""
    person_id: int
    name: str
    email: str
