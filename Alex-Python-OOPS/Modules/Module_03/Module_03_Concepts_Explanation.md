# Python Object-Oriented Programming (OOP) Using Python

# Module 03 – Encapsulation & Data Protection

> Course Level : Intermediate → Advanced
>
> Duration : 1 Day (1–2 Hours)

---

# Module Overview

In previous modules, we learned how to create classes, objects, and relationships between objects.

However, real-world software requires something more important:

**Protecting data from invalid access and accidental modification.**

Imagine a banking application.

Should anyone be allowed to directly change the account balance?

```python
account.balance = -100000
```

Obviously **No**.

Instead, the object itself should decide what is allowed.

This concept is called **Encapsulation**.

Encapsulation is one of the four pillars of Object-Oriented Programming.

It combines data and methods together while restricting direct access to sensitive information.

Python provides several mechanisms for implementing encapsulation.

---

# Learning Objectives

After completing this module, you will be able to

- Protect object data
- Hide implementation details
- Validate user input
- Create secure classes
- Prevent invalid object states
- Build Pythonic APIs using Properties
- Understand Name Mangling
- Design maintainable classes

---

# Module Contents

---

# Topic 1 — Encapsulation

---

## What is Encapsulation?

Encapsulation is the process of

- Combining data and methods into one unit (Class)

AND

- Restricting direct access to internal object data.

Simply put

> "Protect the object from invalid modifications."

---

## Why Encapsulation?

Without encapsulation

Anyone can modify object data.

Example

```
Employee Salary = -50000

Age = -10

Marks = 500

Account Balance = -10000
```

These values should never exist.

Encapsulation prevents such situations.

---

## Advantages

- Data Protection
- Better Security
- Better Maintainability
- Controlled Access
- Validation
- Easy Refactoring
- Loose Coupling

---

# Topic 2 — Public Members

---

## What are Public Members?

Public members are accessible from anywhere.

Python variables are public by default.

Example

```
student.name

student.age
```

---

## Characteristics

- No restrictions
- Easy access
- Suitable for non-sensitive information

---

## Examples

- Student Name
- Book Title
- Product Name

---

## When to Use?

Use public members for

- Read-only data
- General information
- Display purposes

---

# Topic 3 — Protected Members

---

## What are Protected Members?

Protected members indicate

> "This member is intended for internal use."

Python uses

```
_single_underscore
```

Example

```
_balance
```

---

## Important

Python does **not** enforce protection.

It is only a convention.

Developers are expected to respect it.

---

## Usage

Used mainly in

- Parent Classes
- Child Classes

---

## Advantages

- Better code readability
- Indicates internal implementation
- Supports inheritance

---

# Topic 4 — Private Members

---

## What are Private Members?

Private members should not be accessed directly outside the class.

Python uses

```
__double_underscore
```

Example

```
__salary

__balance

__password
```

---

## Why Private?

Protect

- Passwords
- Account Balance
- Credit Card Details
- PIN Numbers
- Internal Algorithms

---

## Advantages

- Better Security
- Better Validation
- Prevents accidental modification

---

# Topic 5 — Name Mangling

---

## What is Name Mangling?

Python does not create truly private variables.

Instead it renames them internally.

Example

```
__salary
```

becomes

```
_ClassName__salary
```

Example

```
Employee

↓

_Employee__salary
```

---

## Why?

Avoid accidental access.

Avoid name conflicts in inheritance.

---

## Important

Name Mangling is **not** encryption.

It is only name transformation.

---

# Topic 6 — Properties

---

## What are Properties?

Properties provide controlled access to object attributes.

Instead of directly accessing variables

```
employee.salary
```

Python internally executes methods.

This allows validation without changing program syntax.

---

## Why Properties?

Without properties

```
employee.salary = -5000
```

No validation.

With properties

Validation happens automatically.

---

## Components

### Getter

Returns value.

---

### Setter

Updates value after validation.

---

### Deleter

Deletes data safely.

---

### Read-only Property

Only getter.

Cannot modify value.

---

### Computed Property

Value is calculated dynamically.

Example

```
BMI

Age

Interest

Tax

Percentage
```

---

# Topic 7 — Validation

---

## What is Validation?

Validation ensures data satisfies predefined rules.

Examples

Age

```
0 - 120
```

Marks

```
0 - 100
```

Salary

```
> 0
```

Password

Minimum length.

---

## Why Validation?

Prevents invalid data.

Maintains data quality.

Improves application security.

---

## Business Rules

Business Rules are application-specific validations.

Examples

Bank

Minimum Balance

Hospital

Patient Age

School

Passing Marks

Shopping

Minimum Order Amount

---

## Exception Handling

Validation failures should raise exceptions.

Examples

```
ValueError

TypeError

RuntimeError
```

---

# Topic 8 — Data Integrity

---

## What is Data Integrity?

Data Integrity means

Stored information always remains valid.

Example

```
Balance

1000
```

Should never become

```
-999999
```

unless business rules allow it.

---

## Techniques

- Validation
- Encapsulation
- Properties
- Read-only Fields
- Controlled Updates

---

# Topic 9 — Immutable Objects

---

## What are Immutable Objects?

Once created

Their state cannot change.

Examples

```
tuple

str

frozenset
```

Custom immutable classes can also be created.

---

## Advantages

- Thread Safe
- Predictable
- Reliable

---

# Topic 10 — Controlled Updates

---

Instead of

```
employee.salary=90000
```

Use

```
employee.increment_salary()
```

Benefits

- Validation
- Logging
- Business Rules
- Security

---

# Topic 11 — Pythonic Design

---

Python encourages

Simple APIs.

Instead of Java

```
getSalary()

setSalary()
```

Python prefers

```
employee.salary
```

using

```
@property
```

Internally

Getter

Setter

Validation

are executed automatically.

---

# Why Avoid Java-style Getters?

Python values

Readability.

Simple syntax.

Cleaner APIs.

Less boilerplate.

---

# Hands-on Programs

Students will implement

- Bank Account
- ATM
- Wallet
- Employee Salary
- Student Marks
- Product Inventory
- Hospital Patient Record

---

# Mini Assignment

Build

## Secure Banking System

Requirements

- Private Balance
- Deposit
- Withdraw
- Validation
- PIN Verification
- Minimum Balance
- Read-only Account Number
- Transaction History

---

# Skills Gained

After completing this module

You can

- Protect object data
- Design secure classes
- Validate user input
- Use properties correctly
- Build Pythonic APIs
- Create maintainable software
- Prevent invalid states
- Design enterprise-ready objects

---

# Expected Learning Outcome

After completing Module 03

You will be able to build secure, maintainable, and well-designed Python classes using encapsulation, properties, validation, and controlled data access.

This module provides the foundation for developing robust enterprise applications where data integrity and security are essential.
