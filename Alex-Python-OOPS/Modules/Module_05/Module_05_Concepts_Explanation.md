# Python Object-Oriented Programming (OOP) Using Python

# Module 05 – Polymorphism & Duck Typing

> **Course Level:** Intermediate → Advanced
>
> **Duration:** 1–2 Hours
>
> **Prerequisites:** Modules 01–04

---

# Module Overview

So far, we have learned how to

- Create Classes
- Create Objects
- Design Relationships
- Protect Data
- Reuse Code using Inheritance

Now we move to one of the most powerful principles of Object-Oriented Programming:

# Polymorphism

The word **Polymorphism** comes from two Greek words.

- Poly = Many
- Morph = Forms

Meaning

> **One Interface, Many Implementations**

Instead of writing different code for every object, we write generic code.

Each object decides how it should behave.

This makes software

- Flexible
- Extensible
- Maintainable
- Scalable

---

# Learning Objectives

After completing this module you will be able to

- Understand Polymorphism
- Implement Runtime Polymorphism
- Override Methods correctly
- Understand Duck Typing
- Apply EAFP philosophy
- Understand Interface concepts
- Build loosely coupled systems
- Decide between Composition and Inheritance

---

# What is Polymorphism?

Polymorphism means

> One interface can represent many different implementations.

Example

A single method

```
draw()
```

may behave differently for

- Circle
- Rectangle
- Triangle

Same method.

Different implementation.

---

# Why Polymorphism?

Without polymorphism

```
if object == Car

if object == Bike

if object == Bus

if object == Truck
```

Large applications become difficult to maintain.

With polymorphism

```
vehicle.start()
```

Each object performs its own implementation.

No complex if-else chains.

---

# Benefits

- Reusable Code
- Cleaner Design
- Less Coupling
- Easy Extension
- Better Testing
- Better Maintainability

---

# Types of Polymorphism

Python mainly supports

## Runtime Polymorphism

through

- Method Overriding
- Duck Typing

Python does not support traditional compile-time method overloading like Java or C++.

Instead

- Default Arguments
- Variable Arguments
- Keyword Arguments

are used.

---

# Runtime Polymorphism

Runtime Polymorphism means

The actual method is decided while the program is running.

Example

```
Animal

↓

Dog

↓

Cat
```

Calling

```
sound()
```

produces

Dog → Bark

Cat → Meow

The same method call behaves differently depending on the object.

---

# Method Overriding

Method Overriding is the foundation of Runtime Polymorphism.

A child class replaces the implementation inherited from its parent.

Rules

- Same method name
- Same purpose
- Different implementation

---

# Operator Polymorphism

Operators behave differently depending on operands.

Examples

```
5 + 3

Addition
```

```
"Python" + "OOP"

Concatenation
```

```
[1,2] + [3,4]

List Merge
```

Same operator.

Different behavior.

This is Operator Polymorphism.

Python internally uses Magic Methods.

Example

```
__add__()
```

---

# Built-in Polymorphism

Python functions also demonstrate polymorphism.

Examples

```
len()

str()

print()

max()

min()

sum()
```

Each function works for many object types.

---

# Duck Typing

Duck Typing is one of Python's most unique features.

The famous statement says

> If it walks like a duck and quacks like a duck, treat it as a duck.

Python cares about

Behavior

not

Object Type.

Example

Any object containing

```
speak()
```

can be used.

Whether it is

Dog

Robot

Human

Bird

does not matter.

---

# Why Duck Typing?

Avoid unnecessary inheritance.

Objects become more flexible.

Encourages loosely coupled design.

Widely used in

- Django
- Flask
- FastAPI
- Pandas
- NumPy

---

# Duck Typing vs Inheritance

Inheritance

Requires

```
IS-A
```

relationship.

Duck Typing requires

```
HAS THE REQUIRED METHOD
```

No inheritance required.

---

# EAFP

Python follows

## EAFP

Meaning

> Easier to Ask Forgiveness than Permission

Instead of checking everything first

Python simply performs the operation

and handles exceptions if something fails.

Example idea

```
try

except
```

This style is considered more Pythonic.

---

# LBYL

LBYL means

Look Before You Leap

Example

```
if file exists

open file
```

This approach is common in languages like Java.

Python generally prefers EAFP.

---

# EAFP vs LBYL

| EAFP | LBYL |
|------|------|
| Try First | Check First |
| try-except | if-condition |
| Pythonic | Traditional |
| Faster in many cases | Safer when failure is expected frequently |

---

# Interfaces (Concept)

Python has no explicit Interface keyword.

Instead

interfaces are implemented using

- Duck Typing
- Abstract Base Classes (ABC)

which will be covered later.

An Interface simply defines

"What an object should do"

not

"How it should do it"

---

# Loose Coupling

Polymorphism reduces dependency.

Instead of

```
PaymentGateway

↓

CreditCard
```

We use

```
PaymentGateway

↓

Any Payment Method
```

Adding new payment methods requires

No code modification.

Only a new class.

---

# Composition vs Inheritance

Inheritance

```
IS-A
```

Composition

```
HAS-A
```

Polymorphism works beautifully with both.

Modern software usually prefers

Composition + Polymorphism.

---

# Real-world Applications

Polymorphism is widely used in

- Payment Gateways
- Notification Systems
- Logging Frameworks
- Database Drivers
- File Readers
- Machine Learning Libraries
- Web Frameworks
- Game Engines

---

# Hands-on Programs

During this module you will build

- Payment Gateway
- Notification System
- Report Generator
- File Reader Framework
- Shape Drawing System
- Employee Salary Processor

---

# Mini Assignment

## Universal Payment Processing Framework

Requirements

Support multiple payment methods

Examples

- Credit Card
- Debit Card
- UPI
- Net Banking
- Wallet
- PayPal

The framework should

- Process payments
- Print receipts
- Handle failures
- Allow future payment methods without modifying existing code

Goal

Apply Runtime Polymorphism.

---

# Best Practices

- Program to Interfaces
- Avoid long if-else chains
- Prefer Polymorphism over conditional logic
- Use Duck Typing when appropriate
- Follow Python's EAFP philosophy
- Design loosely coupled classes

---

# Common Mistakes

- Confusing Overloading with Overriding
- Overusing isinstance()
- Ignoring Duck Typing
- Creating unnecessary inheritance
- Violating Open-Closed Principle

---

# Skills Gained

After completing this module you can

- Design polymorphic systems
- Write generic reusable code
- Apply Duck Typing
- Use EAFP correctly
- Understand Interface-based design
- Build extensible frameworks
- Reduce code duplication
- Improve software flexibility

---

# Expected Learning Outcome

After completing Module 05 you will understand how Python achieves Runtime Polymorphism using Method Overriding and Duck Typing.

You will also understand Interface-based thinking, EAFP philosophy, and how professional applications such as payment gateways, notification services, and file-processing frameworks use polymorphism to remain scalable and easy to extend.

This module prepares you for advanced topics including Abstract Base Classes (ABC), Magic Methods, Design Patterns, SOLID Principles, and Enterprise Software Architecture.
