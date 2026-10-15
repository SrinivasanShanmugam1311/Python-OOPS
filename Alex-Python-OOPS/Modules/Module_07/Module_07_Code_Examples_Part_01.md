# Python Object-Oriented Programming (OOP)

# Module 07 – Abstract Classes, Interfaces & Type Hints

# Module_07_Code_Examples.md (Part 1)

**Level:** Intermediate → Advanced

---

# ABC (Abstract Base Class)

## Problem Without ABC

```python
class CreditCard:

    def pay(self):
        print("Credit Card Payment")


class UPI:
    pass


credit = CreditCard()
credit.pay()

upi = UPI()

# Runtime Error
# upi.pay()
```

### Problem

```
Developer forgot to implement pay().

Error occurs only while running the program.
```

---

# Solution

Use an Abstract Base Class.

---

# Import ABC Module

```python
from abc import ABC
from abc import abstractmethod
```

---

# Example 1 – Basic Abstract Class

```python
from abc import ABC
from abc import abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


dog = Dog()

dog.sound()
```

### Output

```
Dog Barks
```

---

# Trying to Create an Abstract Object

```python
animal = Animal()
```

Output

```
TypeError:

Can't instantiate abstract class Animal
with abstract method sound
```

---

# Why?

Python prevents incomplete objects.

---

# Example 2 – Multiple Child Classes

```python
from abc import ABC
from abc import abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, l, b):

        self.l = l
        self.b = b

    def area(self):

        return self.l * self.b


class Circle(Shape):

    def __init__(self, r):

        self.r = r

    def area(self):

        return 3.14 * self.r * self.r


rectangle = Rectangle(10,5)

circle = Circle(7)

print(rectangle.area())

print(circle.area())
```

Output

```
50

153.86
```

---

# Example 3 – Employee System

```python
from abc import ABC
from abc import abstractmethod


class Employee(ABC):

    @abstractmethod
    def salary(self):
        pass


class Manager(Employee):

    def salary(self):
        return 80000


class Developer(Employee):

    def salary(self):
        return 60000


employees = [

    Manager(),

    Developer()

]

for employee in employees:

    print(employee.salary())
```

Output

```
80000

60000
```

---

# Example 4 – Payment Framework

```python
from abc import ABC
from abc import abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):

        print(
            f"Credit Card : ₹{amount}"
        )


class UPI(Payment):

    def pay(self, amount):

        print(
            f"UPI : ₹{amount}"
        )


class Wallet(Payment):

    def pay(self, amount):

        print(
            f"Wallet : ₹{amount}"
        )


payments = [

    CreditCard(),

    UPI(),

    Wallet()

]

for payment in payments:

    payment.pay(1000)
```

Output

```
Credit Card : ₹1000

UPI : ₹1000

Wallet : ₹1000
```

---

# Example 5 – Bank Accounts

```python
from abc import ABC
from abc import abstractmethod


class Account(ABC):

    @abstractmethod
    def interest(self):
        pass


class Savings(Account):

    def interest(self):

        print("6% Interest")


class Current(Account):

    def interest(self):

        print("0% Interest")


Savings().interest()

Current().interest()
```

---

# Example 6 – File Reader

```python
from abc import ABC
from abc import abstractmethod


class FileReader(ABC):

    @abstractmethod
    def read(self):
        pass


class PDFReader(FileReader):

    def read(self):

        print("Reading PDF")


class CSVReader(FileReader):

    def read(self):

        print("Reading CSV")


PDFReader().read()

CSVReader().read()
```

---

# Example 7 – Notification System

```python
from abc import ABC
from abc import abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class Email(Notification):

    def send(self, message):

        print("Email :", message)


class SMS(Notification):

    def send(self, message):

        print("SMS :", message)


Email().send("Welcome")

SMS().send("OTP")
```

Output

```
Email : Welcome

SMS : OTP
```

---

# Abstract Class with Normal Methods

An Abstract Class can also contain implemented methods.

```python
from abc import ABC
from abc import abstractmethod


class Animal(ABC):

    def sleep(self):

        print("Sleeping...")

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):

        print("Bark")


dog = Dog()

dog.sound()

dog.sleep()
```

Output

```
Bark

Sleeping...
```

---

# Rules of ABC

✅ Cannot create object.

✅ May contain normal methods.

✅ May contain abstract methods.

✅ Child classes must implement all abstract methods.

---

# Where Are ABCs Used?

- Payment Gateways
- Authentication Systems
- Database Drivers
- Machine Learning Models
- Logging Frameworks
- Plugin Systems
- Game Engines
- Report Generators

---

# Best Practices

✅ Keep abstract classes focused.

✅ Declare only mandatory methods.

✅ Provide reusable methods when appropriate.

✅ Use ABC to define contracts.

---

# Common Mistakes

❌ Creating objects of abstract classes.

❌ Forgetting to implement abstract methods.

❌ Creating huge abstract classes with unrelated methods.

❌ Using ABC where a simple class is enough.

---

# Interview Questions

### Basic

- What is an Abstract Class?
- Why can't we create an object of an ABC?
- What is `@abstractmethod`?

### Intermediate

- Difference between ABC and normal class?
- Can an ABC have implemented methods?
- Why use ABC in large projects?

### Advanced

- Design a Payment Framework using ABC.
- Explain the advantages of ABC over runtime checking.
- When should you avoid using an Abstract Base Class?

---

# Next Part

**Module_07_Code_Examples.md (Part 2)**

Topics:

- Interface Concepts
- Protocols (`typing.Protocol`)
- Type Hints
- Generic Programming (`TypeVar`)
- Static Type Checking
- Plugin Architecture
- Authentication Framework
