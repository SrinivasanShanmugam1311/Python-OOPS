# Python Object-Oriented Programming (OOP) Using Python

# Module 02 – Advanced Class Design & Relationships

**Course Level:** Intermediate → Advanced

**Module Duration:** 1 Day (1–2 Hours)

**Prerequisites**

- Python Basics
- Classes and Objects
- Constructors
- Instance Variables
- Class Variables
- Methods

---

# Module Overview

In Module 01, you learned how to create classes and objects.

In this module, you will learn **how professional software engineers design objects that work together** to build real-world applications.

Instead of writing isolated classes, you will learn how multiple classes collaborate, communicate, and form scalable software architectures.

This module introduces object relationships, reusable class design, class methods, static methods, serialization, UML basics, and package organization.

---

# Learning Objectives

After completing this module, you will be able to:

- Design reusable classes.
- Create maintainable object-oriented applications.
- Understand object collaboration.
- Build proper relationships between classes.
- Organize projects using packages and modules.
- Serialize Python objects.
- Read simple UML diagrams.

---

# Module Contents

---

# Topic 1 – Instance Methods

## What are Instance Methods?

Instance methods are methods that belong to an individual object.

Every object has its own copy of instance data, and instance methods operate on that data.

Instance methods always receive the object itself as the first parameter (`self`).

---

## Why Do We Need Instance Methods?

Without instance methods, objects cannot manipulate or access their own data.

They provide behaviour to an object.

Example

Student

- enroll()
- display()
- calculate_grade()

Employee

- calculate_salary()
- promote()
- display()

---

## Concepts Covered

- Defining instance methods
- Calling instance methods
- self keyword
- Accessing instance variables
- Passing objects to methods
- Returning objects
- Object interaction
- Chaining methods

---

## Real-world Usage

- Banking Systems
- Hospital Management
- E-Commerce
- Student Management

---

# Topic 2 – Class Methods

## What are Class Methods?

Class methods belong to the class rather than individual objects.

They operate on class-level data.

Class methods receive `cls` instead of `self`.

---

## Why Do We Need Class Methods?

Sometimes operations belong to the class itself instead of any particular object.

Examples

- Counting total objects
- Creating objects
- Loading configuration
- Managing shared resources

---

## Concepts Covered

- @classmethod
- cls keyword
- Accessing class variables
- Updating shared data
- Factory Methods
- Alternative Constructors

---

## Real-world Usage

- Database Connection Factory
- User Creation
- Configuration Loader
- Singleton Initialization

---

# Topic 3 – Static Methods

## What are Static Methods?

Static methods belong to the class but do not use either `self` or `cls`.

They behave like normal functions grouped logically inside a class.

---

## Why Do We Need Static Methods?

Sometimes a function is related to a class but does not require object data.

Examples

- Validation
- Calculations
- Utility Functions
- Helper Functions

---

## Concepts Covered

- @staticmethod
- Utility methods
- Validation helpers
- Data conversion
- Formatting helpers

---

## Real-world Usage

- Email validation
- Password validation
- Tax calculation
- Discount calculation

---

# Topic 4 – Object Relationships

Real-world software rarely consists of one class.

Objects interact with other objects.

Python supports several relationship models.

---

## Association

Association is a relationship where two independent objects communicate.

Both objects can exist independently.

Example

Teacher ↔ Student

Customer ↔ Bank

Doctor ↔ Patient

---

### Characteristics

- Loose coupling
- Independent lifecycle
- One-to-One
- One-to-Many
- Many-to-Many

---

## Aggregation

Aggregation represents a "Has-A" relationship.

One object contains another object.

However, contained objects can exist independently.

Example

Department has Employees.

Library has Books.

University has Students.

Deleting the Department does not delete Employees.

---

### Characteristics

- Weak ownership
- Independent lifecycle
- Reusable objects

---

## Composition

Composition is a stronger "Has-A" relationship.

Contained objects cannot exist without the parent.

Example

House → Room

Car → Engine

Human → Heart

If the parent object is destroyed, the child objects are also destroyed.

---

### Characteristics

- Strong ownership
- Tight relationship
- Dependent lifecycle

---

## Difference Between Relationships

Association

- Uses another object

Aggregation

- Has another object

Composition

- Owns another object

---

# Topic 5 – Object Collaboration

Large software systems require multiple objects working together.

Instead of creating one giant class, responsibilities are distributed.

---

## Collaboration Types

### One-to-One

Example

Person → Passport

Employee → Laptop

---

### One-to-Many

Example

Department → Employees

Library → Books

Course → Students

---

### Many-to-Many

Example

Students ↔ Courses

Doctors ↔ Patients

Actors ↔ Movies

---

## Benefits

- Modular design
- Better maintenance
- Easy testing
- Better scalability

---

# Topic 6 – Nested Objects

Objects can contain other objects.

Instead of storing primitive values, an object stores another object.

Example

Employee

contains

Address

which contains

City

---

## Benefits

- Better organization
- Better encapsulation
- Real-world modelling

---

## Concepts Covered

- Object inside object
- Passing objects
- Nested constructors
- Object traversal

---

# Topic 7 – Copying Objects

Copying objects is different from copying primitive values.

Python supports multiple copying techniques.

---

## Assignment

Both variables point to the same object.

Changes affect both variables.

---

## Shallow Copy

Copies only the outer object.

Nested objects remain shared.

---

## Deep Copy

Creates completely independent objects.

Nested objects are also copied.

---

## Concepts Covered

- copy()
- deepcopy()
- Mutable vs Immutable behaviour
- Reference sharing

---

# Topic 8 – Object Serialization

Serialization converts Python objects into a format suitable for storage or transmission.

---

## Why Serialization?

Save objects

Transfer objects

Store objects

Reload objects later

---

## Topics Covered

### Pickle

- Serialization
- Deserialization
- Saving Objects
- Loading Objects

---

### JSON

- JSON Basics
- Converting objects
- Dictionary mapping
- API communication

---

## Real-world Usage

- Save configuration
- Machine Learning models
- Caching
- REST APIs

---

# Topic 9 – UML Basics

Professional software is designed before coding.

UML provides a visual representation.

---

## Topics Covered

### Class Diagram

Represents

- Classes
- Attributes
- Methods

---

### Object Diagram

Represents

Actual object instances

---

### Relationships

Association

Aggregation

Composition

Inheritance

Dependency

---

## Benefits

- Better communication
- Better documentation
- Better architecture

---

# Topic 10 – Package Organization

Large applications should never be written in one file.

Python provides packages and modules for organizing code.

---

## Modules

Single Python file

Example

student.py

employee.py

bank.py

---

## Packages

Collection of related modules.

Example

college/

student.py

teacher.py

course.py

---

## __init__.py

Marks a directory as a package.

Can expose selected classes.

Can initialize package variables.

---

## Imports

Absolute Import

Relative Import

Selective Import

Package Import

---

## Benefits

- Better organization
- Reusability
- Maintainability
- Scalability

---

# Real-world Systems Covered

Throughout this module, concepts will be demonstrated using:

- Student Management System
- College Management System
- Hospital Management System
- Banking System
- Library Management System
- Employee Management System
- E-Commerce System

---

# Skills Gained

After completing this module, you will be able to:

- Design reusable classes.
- Use instance, class, and static methods correctly.
- Apply Association, Aggregation, and Composition.
- Model object collaboration.
- Create nested object structures.
- Copy objects safely.
- Serialize Python objects.
- Read simple UML diagrams.
- Organize Python projects using packages and modules.

---

# Mini Assignment

Design a **College Management System** using:

- Student
- Teacher
- Department
- Course
- Classroom
- Address
- Library

Apply:

- Instance Methods
- Class Methods
- Static Methods
- Association
- Aggregation
- Composition
- Nested Objects
- Packages

---

# Expected Learning Outcome

After completing Module 02, you will be able to design medium-sized Python applications using proper object-oriented relationships and industry-standard project organization instead of writing isolated or tightly coupled classes.
