from dataclasses import dataclass
from datetime import datetime
@dataclass
class Record:
    record_id: int
    person_id: int
    resource_id: int
    units: int
    created_at: datetime
    status: str = 'ACTIVE'
