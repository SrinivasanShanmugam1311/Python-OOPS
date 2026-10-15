# Python Object-Oriented Programming (OOP)

# Module 09 – SOLID Principles & Design Patterns

# Module_09_Code_Examples_Part_2.md

**Level:** Advanced

**Topics Covered**

- Singleton Pattern
- Factory Method
- Abstract Factory
- Builder Pattern
- Strategy Pattern
- Observer Pattern
- Adapter Pattern
- Facade Pattern
- Template Method

---

# 1. Singleton Pattern

## Concept

Singleton ensures:

```
Only One Object

↓

Throughout Application
```

Common Uses:

- Logger
- Configuration Manager
- Database Connection

---

# Example: Logger Singleton

```python
class Logger:


    _instance = None


    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

        return cls._instance



logger1 = Logger()

logger2 = Logger()


print(logger1 is logger2)
```

Output

```
True
```

Both variables point to the same object.

---

# Real Example

```python
class ApplicationConfig:


    _instance = None


    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.settings = {}


        return cls._instance



config1 = ApplicationConfig()

config1.settings["theme"] = "dark"


config2 = ApplicationConfig()


print(config2.settings)
```

Output

```
{'theme':'dark'}
```

---

# 2. Factory Method Pattern

## Concept

Factory creates objects without exposing creation logic.

Instead of:

```python
Car()

Bike()
```

Use:

```
VehicleFactory

↓

Creates Object
```

---

# Example: Vehicle Factory

```python
from abc import ABC, abstractmethod



class Vehicle(ABC):


    @abstractmethod
    def drive(self):

        pass



class Car(Vehicle):


    def drive(self):

        print("Driving Car")



class Bike(Vehicle):


    def drive(self):

        print("Driving Bike")



class VehicleFactory:


    @staticmethod
    def create_vehicle(vehicle_type):

        if vehicle_type == "car":

            return Car()


        elif vehicle_type == "bike":

            return Bike()


car = VehicleFactory.create_vehicle("car")

car.drive()


bike = VehicleFactory.create_vehicle("bike")

bike.drive()
```

Output

```
Driving Car

Driving Bike
```

---

# Benefits

- Centralized object creation
- Easy extension
- Cleaner client code

---

# 3. Abstract Factory Pattern

## Concept

Creates families of related objects.

Example:

GUI System

```
Windows Factory

↓

Button

Menu


Mac Factory

↓

Button

Menu
```

---

# Example

```python
from abc import ABC, abstractmethod



class Button(ABC):


    @abstractmethod
    def click(self):

        pass



class WindowsButton(Button):


    def click(self):

        print("Windows Button")



class MacButton(Button):


    def click(self):

        print("Mac Button")



class GUIFactory(ABC):


    @abstractmethod
    def create_button(self):

        pass



class WindowsFactory(GUIFactory):


    def create_button(self):

        return WindowsButton()



class MacFactory(GUIFactory):


    def create_button(self):

        return MacButton()



factory = WindowsFactory()


button = factory.create_button()


button.click()
```

---

# 4. Builder Pattern

## Concept

Creates complex objects step-by-step.

Example:

Computer

```
CPU

RAM

Storage

GPU
```

---

# Example

```python
class Computer:


    def __init__(
        self,
        cpu,
        ram,
        storage
    ):

        self.cpu = cpu

        self.ram = ram

        self.storage = storage



class ComputerBuilder:


    def __init__(self):

        self.cpu = None

        self.ram = None

        self.storage = None



    def set_cpu(self,cpu):

        self.cpu = cpu

        return self



    def set_ram(self,ram):

        self.ram = ram

        return self



    def set_storage(self,storage):

        self.storage = storage

        return self



    def build(self):

        return Computer(
            self.cpu,
            self.ram,
            self.storage
        )



computer = (
    ComputerBuilder()
    .set_cpu("Intel")
    .set_ram("16GB")
    .set_storage("1TB")
    .build()
)


print(computer.cpu)
```

Output

```
Intel
```

---

# 5. Strategy Pattern

## Concept

Change behavior dynamically.

Example:

Payment Methods

```
Payment

↓

UPI Strategy

Card Strategy

Wallet Strategy
```

---

# Example

```python
from abc import ABC, abstractmethod



class PaymentStrategy(ABC):


    @abstractmethod
    def pay(self,amount):

        pass



class UPI(PaymentStrategy):


    def pay(self,amount):

        print(
            f"UPI Payment {amount}"
        )



class Card(PaymentStrategy):


    def pay(self,amount):

        print(
            f"Card Payment {amount}"
        )



class ShoppingCart:


    def __init__(self,strategy):

        self.strategy = strategy



    def checkout(self,amount):

        self.strategy.pay(amount)



cart = ShoppingCart(
    UPI()
)


cart.checkout(1000)
```

Output

```
UPI Payment 1000
```

---

# 6. Observer Pattern

## Concept

One object changes.

Many objects get notified.

Example:

```
YouTube Channel

↓

Subscribers
```

---

# Example

```python
class Subscriber:


    def __init__(self,name):

        self.name = name



    def update(self,message):

        print(
            self.name,
            message
        )



class Channel:


    def __init__(self):

        self.subscribers = []



    def subscribe(self,subscriber):

        self.subscribers.append(subscriber)



    def notify(self,message):

        for subscriber in self.subscribers:

            subscriber.update(message)



channel = Channel()


channel.subscribe(
    Subscriber("Alex")
)

channel.subscribe(
    Subscriber("John")
)


channel.notify(
    "New Video Uploaded"
)
```

Output

```
Alex New Video Uploaded

John New Video Uploaded
```

---

# 7. Adapter Pattern

## Concept

Allows incompatible classes to work together.

Example:

```
Old System

↓

Adapter

↓

New System
```

---

# Example

```python
class OldPrinter:


    def old_print(self):

        print("Old Printer")



class PrinterAdapter:


    def __init__(self,printer):

        self.printer = printer



    def print(self):

        self.printer.old_print()



printer = PrinterAdapter(
    OldPrinter()
)


printer.print()
```

---

# 8. Facade Pattern

## Concept

Provides a simple interface to a complex system.

---

Example:

Online Shopping

Behind scenes:

```
Inventory

Payment

Shipping

Email
```

User only calls:

```
place_order()
```

---

# Example

```python
class Inventory:


    def check(self):

        print("Inventory Checked")



class Payment:


    def pay(self):

        print("Payment Completed")



class Shipping:


    def ship(self):

        print("Product Shipped")



class OrderFacade:


    def place_order(self):

        Inventory().check()

        Payment().pay()

        Shipping().ship()



order = OrderFacade()


order.place_order()
```

Output

```
Inventory Checked

Payment Completed

Product Shipped
```

---

# 9. Template Method Pattern

## Concept

Defines algorithm structure.

Child classes customize steps.

---

# Example

```python
from abc import ABC, abstractmethod



class DataProcessor(ABC):


    def process(self):

        self.read()

        self.transform()

        self.save()



    @abstractmethod
    def read(self):

        pass



    @abstractmethod
    def transform(self):

        pass



    def save(self):

        print("Saving Data")



class CSVProcessor(DataProcessor):


    def read(self):

        print("Reading CSV")


    def transform(self):

        print("Transform CSV")



processor = CSVProcessor()


processor.process()
```

Output

```
Reading CSV

Transform CSV

Saving Data
```

---

# Pattern Selection Guide

| Problem | Pattern |
|-|-|
| One object only | Singleton |
| Object creation complexity | Factory |
| Family of objects | Abstract Factory |
| Complex object creation | Builder |
| Change behavior dynamically | Strategy |
| Notify many objects | Observer |
| Connect incompatible systems | Adapter |
| Simplify complex subsystem | Facade |
| Common workflow | Template Method |

---

# Mini Architecture Example

## E-Commerce Payment Engine

```
Order

↓

Payment Strategy

↓

UPI

Credit Card

Wallet


↓

Payment Factory


↓

Notification Observer


↓

Email

SMS
```

Uses:

- SRP
- OCP
- DIP
- Strategy
- Factory
- Observer

---

# Final Module Outcome

After Module 09:

You can:

✅ Design scalable Python applications.

✅ Apply SOLID principles.

✅ Choose correct design patterns.

✅ Build enterprise-level OOP systems.

✅ Understand professional software architecture.

---

# Next

## Module 10 – Real World OOP Project Architecture

Topics:

- Layered Architecture
- Service Layer
- Repository Pattern
- Dependency Injection
- Project Structure
- Testing OOP Applications
- Final Capstone Project
