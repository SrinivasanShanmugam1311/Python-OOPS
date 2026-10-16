class DomainError(Exception):
    """Parent for all Employee Payroll domain errors."""
class NotFoundError(DomainError): pass
class InvalidAmountError(DomainError): pass
class InsufficientCapacityError(DomainError): pass
class DuplicateActionError(DomainError): pass
class InvalidStateError(DomainError): pass
