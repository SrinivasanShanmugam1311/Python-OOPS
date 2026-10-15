# Python Object-Oriented Programming (OOP)

# Module 07 – Abstract Classes, Interfaces & Type Hints

# Module_07_Code_Examples.md (Part 2)

**Level:** Intermediate → Advanced

---

# Part 2 Overview

In Part 1, we learned **Abstract Base Classes (ABC)**.

Now we will learn:

- Interface Concept
- Protocols
- Type Hints
- Generic Programming
- Static Type Checking
- Plugin Architecture
- Authentication Framework

---

# 1. Interface Concept

## What is an Interface?

An Interface defines **what a class must do**, not **how it does it**.

Example

```
Payment

↓

pay()
```

Every payment method must provide `pay()`.

---

## Java

```java
interface Payment{

    void pay();
}
```

---

## Python

Python has **no `interface` keyword**.

Instead, we use:

- Abstract Base Classes (ABC)
- Protocols

---

## Interface Using ABC

```python
from abc import ABC
from abc import abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class CreditCard(Payment):

    def pay(self):
        print("Credit Card Payment")


class UPI(Payment):

    def pay(self):
        print("UPI Payment")


payments = [
    CreditCard(),
    UPI()
]

for payment in payments:
    payment.pay()
```

Output

```
Credit Card Payment
UPI Payment
```

---

# 2. Protocols

## What is a Protocol?

Protocol checks **behavior**, not inheritance.

If a class has the required methods,
it satisfies the protocol.

Inheritance is **optional**.

---

## Example

```python
from typing import Protocol


class Speaker(Protocol):

    def speak(self):
        ...


class Dog:

    def speak(self):
        print("Dog Barks")


class Robot:

    def speak(self):
        print("Robot Speaking")


def make_sound(obj: Speaker):

    obj.speak()


make_sound(Dog())

make_sound(Robot())
```

Output

```
Dog Barks
Robot Speaking
```

Notice:

```
Dog

↓

NOT inherited from

↓

Speaker
```

Still works.

---

# ABC vs Protocol

| ABC | Protocol |
|------|----------|
| Requires inheritance | No inheritance required |
| Strong contract | Structural contract |
| Runtime enforcement | Mainly static checking |
| Good for frameworks | Good for APIs |

---

# 3. Type Hints

Type Hints improve readability.

---

## Function Type Hints

```python
def add(a: int, b: int) -> int:

    return a + b


print(add(10,20))
```

Output

```
30
```

---

## Variable Type Hints

```python
name: str = "Alex"

age: int = 45

salary: float = 50000.50

active: bool = True

print(name)
```

---

## List Type Hint

```python
numbers: list[int] = [
    10,
    20,
    30
]

print(numbers)
```

---

## Dictionary Type Hint

```python
student: dict[str,int] = {

    "Math":95,

    "Science":90

}

print(student)
```

---

## Optional Type

```python
from typing import Optional


def display(name: Optional[str]):

    print(name)


display("Alex")

display(None)
```

---

# 4. Generic Programming

Generic Programming allows one class
to work with multiple data types.

---

## Without Generics

```
Student Stack

Employee Stack

Integer Stack

Product Stack
```

Many duplicate classes.

---

## With Generics

One reusable class.

---

## Example

```python
from typing import TypeVar
from typing import Generic

T = TypeVar("T")


class Box(Generic[T]):

    def __init__(self, value: T):

        self.value = value

    def show(self):

        print(self.value)


Box[int](100).show()

Box[str]("Python").show()

Box[float](3.14).show()
```

Output

```
100
Python
3.14
```

---

# 5. Static Type Checking

Python itself does not enforce type hints.

Static type checkers examine your code
before execution.

---

## Example

```python
def multiply(a: int, b: int) -> int:

    return a * b


multiply("10",20)
```

Python runs it,
but a static type checker reports:

```
Expected int

Received str
```

Benefits

- Detect errors early.
- Better IDE support.
- Easier maintenance.

---

# Project 1 – Plugin Architecture

Every plugin should implement
`start()` and `stop()`.

```python
from abc import ABC
from abc import abstractmethod


class Plugin(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class AudioPlugin(Plugin):

    def start(self):
        print("Audio Started")

    def stop(self):
        print("Audio Stopped")


class VideoPlugin(Plugin):

    def start(self):
        print("Video Started")

    def stop(self):
        print("Video Stopped")


plugins = [

    AudioPlugin(),

    VideoPlugin()

]

for plugin in plugins:

    plugin.start()

    plugin.stop()
```

---

# Project 2 – Authentication Framework

```python
from abc import ABC
from abc import abstractmethod


class Authentication(ABC):

    @abstractmethod
    def authenticate(self):
        pass


class GoogleLogin(Authentication):

    def authenticate(self):
        print("Google Login")


class FacebookLogin(Authentication):

    def authenticate(self):
        print("Facebook Login")


class EmailLogin(Authentication):

    def authenticate(self):
        print("Email Login")


methods = [

    GoogleLogin(),

    FacebookLogin(),

    EmailLogin()

]

for method in methods:

    method.authenticate()
```

---

# Project 3 – Report Export Framework

```python
from abc import ABC
from abc import abstractmethod


class Exporter(ABC):

    @abstractmethod
    def export(self):
        pass


class PDFExporter(Exporter):

    def export(self):
        print("Export PDF")


class ExcelExporter(Exporter):

    def export(self):
        print("Export Excel")


class CSVExporter(Exporter):

    def export(self):
        print("Export CSV")


reports = [

    PDFExporter(),

    ExcelExporter(),

    CSVExporter()

]

for report in reports:

    report.export()
```

---

# Real-World Applications

These concepts are used in:

- Django
- Flask
- FastAPI
- SQLAlchemy
- NumPy
- Pandas
- TensorFlow
- PyTorch
- Plug-in Systems
- Database Drivers
- Cloud SDKs

---

# Best Practices

✅ Use ABC when inheritance is required.

✅ Use Protocols when only behavior matters.

✅ Add Type Hints to public APIs.

✅ Keep interfaces small.

✅ Use Generics for reusable code.

---

# Common Mistakes

❌ Confusing Duck Typing with Protocols.

❌ Forgetting to implement abstract methods.

❌ Thinking Type Hints enforce types at runtime.

❌ Using Generics unnecessarily.

❌ Creating very large interfaces.

---

# Summary Table

| Concept | Purpose |
|----------|---------|
| ABC | Enforce implementation |
| Interface | Define behavior contract |
| Protocol | Structural typing |
| Type Hint | Improve readability |
| Generic | Reusable type-safe code |
| Static Checking | Detect errors before running |

---

# Interview Questions

## Basic

- What is an Abstract Base Class?
- Does Python have interfaces?
- What is a Protocol?
- What are Type Hints?

---

## Intermediate

- ABC vs Protocol?
- Why use Type Hints?
- What is Generic Programming?
- Why are Protocols useful?

---

## Advanced

- Design a Plugin Framework.
- Design an Authentication System.
- Explain Structural Typing.
- How do Type Hints improve large projects?
- When should you use ABC instead of Protocol?

---

# Module 07 Summary

After completing this module, you can:

✅ Design abstract APIs using ABC.

✅ Understand Interface concepts in Python.

✅ Use Protocols for structural typing.

✅ Write clear Type Hints.

✅ Build reusable Generic classes.

✅ Understand Static Type Checking.

✅ Design extensible enterprise frameworks.

---

# Next Module

## Module 08 – Exception Handling, Custom Exceptions & Logging

Topics:

- Exception Hierarchy
- try / except / else / finally
- raise
- Custom Exceptions
- Exception Chaining
- Context Managers for Exceptions
- Logging Module
- Debugging Techniques
- Production Error Handling
