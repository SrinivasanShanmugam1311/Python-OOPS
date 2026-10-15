# Python Object-Oriented Programming (OOP)

# Module 07 – Abstract Classes, Interfaces & Type Hints

**File:** Module_07_Concepts_Explanation.md

**Level:** Intermediate → Advanced

**Duration:** 2 Hours

**Prerequisites:** Modules 01–06

---

# Module Overview

In previous modules, we learned:

- Classes & Objects
- Encapsulation
- Inheritance
- Polymorphism
- Magic Methods

Now we answer an important question:

> **How can we force every developer to follow the same design rules?**

This module introduces **Abstract Classes**, **Interfaces (Concept)**, **Protocols**, and **Type Hints**, which help build reliable, maintainable, and scalable applications.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand why Abstract Classes are needed.
- Design common interfaces for multiple classes.
- Use Python's `abc` module.
- Write Abstract Methods.
- Understand Interface concepts in Python.
- Use Protocols from `typing`.
- Write Type Hints.
- Understand Generic Programming basics.
- Perform Static Type Checking.

---

# Why Do We Need This Module?

Suppose you are building a payment system.

Every payment method should provide:

```text
pay()
```

Imagine a developer writes:

```python
class CreditCard:

    def pay(self):
        print("Paid")


class UPI:
    pass
```

Later,

```python
upi.pay()
```

Output

```
AttributeError
```

The mistake is discovered **only at runtime**.

We need a way to force every payment class to implement `pay()`.

That is why **Abstract Classes** exist.

---

# Evolution of Python Design

```
Normal Classes

↓

Duck Typing

↓

Abstract Classes (ABC)

↓

Protocols

↓

Type Hints

↓

Static Type Checking
```

Each step improves code quality and developer experience.

---

# 1. Abstract Base Classes (ABC)

## What?

An **Abstract Base Class (ABC)** is a class that defines a blueprint for other classes.

It specifies **what methods must exist**, but not necessarily how they are implemented.

---

## Real-Life Example

```
Vehicle

↓

Car

Bike

Bus
```

Every vehicle must implement:

- Start
- Stop

Each vehicle implements them differently.

---

## Why Use ABC?

Without ABC:

- Developers may forget required methods.
- Errors appear during execution.
- Code becomes inconsistent.

With ABC:

- Required methods are enforced.
- Missing implementations are detected immediately.
- Design is consistent.

---

## Where Is It Used?

- Payment Gateways
- Database Drivers
- Authentication Systems
- Game Engines
- Machine Learning Models
- Plugin Frameworks

---

# 2. abc Module

Python provides the built-in `abc` module for creating abstract classes.

```python
from abc import ABC, abstractmethod
```

### Components

| Component | Purpose |
|----------|---------|
| `ABC` | Base class for abstract classes |
| `@abstractmethod` | Marks a method as mandatory |

---

# 3. Abstract Methods

An abstract method:

- Has no implementation (or only a placeholder).
- Must be implemented by subclasses.

Example:

```python
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

Trying to create:

```python
Animal()
```

Results in:

```
TypeError
```

Because abstract classes cannot be instantiated.

---

# 4. Interface Concept

## What is an Interface?

An interface defines **what a class must do**, not **how it does it**.

Example:

```
Payment

↓

pay()
```

Every payment method must provide `pay()`.

---

## Does Python Have Interfaces?

**No.**

Python does **not** have an `interface` keyword like Java or C#.

Instead, Python uses:

- Abstract Base Classes (ABC)
- Protocols

to achieve similar behavior.

---

# ABC vs Interface

| Abstract Class | Interface (Concept) |
|----------------|---------------------|
| Can contain implemented methods | Only defines behavior |
| Can contain attributes | Focuses on method contracts |
| Uses inheritance | Uses contracts |

In Python, ABCs often serve as interfaces.

---

# 5. Protocols

## What is a Protocol?

A Protocol defines **expected behavior** rather than requiring inheritance.

If an object has the required methods, it satisfies the protocol.

Example:

```
Duck

↓

walk()

quack()

swim()
```

Anything implementing these methods behaves like a duck.

---

## Why Protocols?

Protocols reduce coupling.

Classes don't need to inherit from the same base class—they only need to provide the expected methods.

---

## Where Are Protocols Used?

- Library Design
- APIs
- Frameworks
- Large Applications

---

# 6. Type Hints

## What are Type Hints?

Type hints describe the expected types of variables, parameters, and return values.

Example:

Without hints:

```python
def add(a, b):
    return a + b
```

With hints:

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## Benefits

- Better readability.
- IDE auto-completion.
- Easier maintenance.
- Better documentation.
- Supports static analysis.

---

# 7. Generic Programming (Introduction)

Generic programming allows code to work with multiple data types.

Instead of writing:

```
Integer Stack

String Stack

Employee Stack
```

We write:

```
One Generic Stack
```

Python uses `TypeVar` for generic programming.

---

# 8. Static Type Checking

Python is dynamically typed.

Errors are usually found while the program is running.

Static type checking analyzes code **before execution**.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b

add("10", 20)
```

A static type checker reports that `"10"` is a string where an integer is expected.

---

# Comparison

| Feature | Purpose |
|----------|---------|
| Duck Typing | Trust object behavior |
| ABC | Enforce required methods |
| Protocol | Check behavior without inheritance |
| Type Hints | Improve readability and tooling |
| Static Checking | Detect errors before execution |

---

# Real-World Applications

## Payment Framework

Every payment method implements:

```
pay()
```

Examples:

- Credit Card
- UPI
- Wallet
- Net Banking

---

## Plugin Architecture

Every plugin implements:

```
start()

stop()
```

Examples:

- Audio Plugin
- Video Plugin
- Analytics Plugin

---

## Authentication Framework

Every authentication system implements:

```
authenticate()
```

Examples:

- Google Login
- Facebook Login
- Email Login
- LDAP Login

---

# Best Practices

- Use ABC when you need mandatory methods.
- Use Protocols for flexible designs.
- Add Type Hints to public APIs.
- Keep interfaces small and focused.
- Prefer composition over deep inheritance.

---

# Common Mistakes

- Confusing ABC with normal classes.
- Using inheritance where Protocols are sufficient.
- Ignoring Type Hints in large projects.
- Creating large, complex interfaces.
- Overusing abstract classes for simple problems.

---

# Skills Gained

After completing this module, you will be able to:

- Design reusable software architectures.
- Enforce implementation rules.
- Build extensible frameworks.
- Write type-safe Python code.
- Improve code readability and maintainability.
- Understand modern Python development practices.

---

# Expected Learning Outcome

By the end of this module, you will understand:

- Why Abstract Classes exist.
- How Interfaces are modeled in Python.
- When to use Protocols.
- Why Type Hints matter.
- How Static Type Checking improves code quality.

These concepts are widely used in professional Python projects, frameworks, libraries, and enterprise applications.

---

# Next

**Module_07_Code_Examples.md (Part 1)**

Topics:

- `abc` Module
- `ABC`
- `@abstractmethod`
- Creating Abstract Classes
- Preventing Object Creation
- Implementing Child Classes
- Real-world ABC Examples
