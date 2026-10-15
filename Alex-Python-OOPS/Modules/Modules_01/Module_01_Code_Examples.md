# Python Object-Oriented Programming (OOP) Using Python

# Module 01 – Python Object Model & Class Fundamentals

**Course:** Python OOP (Intermediate → Advanced)

**Document:** Module_01_Code_Examples.md

---

# Topic 1 – Introduction to Object-Oriented Programming (OOP)

---

# Learning Objectives

After completing this topic, you will be able to:

- Understand what Object-Oriented Programming (OOP) is.
- Explain why OOP is widely used.
- Compare Procedural Programming with Object-Oriented Programming.
- Understand the four pillars of OOP.
- Understand why Python is considered an Object-Oriented language.
- Relate real-world entities to software objects.

---

# 1. What is Programming?

Programming is the process of writing instructions that tell a computer how to perform a task or solve a problem.

Example:

```python
print("Hello World")
```

Output

```text
Hello World
```

Every program is made up of instructions that the computer executes one after another.

---

# 2. What is a Programming Paradigm?

A Programming Paradigm is a style or methodology used to write software.

It defines how a programmer organizes logic, data, and functionality.

Python supports multiple programming paradigms.

Some common paradigms include:

- Procedural Programming
- Object-Oriented Programming
- Functional Programming
- Event-Driven Programming
- Declarative Programming

This course focuses on **Object-Oriented Programming (OOP).**

---

# 3. Procedural Programming

Procedural Programming organizes code into functions.

Data is passed between functions.

Example

```python
def withdraw(balance, amount):

    if amount <= balance:
        balance -= amount

    return balance

balance = 10000

balance = withdraw(balance, 2500)

print(balance)
```

Output

```text
7500
```

## Advantages

- Easy to understand
- Less code initially
- Suitable for small programs

## Disadvantages

- Difficult to manage large software
- Functions can modify data from anywhere
- Low reusability
- Code duplication
- Difficult maintenance

---

# 4. Object-Oriented Programming

Object-Oriented Programming organizes software around **Objects**.

An Object contains

- Data
- Behaviour

Instead of writing

```text
deposit()

withdraw()

check_balance()
```

we create a BankAccount object.

Example

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(10000)

account.deposit(500)

account.withdraw(1000)

print(account.balance)
```

Output

```text
9500
```

Notice that the balance belongs to the object itself.

---

# 5. Why Do We Need OOP?

Suppose you are building a Hospital Management System.

There may be

- 10000 Patients
- 500 Doctors
- 100 Nurses
- Thousands of Appointments

Managing everything with only variables and functions becomes difficult.

Instead, we model real-world entities as objects.

Example

```text
Patient

Doctor

Appointment

Medicine

Bill

Laboratory
```

Each object stores its own data and behaviour.

---

# 6. Real-World Analogy

Consider a Car.

## State (Data)

- Brand
- Colour
- Speed
- Fuel
- Engine Number

## Behaviour (Methods)

- start()
- stop()
- accelerate()
- brake()
- refuel()

Software models the same concept.

```python
class Car:

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

car = Car()

car.start()

car.stop()
```

Output

```text
Car Started
Car Stopped
```

---

# 7. Four Pillars of OOP

These are the foundation of Object-Oriented Programming.

---

## Encapsulation

Combining data and methods together while protecting the data.

Example

```python
class BankAccount:

    def __init__(self):
        self.__balance = 0
```

---

## Inheritance

Reusing an existing class.

Example

```python
class Vehicle:
    pass

class Car(Vehicle):
    pass
```

---

## Polymorphism

One interface with different implementations.

Example

```python
dog.sound()

cat.sound()

bird.sound()
```

Each object implements its own version of `sound()`.

---

## Abstraction

Showing only the required functionality while hiding implementation details.

Example

A driver operates a car without needing to understand the engine internals.

---

# 8. Why Python is Good for OOP?

Python supports

- Classes
- Objects
- Inheritance
- Multiple Inheritance
- Polymorphism
- Abstraction
- Properties
- Decorators
- Dataclasses
- Magic Methods
- Abstract Base Classes

Python combines simplicity with powerful object-oriented features.

---

# 9. Real-World OOP Examples

## Banking System

Classes

```text
Customer

Account

Transaction

Loan

Branch

Employee
```

---

## Hospital Management

Classes

```text
Patient

Doctor

Appointment

Medicine

Laboratory

Bill
```

---

## E-Commerce

Classes

```text
Customer

Product

Cart

Order

Payment

Invoice
```

---

## School Management

Classes

```text
Student

Teacher

Course

Exam

Result
```

---

# 10. Benefits of OOP

- Better code organization
- Easy maintenance
- Code reuse
- Easier debugging
- Better scalability
- Better teamwork
- Models real-world entities naturally

---

# 11. OOP Terminology

| Term | Meaning |
|------|---------|
| Class | Blueprint for creating objects |
| Object | Instance of a class |
| Attribute | Data stored in an object |
| Method | Function inside a class |
| Instance | Object created from a class |
| Constructor | Initializes an object |
| Encapsulation | Protecting object data |
| Inheritance | Reusing another class |
| Polymorphism | Same interface, different behaviour |
| Abstraction | Hiding implementation details |

---

# Example 1 – Procedural vs OOP

## Procedural Programming

```python
name = "Alex"

salary = 50000

def display(name, salary):
    print(name)
    print(salary)

display(name, salary)
```

Output

```text
Alex
50000
```

---

## Object-Oriented Programming

```python
class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def display(self):

        print(self.name)
        print(self.salary)

employee = Employee("Alex", 50000)

employee.display()
```

Output

```text
Alex
50000
```

### Why OOP Is Better

- Data and methods stay together.
- Better organization.
- Easy maintenance.
- High reusability.
- Easy to extend.

---

# Common Mistakes

❌ Thinking OOP means only creating classes.

Classes are only one part of Object-Oriented Programming.

---

❌ Creating one huge class.

Instead, create multiple small classes with a single responsibility.

---

❌ Using global variables.

Store data inside objects whenever possible.

---

# Best Practices

- Think in terms of real-world entities.
- Keep classes focused.
- Use meaningful class names.
- Keep related data and methods together.
- Prefer readability over clever code.

---

# Interview Questions

## Q1. What is Object-Oriented Programming?

**Answer**

Object-Oriented Programming is a programming paradigm that organizes software around objects. Each object combines data (attributes) and behaviour (methods), making software modular, reusable, and maintainable.

---

## Q2. Why is OOP preferred for large applications?

**Answer**

OOP divides software into independent objects, making applications easier to maintain, test, extend, and reuse. It reduces duplication and models real-world systems naturally.

---

## Q3. What are the four pillars of OOP?

**Answer**

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

---

## Q4. Is Python purely object-oriented?

**Answer**

No.

Python is a multi-paradigm language. It supports:

- Object-Oriented Programming
- Procedural Programming
- Functional Programming

However, everything in Python is treated as an object, making OOP a central feature of the language.

---

# Summary

In this topic, you learned:

- What a programming paradigm is.
- The difference between Procedural Programming and Object-Oriented Programming.
- Why OOP is essential for building scalable software.
- The four pillars of OOP.
- Why Python is well suited for Object-Oriented Programming.
- How real-world entities are modeled as software objects.

---

# What's Next?

**Topic 2 – Understanding Objects & Python Object Model**

You will learn:

- What is an Object?
- Identity, State, and Behaviour
- Everything is an Object
- Object References
- Memory Model
- `id()`
- `type()`
- Object Creation Process
- Python Object Lifecycle
