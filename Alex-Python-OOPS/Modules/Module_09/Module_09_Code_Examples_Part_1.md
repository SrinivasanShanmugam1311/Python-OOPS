# Python Object-Oriented Programming (OOP)

# Module 09 – SOLID Principles & Design Patterns

# Module_09_Code_Examples_Part_1.md

**Level:** Advanced

**Topics Covered**

- Single Responsibility Principle (SRP)
- Open Closed Principle (OCP)
- Liskov Substitution Principle (LSP)
- Interface Segregation Principle (ISP)
- Dependency Inversion Principle (DIP)
- Clean Code Principles

---

# 1. Single Responsibility Principle (SRP)

## Concept

A class should have:

```
One Class

↓

One Responsibility

↓

One Reason To Change
```

---

# Bad Example

## One Class Doing Everything

```python
class Invoice:

    def calculate_total(self):

        print("Calculating Total")


    def save_database(self):

        print("Saving Invoice")


    def send_email(self):

        print("Sending Email")
```

Problem:

This class has:

```
Invoice Calculation

Database Handling

Email Handling
```

Three responsibilities.

---

# Better Design

Separate responsibilities.

```python
class InvoiceCalculator:


    def calculate_total(self):

        print("Calculating Total")



class InvoiceRepository:


    def save(self):

        print("Saving Invoice")



class EmailService:


    def send(self):

        print("Sending Email")



calculator = InvoiceCalculator()

repository = InvoiceRepository()

email = EmailService()


calculator.calculate_total()

repository.save()

email.send()
```

Output

```
Calculating Total
Saving Invoice
Sending Email
```

---

# Real World Usage

SRP is used in:

- Django Models
- API Services
- Database Layers
- Payment Systems

---

<br>

# 2. Open Closed Principle (OCP)

## Concept

A class should be:

```
Open for Extension

Closed for Modification
```

Meaning:

Add new features without changing existing code.

---

# Bad Example

```python
class Payment:


    def pay(self, method):

        if method == "UPI":

            print("UPI Payment")


        elif method == "CARD":

            print("Card Payment")
```

Problem:

Tomorrow:

```
Wallet

Net Banking

Crypto
```

Need to modify this class.

---

# Better Design

Use abstraction.

```python
from abc import ABC, abstractmethod



class Payment(ABC):


    @abstractmethod
    def pay(self):

        pass



class UPI(Payment):


    def pay(self):

        print("UPI Payment")



class CreditCard(Payment):


    def pay(self):

        print("Credit Card Payment")



class Wallet(Payment):


    def pay(self):

        print("Wallet Payment")



payments = [

    UPI(),

    CreditCard(),

    Wallet()

]


for payment in payments:

    payment.pay()
```

Output

```
UPI Payment
Credit Card Payment
Wallet Payment
```

Adding a new payment:

```python
class Crypto(Payment):

    def pay(self):

        print("Crypto Payment")
```

No existing code changes.

---

# 3. Liskov Substitution Principle (LSP)

## Concept

Child classes should replace parent classes safely.

```
Parent Object

↓

Child Object

↓

Application Should Still Work
```

---

# Bad Example

```python
class Bird:


    def fly(self):

        print("Flying")



class Penguin(Bird):


    def fly(self):

        raise Exception(
            "Cannot Fly"
        )
```

Problem:

Penguin is a Bird,
but cannot fly.

Inheritance is wrong.

---

# Better Design

```python
class Bird:


    def eat(self):

        print("Eating")



class FlyingBird(Bird):


    def fly(self):

        print("Flying")



class Sparrow(FlyingBird):

    pass



class Penguin(Bird):

    pass



bird1 = Sparrow()

bird1.fly()


bird2 = Penguin()

bird2.eat()
```

Output

```
Flying
Eating
```

---

# Rule

Do not create inheritance only because classes look related.

Design based on behavior.

---

<br>

# 4. Interface Segregation Principle (ISP)

## Concept

Clients should not depend on methods they do not use.

---

# Bad Design

```python
class Machine:


    def print_document(self):

        pass


    def scan_document(self):

        pass


    def fax_document(self):

        pass
```

Problem:

Simple printer does not need:

```
Scan

Fax
```

---

# Better Design

Create small interfaces.

```python
from abc import ABC, abstractmethod



class Printer(ABC):


    @abstractmethod
    def print_document(self):

        pass



class Scanner(ABC):


    @abstractmethod
    def scan_document(self):

        pass



class SimplePrinter(Printer):


    def print_document(self):

        print("Printing")



class MultiFunctionPrinter(
    Printer,
    Scanner
):


    def print_document(self):

        print("Printing")


    def scan_document(self):

        print("Scanning")
```

---

# Benefits

- Small interfaces
- Less dependency
- Easier maintenance

---

<br>

# 5. Dependency Inversion Principle (DIP)

## Concept

High-level modules should not depend on low-level modules.

Both should depend on abstraction.

---

# Bad Design

```python
class MySQLDatabase:


    def connect(self):

        print("MySQL Connected")



class Application:


    def __init__(self):

        self.database = MySQLDatabase()



app = Application()

app.database.connect()
```

Problem:

Application is tightly connected to MySQL.

Changing database is difficult.

---

# Better Design

Use abstraction.

```python
from abc import ABC, abstractmethod



class Database(ABC):


    @abstractmethod
    def connect(self):

        pass



class MySQL(Database):


    def connect(self):

        print("MySQL Connected")



class MongoDB(Database):


    def connect(self):

        print("MongoDB Connected")



class Application:


    def __init__(self, database):

        self.database = database



app = Application(
    MySQL()
)

app.database.connect()
```

Output

```
MySQL Connected
```

Now:

```python
app = Application(
    MongoDB()
)
```

Works without changing Application.

---

# Clean Code Principles

---

# 1. DRY

## Don't Repeat Yourself

Bad:

```python
print("Welcome Alex")

print("Welcome John")

print("Welcome Sara")
```

Better:

```python
def welcome(name):

    print(
        f"Welcome {name}"
    )


welcome("Alex")

welcome("John")
```

---

# 2. KISS

## Keep It Simple

Avoid unnecessary complexity.

Bad:

```
100 lines for simple calculation
```

Good:

```
Simple readable solution
```

---

# 3. YAGNI

## You Aren't Gonna Need It

Do not build features before they are required.

Example:

Don't create:

```
Payment

Crypto

AI Payment

Future Payment
```

when only UPI is needed.

---

# 4. High Cohesion

A class should contain related responsibilities.

Good:

```
Employee

↓

Salary

Leave

Profile
```

Bad:

```
Employee

↓

Salary

↓

Email

↓

Database

↓

Report
```

---

# 5. Loose Coupling

Objects should depend less on each other.

Bad:

```
Order

↓

UPI Class
```

Good:

```
Order

↓

Payment Interface

↓

UPI
```

---

# SOLID Summary

| Principle | Meaning |
|-|-|
| SRP | One class, one responsibility |
| OCP | Extend without modifying |
| LSP | Child must replace parent |
| ISP | Small focused interfaces |
| DIP | Depend on abstractions |

---

# Interview Questions

## Basic

1. What is SRP?
2. What does OCP mean?
3. Why do we need DIP?

---

## Intermediate

1. Explain LSP with example.
2. Difference between inheritance and composition?
3. How does ISP improve design?

---

## Advanced

1. Design a payment system using SOLID.
2. How does DIP reduce coupling?
3. Explain how OCP supports scalable software.

---

# Next

## Module_09_Code_Examples_Part_2.md

Topics:

- Singleton Pattern
- Factory Method
- Abstract Factory
- Builder Pattern
- Strategy Pattern
- Observer Pattern
- Adapter Pattern
- Facade Pattern
- Template Method
