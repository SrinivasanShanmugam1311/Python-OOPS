# Python Object-Oriented Programming (OOP)

# Module 10 – Real-World Application Architecture

**File:** Module_10_Concepts_Explanation.md

**Level:** Advanced

---

# Module Overview

Writing classes is only one part of software development.

Professional applications require:

- Organized code
- Multiple modules
- Error handling
- Logging
- Testing
- Documentation
- Dependency management

A real project is not:

```
main.py
```

It is:

```
Project

│

├── Modules

├── Packages

├── Configuration

├── Tests

├── Logs

└── Documentation
```

---

# Learning Objectives

After completing this module, you will understand:

- How professional Python projects are organized.
- How to create packages and modules.
- How to manage project configuration.
- How to handle application errors.
- How to create custom exceptions.
- How logging works.
- How testing improves quality.
- How to write maintainable Python code.

---

# 1. Project Folder Structure

## Why Structure Matters?

Small programs can have one file.

Large applications need separation.

---

## Bad Structure

```
project

main.py
```

Problem:

Everything becomes mixed:

- Business logic
- Database
- UI
- Configuration

---

## Professional Structure

Example:

```
 ecommerce_app

│

├── app

│   ├── models

│   ├── services

│   ├── repositories

│   ├── exceptions

│   └── utils

│

├── config

│

├── tests

│

├── logs

│

├── requirements.txt

│

└── main.py
```

---

# 2. Packages & Modules

## Module

A Python file.

Example:

```
student.py
```

contains:

```python
class Student:
    pass
```

---

## Package

Collection of modules.

Example:

```
school

│

├── student.py

├── teacher.py

└── course.py
```

---

## Why Packages?

Benefits:

- Reusable code
- Better organization
- Easy maintenance

---

# 3. Configuration Management

## Problem

Hard coding values:

```python
database="mysql"
password="12345"
```

is bad.

---

## Better Approach

Store configuration separately.

Example:

```
config.json

database

username

password
```

Application reads configuration.

---

## Benefits

- Security
- Easy changes
- Different environments

Examples:

```
Development

Testing

Production
```

---

# 4. Logging

## What is Logging?

Recording application events.

Example:

```
User Login

Payment Success

Database Error
```

---

## Why Logging?

Instead of:

```python
print("Error")
```

Use:

```
INFO
WARNING
ERROR
CRITICAL
```

---

## Logging Levels

| Level | Purpose |
|-|-|
| DEBUG | Detailed information |
| INFO | Normal events |
| WARNING | Possible issue |
| ERROR | Failure |
| CRITICAL | Serious failure |

---

# 5. Exception Hierarchy

Python exceptions follow hierarchy.

```
BaseException

      |

Exception

      |

ValueError

TypeError

FileNotFoundError
```

---

# Why Exception Hierarchy?

Allows:

- Better error handling
- Custom error categories
- Cleaner code

---

# 6. Custom Exceptions

## Why?

Built-in exceptions may not describe business problems.

Example:

Banking:

```
Insufficient Balance

Invalid Account

Payment Failed
```

---

## Custom Exception

```python
class InsufficientBalance(Exception):

    pass
```

Now errors are meaningful.

---

# 7. Dependency Management

## What?

Managing external libraries.

Example:

```
Django

Flask

Requests

Pandas
```

---

## requirements.txt

Stores dependencies.

Example:

```
django==5.0

requests==2.31

pandas==2.0
```

---

# 8. Virtual Environment

## Problem

Different projects need different package versions.

Example:

```
Project A

Django 4


Project B

Django 5
```

---

## Solution

Virtual Environment.

Structure:

```
Project

|

venv

|

Packages
```

---

# 9. Documentation

## Docstrings

Explain:

- What function does
- Parameters
- Return value

Example:

```python
def add(a,b):
    """
    Adds two numbers.

    Returns:
        Sum
    """

    return a+b
```

---

# 10. Unit Testing

## Why Testing?

Manual testing is slow.

Automated testing checks code automatically.

---

## Unit Test

Testing a small piece.

Example:

```
Function

↓

Input

↓

Expected Output
```

---

# unittest

Python built-in testing framework.

Example:

```python
import unittest
```

---

# pytest Introduction

pytest provides:

- Simple syntax
- Better reporting
- Fixtures
- Plugins

---

# 11. Code Style (PEP 8)

PEP 8 defines Python coding standards.

Examples:

Good:

```python
student_name
```

Bad:

```python
StudentName
```

---

## Rules

- Meaningful names
- Proper indentation
- Line length control
- Clean imports

---

# 12. Refactoring Basics

## What?

Improving existing code without changing behavior.

---

Example:

Before:

```python
def calculate():
    pass
```

After:

```python
def calculate_salary():
    pass
```

---

# Refactoring Goals

Improve:

- Readability
- Performance
- Maintainability

---

# Hands-On Projects

---

# Project 1: Multi Module Application

Structure:

```
Application

|

Models

Services

Repositories

Utils
```

Learn:

- Packages
- Imports
- Architecture

---

# Project 2: Logging Framework

Features:

- Logger class
- File logging
- Error logging
- Multiple levels

Concepts:

- Singleton
- File handling
- Exceptions

---

# Project 3: Configuration Loader

Features:

- Load JSON configuration
- Environment settings
- Validation

Concepts:

- Dataclasses
- Factory methods

---

# Project 4: Exception Framework

Features:

Custom exceptions:

```
DatabaseError

ValidationError

PaymentError
```

---

# Real World Architecture

Typical enterprise application:

```
Client

 |

API Layer

 |

Service Layer

 |

Repository Layer

 |

Database
```

---

# Best Practices

✅ Separate responsibilities.

✅ Keep configuration outside code.

✅ Use logging instead of print.

✅ Create meaningful exceptions.

✅ Write tests.

✅ Document public functions.

✅ Follow PEP 8.

---

# Common Mistakes

❌ One huge Python file.

❌ Hard-coded passwords.

❌ Using print for debugging.

❌ Ignoring exceptions.

❌ No testing.

❌ Poor naming.

---

# Module 10 Outcome

After completing this module:

You can:

✅ Create professional Python project structures.

✅ Build multi-file applications.

✅ Manage dependencies.

✅ Handle production errors.

✅ Create logging systems.

✅ Write tested maintainable code.

✅ Follow industry Python practices.

---

# Next

## Module_10_Code_Examples.md

Topics:

- Project Structure
- Packages
- Configuration Loader
- Logging Framework
- Custom Exceptions
- Unit Testing
- Multi-module Application
