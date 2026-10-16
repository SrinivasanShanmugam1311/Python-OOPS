from abc import ABC, abstractmethod
from exceptions.domain_errors import InvalidAmountError, InsufficientCapacityError
class Room(ABC):
    """Base class: owns capacity and validates all changes."""
    def __init__(self, resource_id: int, name: str, capacity: int):
        if capacity < 0: raise InvalidAmountError('Initial capacity cannot be negative')
        self.resource_id = resource_id
        self.name = name
        self.__capacity = capacity  # Encapsulation: do not modify outside the class.
    @property
    def capacity(self): return self.__capacity
    def allocate(self, units):
        if units <= 0: raise InvalidAmountError('Units must be positive')
        if units > self.__capacity: raise InsufficientCapacityError('Not enough capacity')
        self.__capacity -= units
    def release(self, units):
        if units <= 0: raise InvalidAmountError('Units must be positive')
        self.__capacity += units
    @abstractmethod
    def description(self): pass
class StandardRoom(Room):
    def description(self): return 'StandardRoom: ' + self.name
class DeluxeRoom(Room):
    def description(self): return 'DeluxeRoom: ' + self.name
