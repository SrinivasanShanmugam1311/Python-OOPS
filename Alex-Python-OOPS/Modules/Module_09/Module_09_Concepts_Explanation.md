# Python Object-Oriented Programming (OOP)

# Module 09 – SOLID Principles & Design Patterns

**File:** Module_09_Concepts_Explanation.md

**Level:** Advanced

**Prerequisites:**

- OOP Fundamentals
- Inheritance
- Polymorphism
- Abstract Classes
- Design Relationships

---

# Module Overview

Writing classes is easy.

Designing classes that survive years of changes is difficult.

Professional software requires:

- Maintainability
- Scalability
- Flexibility
- Reusable Components

SOLID principles and Design Patterns help us achieve this.

---

# Why SOLID?

Imagine an e-commerce application.

Today:

```
Payment

↓

Credit Card
```

Tomorrow:

```
Payment

↓

Credit Card

UPI

Wallet

Net Banking

Crypto
```

Poor design requires changing existing code every time.

Good design allows adding features without breaking old code.

---

# Software Design Evolution

```
Working Code

↓

Clean Code

↓

SOLID Principles

↓

Design Patterns

↓

Enterprise Architecture
```

---

# PART 1 – SOLID PRINCIPLES

SOLID is a collection of five design principles.

```
S → Single Responsibility

O → Open Closed

L → Liskov Substitution

I → Interface Segregation

D → Dependency Inversion
```

---

# 1. Single Responsibility Principle (SRP)

## Definition

A class should have:

```
One Reason To Change
```

Meaning:

One class should perform one responsibility.

---

## Bad Design

```python
class Invoice:

    def calculate_total(self):
        pass

    def save_database(self):
        pass

    def send_email(self):
        pass
```

Problem:

Three responsibilities:

```
Calculation

Database

Email
```

Any change affects this class.

---

## Good Design

```
Invoice

↓

InvoiceCalculator


InvoiceRepository


EmailService
```

Each class has one job.

---

## Benefits

- Easier testing
- Easier maintenance
- Less coupling

---

# 2. Open Closed Principle (OCP)

## Definition

Software entities should be:

```
Open for Extension

Closed for Modification
```

Meaning:

Add new features without changing existing code.

---

## Bad Example

```python
class Payment:

    def pay(self,type):

        if type=="UPI":
            pass

        elif type=="CARD":
            pass
```

Every new payment requires modifying this class.

---

## Good Design

```
Payment Interface

↓

UPI Payment

Card Payment

Wallet Payment
```

Add new classes instead of changing existing code.

---

# 3. Liskov Substitution Principle (LSP)

## Definition

Child classes should replace parent classes without breaking the application.

---

Example:

```
Bird

↓

Flying Bird
```

Problem:

Penguin cannot fly.

Wrong inheritance:

```
Bird

↓

Penguin
```

Better:

```
Bird

↓

FlyingBird

SwimmingBird
```

---

# 4. Interface Segregation Principle (ISP)

## Definition

Clients should not depend on methods they don't use.

---

Bad:

```python
class Machine:

    def print():
        pass

    def scan():
        pass

    def fax():
        pass
```

A simple printer does not need fax.

---

Better:

```
Printer Interface

Scanner Interface

Fax Interface
```

Small focused interfaces.

---

# 5. Dependency Inversion Principle (DIP)

## Definition

High-level modules should not depend on low-level modules.

Both should depend on abstractions.

---

Bad:

```
Order

↓

MySQL Database
```

Good:

```
Order

↓

Database Interface

↓

MySQL

MongoDB

PostgreSQL
```

---

# PART 2 – Clean Code Principles

---

# DRY

## Don't Repeat Yourself

Avoid duplicate code.

Bad:

```
Calculate Tax

Calculate Tax

Calculate Tax
```

Create reusable function.

---

# KISS

## Keep It Simple

Simple solutions are easier to maintain.

Avoid unnecessary complexity.

---

# YAGNI

## You Aren't Gonna Need It

Do not build features before they are required.

---

# High Cohesion

A class should contain related functionality.

Example:

Good:

```
PaymentService

↓

Payment Methods
```

Bad:

```
PaymentService

↓

Email

↓

Database

↓

Report
```

---

# Loose Coupling

Objects should depend less on each other.

Good:

```
Order

↓

Payment Interface

↓

UPI
```

---

# PART 3 – Design Patterns

Design Patterns are proven solutions to common software problems.

---

# 1. Singleton Pattern

## Purpose

Only one object should exist.

Example:

```
Application Logger

Database Connection

Configuration Manager
```

---

## Usage

```
Logger Instance

↓

All Modules Share Same Logger
```

---

# 2. Factory Method

## Purpose

Create objects without exposing creation logic.

Example:

Instead of:

```
Car()

Bike()
```

Use:

```
VehicleFactory.create()
```

---

Benefits:

- Centralized creation
- Easy extension

---

# 3. Abstract Factory

## Purpose

Create families of related objects.

Example:

```
GUI Factory

↓

Windows Button

Windows Menu


Mac Button

Mac Menu
```

---

# 4. Builder Pattern

## Purpose

Create complex objects step-by-step.

Example:

```
Computer

↓

CPU

RAM

Storage

Graphics Card
```

---

# 5. Strategy Pattern

## Purpose

Change behavior dynamically.

Example:

Payment:

```
Credit Card Strategy

UPI Strategy

Wallet Strategy
```

---

# 6. Observer Pattern

## Purpose

Notify multiple objects when something changes.

Example:

```
YouTube Channel

↓

Subscribers
```

---

# 7. Adapter Pattern

## Purpose

Make incompatible objects work together.

Example:

```
Old Payment API

↓

Adapter

↓

New System
```

---

# 8. Facade Pattern

## Purpose

Provide a simple interface to complex systems.

Example:

```
Online Shopping

↓

Payment

Inventory

Shipping

Notification
```

User sees one simple operation.

---

# 9. Template Method

## Purpose

Define algorithm structure but allow subclasses to customize steps.

Example:

```
Data Processing

↓

Read Data

Process Data

Save Data
```

---

# Real World Applications

## Logger

Uses:

- Singleton

---

## Payment System

Uses:

- Strategy
- Factory
- SOLID

---

## Notification System

Uses:

- Observer
- Strategy

---

## Vehicle Factory

Uses:

- Factory Method
- Abstract Factory

---

# Mini Project

# Multi-Payment E-Commerce Engine

Design:

```
Order

↓

Payment Interface

↓

UPI

Credit Card

Wallet


↓

Notification

↓

Email

SMS
```

Applying:

- SRP
- OCP
- DIP
- Strategy Pattern
- Factory Pattern

---

# Best Practices

✅ Prefer composition over inheritance.

✅ Depend on abstractions.

✅ Keep classes small.

✅ Use patterns only when required.

✅ Avoid unnecessary complexity.

---

# Common Mistakes

❌ Creating patterns everywhere.

❌ Deep inheritance trees.

❌ Huge classes.

❌ Tight coupling.

❌ Violating SRP.

---

# Learning Outcome

After completing this module:

You can:

- Design scalable OOP systems.
- Apply SOLID principles.
- Select suitable design patterns.
- Build maintainable architectures.
- Think like a professional Python developer.

---

# Next

## Module_09_Code_Examples_Part_1

Topics:

- SRP
- OCP
- LSP
- ISP
- DIP
- Clean Code Examples
