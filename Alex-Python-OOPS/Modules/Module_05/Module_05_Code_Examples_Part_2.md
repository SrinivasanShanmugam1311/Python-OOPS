# Python Object-Oriented Programming (OOP)

# Module 05 – Polymorphism & Duck Typing

# Module_05_Code_Examples.md (Part 2)

**Course Level:** Intermediate → Advanced

---

# Project 1 – Payment Gateway

## Objective

Design a payment gateway that can process multiple payment methods without changing existing code.

---

## Class Diagram

```
              Payment
                  ▲
      -------------------------
      |          |            |
 CreditCard     UPI        NetBanking
```

---

## Code

```python
class Payment:

    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay().")


class CreditCard(Payment):

    def pay(self, amount):
        print(f"₹{amount} paid using Credit Card")


class UPI(Payment):

    def pay(self, amount):
        print(f"₹{amount} paid using UPI")


class NetBanking(Payment):

    def pay(self, amount):
        print(f"₹{amount} paid using Net Banking")


def checkout(payment, amount):
    payment.pay(amount)


payments = [
    CreditCard(),
    UPI(),
    NetBanking()
]

for payment in payments:
    checkout(payment, 2500)
```

### Output

```text
₹2500 paid using Credit Card
₹2500 paid using UPI
₹2500 paid using Net Banking
```

---

## Why Polymorphism?

No `if-elif` chain.

To add a new payment method, create a new class and implement `pay()`.

---

# Project 2 – Notification System

## Objective

Send notifications through different communication channels.

---

## Code

```python
class Notification:

    def send(self, message):
        raise NotImplementedError


class Email(Notification):

    def send(self, message):
        print(f"Email : {message}")


class SMS(Notification):

    def send(self, message):
        print(f"SMS : {message}")


class WhatsApp(Notification):

    def send(self, message):
        print(f"WhatsApp : {message}")


def notify(service, message):
    service.send(message)


services = [
    Email(),
    SMS(),
    WhatsApp()
]

for service in services:
    notify(service, "Interview Tomorrow")
```

### Output

```text
Email : Interview Tomorrow
SMS : Interview Tomorrow
WhatsApp : Interview Tomorrow
```

---

# Project 3 – Report Generator

## Objective

Generate reports in multiple formats.

---

## Code

```python
class Report:

    def generate(self):
        raise NotImplementedError


class PDFReport(Report):

    def generate(self):
        print("Generating PDF Report")


class ExcelReport(Report):

    def generate(self):
        print("Generating Excel Report")


class HTMLReport(Report):

    def generate(self):
        print("Generating HTML Report")


reports = [
    PDFReport(),
    ExcelReport(),
    HTMLReport()
]

for report in reports:
    report.generate()
```

---

# Project 4 – File Reader Framework

## Objective

Read different file types using a common interface.

---

## Code

```python
class FileReader:

    def read(self):
        raise NotImplementedError


class TextReader(FileReader):

    def read(self):
        print("Reading Text File")


class PDFReader(FileReader):

    def read(self):
        print("Reading PDF File")


class CSVReader(FileReader):

    def read(self):
        print("Reading CSV File")


files = [
    TextReader(),
    PDFReader(),
    CSVReader()
]

for file in files:
    file.read()
```

---

# Project 5 – Universal Payment Processing Framework

## Objective

Create an extensible payment framework supporting multiple payment methods.

---

## Code

```python
class PaymentMethod:

    def pay(self, amount):
        raise NotImplementedError


class CreditCard(PaymentMethod):

    def pay(self, amount):
        print(f"Credit Card : ₹{amount}")


class DebitCard(PaymentMethod):

    def pay(self, amount):
        print(f"Debit Card : ₹{amount}")


class UPI(PaymentMethod):

    def pay(self, amount):
        print(f"UPI : ₹{amount}")


class Wallet(PaymentMethod):

    def pay(self, amount):
        print(f"Wallet : ₹{amount}")


class PayPal(PaymentMethod):

    def pay(self, amount):
        print(f"PayPal : ₹{amount}")


class PaymentProcessor:

    def process(self, payment, amount):

        print("Processing Payment...")

        payment.pay(amount)

        print("Payment Successful\n")


processor = PaymentProcessor()

methods = [
    CreditCard(),
    DebitCard(),
    UPI(),
    Wallet(),
    PayPal()
]

for method in methods:
    processor.process(method, 5000)
```

### Output

```text
Processing Payment...
Credit Card : ₹5000
Payment Successful

Processing Payment...
Debit Card : ₹5000
Payment Successful

Processing Payment...
UPI : ₹5000
Payment Successful

Processing Payment...
Wallet : ₹5000
Payment Successful

Processing Payment...
PayPal : ₹5000
Payment Successful
```

---

# Extending the Framework

Adding a new payment method requires **no changes** to `PaymentProcessor`.

Example:

```python
class Crypto(PaymentMethod):

    def pay(self, amount):
        print(f"Crypto : ₹{amount}")


processor.process(Crypto(), 10000)
```

This follows the **Open-Closed Principle (OCP)**.

---

# Real-World Applications

The same design is used in:

- Payment Gateways
- Cloud Storage APIs
- Logging Frameworks
- Database Drivers
- Machine Learning Libraries
- Authentication Systems
- Web Frameworks
- Plugin Architectures

---

# Best Practices

- Program to abstractions rather than concrete classes.
- Keep interfaces small and focused.
- Avoid long `if-elif` chains.
- Use polymorphism for extensibility.
- Use composition where appropriate.
- Raise `NotImplementedError` in base classes intended to be overridden.
- Design new classes without modifying existing business logic.

---

# Common Mistakes

- Using `isinstance()` instead of polymorphism.
- Hardcoding object types.
- Mixing unrelated responsibilities.
- Forgetting to override required methods.
- Violating the Open-Closed Principle by editing existing logic for every new class.

---

# Interview Questions

## Basic

- What is polymorphism?
- What is method overriding?
- What is duck typing?

---

## Intermediate

- Explain runtime polymorphism with an example.
- Why is polymorphism better than `if-elif` chains?
- How is duck typing related to polymorphism?

---

## Advanced

- Design a payment gateway using polymorphism.
- How does polymorphism support the Open-Closed Principle?
- Explain the difference between inheritance, composition, and polymorphism.
- Why are plugin systems commonly implemented using polymorphism?

---

# Module Summary

After completing Module 05, you can:

- ✅ Explain Runtime Polymorphism.
- ✅ Implement Method Overriding.
- ✅ Apply Duck Typing effectively.
- ✅ Understand EAFP vs LBYL.
- ✅ Design interface-like APIs.
- ✅ Build extensible software using polymorphism.
- ✅ Replace complex conditional logic with object-oriented design.
- ✅ Create enterprise-style frameworks such as payment gateways, notification services, report generators, and file readers.

---

# What's Next?

## Module 06 – Abstract Base Classes (ABC), Interfaces & SOLID Foundations

Topics include:

- Abstract Base Classes (`abc` module)
- `@abstractmethod`
- Interface Design
- Multiple Abstract Classes
- Template Method Pattern
- Dependency Inversion Principle
- Interface Segregation Principle
- Liskov Substitution Principle
- Open-Closed Principle
- Enterprise Design Guidelines
