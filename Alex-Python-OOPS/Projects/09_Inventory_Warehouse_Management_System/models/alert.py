from abc import ABC, abstractmethod
class StockAlert(ABC):
    @abstractmethod
    def notify(self, message):
        """Every alert channel must implement this method."""
class ConsoleAlert(StockAlert):
    def notify(self, message):
        return f'CONSOLE ALERT: {message}'
class EmailAlert(StockAlert):
    def notify(self, message):
        return f'SIMULATED EMAIL ALERT: {message}'
