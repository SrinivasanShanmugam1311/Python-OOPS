# Python Object-Oriented Programming (OOP) Using Python

## Intermediate → Advanced Syllabus (Detailed)

> **Duration:** 10 Days (1–2 Hours/Day)
> **Level:** Intermediate → Advanced
> **Prerequisites:** Python Basics, Functions, Modules, Exception Handling, File Handling, Collections

---

# Module 1 – Python Object Model & Class Fundamentals

## Learning Objectives

After completing this module, you will be able to:

* Understand Python's object-oriented philosophy.
* Explain why everything in Python is an object.
* Create reusable classes.
* Understand object lifecycle.
* Differentiate class variables and instance variables.
* Understand memory references and object identity.

---

## Topics Covered

### 1. Introduction to Object-Oriented Programming

* Procedural Programming vs OOP
* Why OOP?
* Advantages
* Real-world examples
* OOP Principles Overview

---

### 2. Python Object Model

* Everything is an Object
* Objects in Memory
* Object References
* Variables as References
* Object Identity
* Object State
* Object Behavior

---

### 3. Identity vs Equality

* id()
* ==
* is
* Object comparison
* Immutable vs Mutable comparison

---

### 4. Classes and Objects

* Defining Classes
* Creating Objects
* Instance Creation
* Object Initialization
* Multiple Objects

---

### 5. Constructors

* **init**()
* Constructor Parameters
* Default Constructors
* Parameterized Constructors
* Constructor Best Practices

---

### 6. Instance Variables

* Creating Instance Variables
* Dynamic Variables
* Accessing Variables
* Updating Variables
* Deleting Variables

---

### 7. Class Variables

* Static/Class Variables
* Shared Data
* Class Namespace
* Updating Class Variables
* Difference between Instance & Class Variables

---

### 8. Methods

* Instance Methods
* Calling Methods
* self keyword
* Object Interaction

---

### 9. Object Lifecycle

* Object Creation
* Garbage Collection
* Reference Counting
* Destructor (**del**)

---

### 10. Python Introspection

* type()
* isinstance()
* dir()
* vars()
* help()
* hasattr()
* getattr()
* setattr()
* delattr()

---

### 11. Namespaces

* Local Namespace
* Global Namespace
* Class Namespace
* Object Namespace

---

### 12. Scope Resolution

* LEGB Rule
* Global Variables
* Local Variables
* nonlocal
* global keyword

---

### 13. Memory Concepts

* Reference Variables
* Memory Address
* Aliasing
* Shallow References

---

### 14. Mutable vs Immutable Objects

* Lists
* Tuples
* Strings
* Dictionaries
* Sets
* Numbers

---

## Hands-on Exercises

* Student Class
* Employee Class
* Product Class
* Mobile Class
* Book Class
* Car Class

---

## Mini Assignment

Build a **Library Book Management Class**

Features

* Add Book
* Display Book
* Update Price
* Delete Book
* Count Total Books

---

## Expected Learning Outcome

After this module you can:

* Design classes
* Create multiple objects
* Understand memory behavior
* Work confidently with constructors
* Understand how Python stores objects

---

# Module 2 – Advanced Class Design & Relationships

## Learning Objectives

* Design reusable classes.
* Model real-world relationships.
* Organize objects effectively.
* Understand object collaboration.

---

## Topics Covered

### 1. Instance Methods

* Calling
* Passing Objects
* Returning Objects

---

### 2. Class Methods

* @classmethod
* cls keyword
* Factory Methods
* Alternative Constructors

---

### 3. Static Methods

* @staticmethod
* Utility Functions
* Validation Helpers

---

### 4. Object Relationships

* Association
* Aggregation
* Composition

---

### 5. Object Collaboration

* One-to-One
* One-to-Many
* Many-to-Many

---

### 6. Nested Objects

* Object inside Object
* Passing Objects

---

### 7. Copying Objects

* Assignment
* Shallow Copy
* Deep Copy

---

### 8. Object Serialization

* pickle
* JSON Serialization Basics

---

### 9. UML Basics

* Class Diagram
* Object Diagram
* Relationships

---

### 10. Package Organization

* Multiple Python Files
* Packages
* Modules
* **init**.py

---

## Hands-on Exercises

* Department–Employee
* Hospital–Doctor–Patient
* Library–Book–Member
* School–Teacher–Student

---

## Mini Assignment

Design a **College Management System** using proper class relationships.

---

## Expected Learning Outcome

You can model real-world systems using proper OOP relationships instead of placing everything in a single class.

---

# Module 3 – Encapsulation & Data Protection

## Learning Objectives

* Protect object data.
* Validate inputs.
* Expose controlled interfaces.

---

## Topics Covered

### Encapsulation

* Public Members
* Protected Members
* Private Members
* Name Mangling

---

### Properties

* @property
* Getter
* Setter
* Deleter
* Read-only Property
* Computed Property

---

### Validation

* Input Validation
* Business Rules
* Exception Handling

---

### Data Integrity

* Prevent Invalid States
* Immutable Objects
* Controlled Updates

---

### Pythonic Design

* Avoid Java-style Getters
* Idiomatic Property Usage

---

## Hands-on

* Bank Account
* ATM
* Wallet
* Employee Salary
* Student Marks

---

## Mini Assignment

Build a **Secure Banking System** with validation and protected account operations.

---

## Expected Outcome

You can build robust classes with controlled access and validation.

---

# Module 4 – Inheritance & Method Resolution Order (MRO)

## Learning Objectives

* Reuse code through inheritance.
* Understand Python's inheritance model.
* Resolve multiple inheritance correctly.

---

## Topics Covered

* Single Inheritance
* Multiple Inheritance
* Multilevel Inheritance
* Hierarchical Inheritance
* Hybrid Inheritance
* Method Overriding
* super()
* Method Resolution Order (MRO)
* Diamond Problem
* mro()
* Cooperative Inheritance
* Best Practices
* Favor Composition vs Inheritance (when appropriate)

---

## Hands-on

* Animal Hierarchy
* Employee Hierarchy
* Vehicle System
* Shape Calculator

---

## Mini Assignment

Build a **University Staff Hierarchy** (Person → Employee → Faculty/Admin).

---

## Expected Outcome

Understand inheritance deeply and use it appropriately in real applications.

---

# Module 5 – Polymorphism & Duck Typing

## Topics Covered

* What is Polymorphism?
* Method Overriding
* Operator Polymorphism
* Duck Typing
* EAFP vs LBYL
* Interfaces (Concept)
* Runtime Polymorphism
* Composition vs Inheritance

---

## Hands-on

* Payment Gateway
* Notification System
* Report Generator
* File Reader Framework

---

## Mini Assignment

Build a **Universal Payment Processing Framework** supporting multiple payment methods.

---

# Module 6 – Python Data Model (Magic Methods)

## Topics Covered

* `__new__`
* `__init__`
* `__del__`
* `__str__`
* `__repr__`
* `__len__`
* `__bool__`
* `__iter__`
* `__next__`
* `__getitem__`
* `__setitem__`
* `__contains__`
* `__call__`
* `__eq__`
* `__lt__`, `__gt__`, `__le__`, `__ge__`
* Operator Overloading
* Context Managers (`__enter__`, `__exit__`)

---

## Hands-on

* Custom List
* Vector Class
* Shopping Cart
* Matrix Operations

---

## Mini Assignment

Create your own **Python Collection Class** that behaves like a built-in container.

---

# Module 7 – Abstract Classes, Interfaces & Type Hints

## Topics Covered

* Abstract Base Classes (ABC)
* `abc` Module
* Abstract Methods
* Interface Concepts
* Protocols (typing)
* Generic Programming (Introduction)
* Type Hints
* Static Type Checking Basics

---

## Hands-on

* Payment Framework
* Plugin Architecture
* Authentication Framework

---

## Mini Assignment

Build a **Document Processing Framework** with interchangeable processors (PDF, Word, Excel, etc.).

---

# Module 8 – Modern Python OOP Features

## Topics Covered

* Dataclasses
* Frozen Dataclasses
* `__slots__`
* Enums
* NamedTuple
* Decorators in Classes
* Cached Properties
* Type Annotations
* Forward References
* Class Factories

---

## Hands-on

* Inventory System
* Hospital Records
* Student Database

---

## Mini Assignment

Build a **Product Inventory System** using dataclasses and modern Python features.

---

# Module 9 – SOLID Principles & Design Patterns

## Topics Covered

### SOLID Principles

* Single Responsibility Principle (SRP)
* Open/Closed Principle (OCP)
* Liskov Substitution Principle (LSP)
* Interface Segregation Principle (ISP)
* Dependency Inversion Principle (DIP)

### Clean Code Principles

* DRY
* KISS
* YAGNI
* High Cohesion
* Loose Coupling

### Design Patterns

* Singleton
* Factory Method
* Abstract Factory (Overview)
* Builder
* Strategy
* Observer
* Adapter
* Facade
* Template Method (Overview)

---

## Hands-on

* Logger
* Payment Strategy
* Notification Framework
* Vehicle Factory

---

## Mini Assignment

Design a **Multi-Payment E-commerce Engine** applying SOLID principles and multiple design patterns.

---

# Module 10 – Real-World Application Architecture

## Topics Covered

* Project Folder Structure
* Packages & Modules
* Configuration Management
* Logging
* Exception Hierarchy
* Custom Exceptions
* File Organization
* Dependency Management
* Virtual Environments
* `requirements.txt`
* Documentation (`docstrings`)
* Unit Testing (`unittest`)
* Introduction to `pytest`
* Code Style (PEP 8)
* Refactoring Basics

---

## Hands-on

* Multi-module Project
* Logging Framework
* Configuration Loader
* Exception Handling Framework

---

## Capstone Project

Build a **complete, production-style application** (such as a Library Management System, Learning Management System, Hospital Management System, or E-commerce Backend) that demonstrates:

* Modular package structure
* Proper OOP design
* Encapsulation, inheritance, and polymorphism
* Abstract classes and modern Python features
* SOLID principles
* Appropriate design patterns
* Logging and custom exceptions
* Unit tests
* Clean, maintainable, and documented code

---

# Overall Learning Outcomes

After completing this syllabus, you will be able to:

* Design maintainable, object-oriented Python applications.
* Apply advanced OOP concepts to solve real-world problems.
* Understand Python's object model and data model in depth.
* Use modern Python features such as dataclasses, type hints, protocols, and context managers effectively.
* Apply SOLID principles and foundational design patterns to improve software quality.
* Structure medium- to large-scale Python projects following industry best practices.
* Build production-ready applications that provide a strong foundation for backend development, automation, data engineering, and preparation for software engineering interviews.
