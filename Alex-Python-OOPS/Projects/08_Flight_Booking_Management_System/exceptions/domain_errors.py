class DomainError(Exception):
    """Parent for all Flight Booking domain errors."""
class NotFoundError(DomainError): pass
class InvalidAmountError(DomainError): pass
class InsufficientCapacityError(DomainError): pass
class DuplicateActionError(DomainError): pass
class InvalidStateError(DomainError): pass
