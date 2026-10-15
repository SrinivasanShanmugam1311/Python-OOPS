# Python Object-Oriented Programming (OOP)

# Module 05 – Polymorphism & Duck Typing

## Module_05_Code_Examples.md (Part 1B)

**Course Level:** Intermediate → Advanced

---

# Topic 6 – Duck Typing

---

## What is Duck Typing?

Duck Typing is one of Python's most powerful features.

Python does **not** check an object's type first.

Instead, it checks whether the object has the required behavior (methods or attributes).

> **"If it walks like a duck and quacks like a duck, treat it as a duck."**

---

## Example 1 – Different Classes, Same Method

```python
class Dog:

    def speak(self):
        print("Dog Barks")


class Cat:

    def speak(self):
        print("Cat Meows")


class Robot:

    def speak(self):
        print("Robot Speaking")


def make_sound(obj):
    obj.speak()


make_sound(Dog())
make_sound(Cat())
make_sound(Robot())
```

### Output

```text
Dog Barks
Cat Meows
Robot Speaking
```

---

## Example 2 – Payment Systems

```python
class CreditCard:

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI:

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Wallet:

    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")


def process_payment(payment, amount):
    payment.pay(amount)


process_payment(CreditCard(), 1000)
process_payment(UPI(), 500)
process_payment(Wallet(), 200)
```

### Output

```text
Paid ₹1000 using Credit Card
Paid ₹500 using UPI
Paid ₹200 using Wallet
```

---

## Example 3 – File Processing

```python
class TextFile:

    def read(self):
        print("Reading Text File")


class PDFFile:

    def read(self):
        print("Reading PDF File")


class CSVFile:

    def read(self):
        print("Reading CSV File")


def load_file(file):
    file.read()


load_file(TextFile())
load_file(PDFFile())
load_file(CSVFile())
```

---

# Advantages of Duck Typing

- Flexible
- Extensible
- Less coupling
- No unnecessary inheritance
- Easier testing

---

# Topic 7 – EAFP

---

## What is EAFP?

**EAFP = Easier to Ask Forgiveness than Permission**

Instead of checking everything beforehand, perform the operation and handle exceptions if something goes wrong.

Python encourages this style.

---

## Example 1 – Dictionary Access

```python
student = {
    "name": "Alex",
    "marks": 95
}

try:
    print(student["grade"])

except KeyError:
    print("Grade Not Available")
```

### Output

```text
Grade Not Available
```

---

## Example 2 – File Handling

```python
try:

    file = open("sample.txt")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File Not Found")
```

---

## Example 3 – Division

```python
try:

    number = 100 / 0

except ZeroDivisionError:

    print("Cannot Divide by Zero")
```

### Output

```text
Cannot Divide by Zero
```

---

# Why EAFP?

- Cleaner code
- Pythonic style
- Avoids unnecessary checks
- Works well in concurrent environments

---

# Topic 8 – LBYL

---

## What is LBYL?

**LBYL = Look Before You Leap**

Check conditions before performing an operation.

---

## Example 1

```python
number = 10

if number != 0:
    print(100 / number)
```

---

## Example 2

```python
student = {
    "name": "Alex"
}

if "marks" in student:
    print(student["marks"])
else:
    print("Marks Not Found")
```

---

# EAFP vs LBYL

| EAFP | LBYL |
|------|------|
| Try First | Check First |
| Uses Exceptions | Uses Conditions |
| Pythonic | Traditional |
| Faster in many situations | Useful when failures are common |

---

# Topic 9 – Interface Concept

---

Python does not have an explicit `interface` keyword.

Instead, it relies on:

- Duck Typing
- Abstract Base Classes (covered later)

---

## Example

```python
class Email:

    def send(self):
        print("Email Sent")


class SMS:

    def send(self):
        print("SMS Sent")


class WhatsApp:

    def send(self):
        print("WhatsApp Message Sent")


def notify(service):
    service.send()


notify(Email())
notify(SMS())
notify(WhatsApp())
```

### Output

```text
Email Sent
SMS Sent
WhatsApp Message Sent
```

---

# Practical Example – Shape Drawing

```python
class Circle:

    def draw(self):
        print("Drawing Circle")


class Rectangle:

    def draw(self):
        print("Drawing Rectangle")


class Triangle:

    def draw(self):
        print("Drawing Triangle")


def render(shape):
    shape.draw()


render(Circle())
render(Rectangle())
render(Triangle())
```

---

# Practical Example – Logging

```python
class ConsoleLogger:

    def log(self):
        print("Console Log")


class FileLogger:

    def log(self):
        print("File Log")


class DatabaseLogger:

    def log(self):
        print("Database Log")


def write_log(logger):
    logger.log()


write_log(ConsoleLogger())
write_log(FileLogger())
write_log(DatabaseLogger())
```

---

# Best Practices

✅ Program to behavior, not concrete classes.

✅ Prefer Duck Typing over excessive `isinstance()` checks.

✅ Use EAFP for operations that may legitimately fail.

✅ Keep interfaces small and focused.

✅ Write classes that expose consistent method names.

---

# Common Mistakes

❌ Overusing `isinstance()`.

❌ Catching every exception with a bare `except:`.

❌ Using Duck Typing without documenting expected methods.

❌ Mixing unrelated responsibilities in one class.

❌ Ignoring meaningful exception handling.

---

# Interview Questions

## Basic

- What is Polymorphism?
- What is Duck Typing?
- What is EAFP?
- What is LBYL?

---

## Intermediate

- Difference between Duck Typing and Inheritance.
- Explain Runtime Polymorphism.
- Why does Python prefer EAFP?
- How are interfaces implemented in Python?

---

## Advanced

- When should Duck Typing be avoided?
- Explain "Program to an Interface."
- Compare EAFP and LBYL in concurrent applications.
- How do frameworks like Django and Flask use Duck Typing?

---

# Summary

After completing Part 1B, you can:

✅ Apply Duck Typing

✅ Write polymorphic code without inheritance

✅ Use EAFP effectively

✅ Understand LBYL and when to use it

✅ Design interface-like APIs

✅ Build loosely coupled Python applications

---

# Next Part

## Module_05_Code_Examples.md (Part 2)

Real-world Projects:

- Payment Gateway
- Notification System
- Report Generator
- File Reader Framework
- Universal Payment Processing Framework (Mini Project)
- Best Practices
- Module Summary
