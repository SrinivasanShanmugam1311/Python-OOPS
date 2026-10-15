from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount): pass
class UPIPayment(PaymentMethod):
    def pay(self, amount): return f'SIMULATED-UPI-{amount}'
class CardPayment(PaymentMethod):
    def pay(self, amount): return f'SIMULATED-CARD-{amount}'
