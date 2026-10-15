# Python Object-Oriented Programming (OOP)

# Module 08 – Modern Python OOP Features

# Module_08_Code_Examples.md (Part 2)

**Level:** Intermediate → Advanced

---

# Part 2 Overview

In this part, we will learn:

- Class Decorators
- Cached Properties
- Type Annotations
- Forward References
- Class Factory Methods
- Modern Python Design

---

# 1. Class Decorators

## What is a Class Decorator?

A class decorator modifies or extends a class **without changing its source code**.

```
Original Class

↓

Decorator

↓

Enhanced Class
```

---

## Example 1 – Simple Class Decorator

```python
def logger(cls):

    print(f"{cls.__name__} Loaded")

    return cls


@logger
class Student:

    pass


student = Student()
```

### Output

```
Student Loaded
```

---

## Example 2 – Adding a New Method

```python
def add_info(cls):

    def info(self):

        print("Student Information")

    cls.info = info

    return cls


@add_info
class Student:

    pass


student = Student()

student.info()
```

### Output

```
Student Information
```

---

## Example 3 – Logging Object Creation

```python
def log_creation(cls):

    original_init = cls.__init__

    def new_init(self, *args, **kwargs):

        print("Creating Object...")

        original_init(self, *args, **kwargs)

    cls.__init__ = new_init

    return cls


@log_creation
class Employee:

    def __init__(self, name):

        self.name = name


employee = Employee("Alex")
```

Output

```
Creating Object...
```

---

# 2. Cached Property

## Problem

Some calculations take time.

Example

```
Large Report

↓

Calculate Total

↓

Every Time

↓

Slow
```

---

## Solution

Use `cached_property`.

The value is calculated **once** and reused.

---

## Example

```python
from functools import cached_property


class Rectangle:

    def __init__(self, length, width):

        self.length = length

        self.width = width


    @cached_property
    def area(self):

        print("Calculating Area...")

        return self.length * self.width


rectangle = Rectangle(20, 10)

print(rectangle.area)

print(rectangle.area)
```

Output

```
Calculating Area...

200

200
```

Notice

```
Calculated Only Once
```

---

## Another Example

```python
from functools import cached_property


class Student:

    def __init__(self, marks):

        self.marks = marks


    @cached_property
    def average(self):

        print("Computing Average")

        return sum(self.marks) / len(self.marks)


student = Student([90, 95, 85])

print(student.average)

print(student.average)
```

---

# 3. Type Annotations

Type annotations improve readability.

---

## Variables

```python
name: str = "Alex"

age: int = 25

salary: float = 45000.50

active: bool = True

print(name)
```

---

## Function

```python
def calculate_bonus(
        salary: float,
        percentage: int
) -> float:

    return salary * percentage / 100


print(calculate_bonus(50000,10))
```

---

## List

```python
numbers: list[int] = [

    10,

    20,

    30

]

print(numbers)
```

---

## Dictionary

```python
marks: dict[str,int] = {

    "Math":95,

    "Science":90

}

print(marks)
```

---

## Optional

```python
from typing import Optional


def display(name: Optional[str]):

    print(name)


display("Alex")

display(None)
```

---

# 4. Forward References

Sometimes classes reference each other.

```
Employee

↓

Department

↓

Employee
```

---

## Example

```python
from __future__ import annotations


class Employee:

    def __init__(self,
                 name: str,
                 department: Department):

        self.name = name

        self.department = department


class Department:

    def __init__(self,
                 name: str):

        self.name = name


department = Department("IT")

employee = Employee(
    "Alex",
    department
)

print(employee.department.name)
```

Output

```
IT
```

---

## Alternative

Using string annotations.

```python
class Employee:

    def __init__(
        self,
        department: "Department"
    ):

        self.department = department
```

---

# 5. Class Factory Methods

Instead of

```python
Student(...)
```

Create objects using

```
Student.from_dict()

Student.from_json()

Student.from_database()
```

---

## Example 1

```python
from dataclasses import dataclass


@dataclass
class Student:

    id: int

    name: str


    @classmethod
    def from_dict(cls, data):

        return cls(

            data["id"],

            data["name"]

        )


student = Student.from_dict({

    "id":101,

    "name":"Alex"

})

print(student)
```

---

## Example 2

```python
from dataclasses import dataclass


@dataclass
class Employee:

    id: int

    name: str

    salary: float


    @classmethod
    def from_csv(
            cls,
            text
    ):

        data = text.split(",")

        return cls(

            int(data[0]),

            data[1],

            float(data[2])

        )


employee = Employee.from_csv(

    "101,Alex,45000"

)

print(employee)
```

---

## Example 3

```python
from dataclasses import dataclass


@dataclass
class Product:

    id: int

    name: str

    price: float


    @classmethod
    def free_sample(
            cls,
            name
    ):

        return cls(

            0,

            name,

            0.0

        )


product = Product.free_sample("Laptop")

print(product)
```

---

# Mini Project

## Product Inventory System

```python
from dataclasses import dataclass
from enum import Enum


class Category(Enum):

    ELECTRONICS = "Electronics"

    GROCERY = "Grocery"

    BOOKS = "Books"


@dataclass
class Product:

    id: int

    name: str

    category: Category

    price: float

    quantity: int = 0


    @property
    def total_value(self):

        return self.price * self.quantity


    @classmethod
    def sample(cls):

        return cls(

            0,

            "Sample",

            Category.BOOKS,

            0,

            0

        )


product = Product(

    101,

    "Laptop",

    Category.ELECTRONICS,

    55000,

    5

)

print(product)

print(product.total_value)

print(Product.sample())
```

---

# Modern Python Guidelines

Instead of

```
Long Constructors
```

Use

```
Dataclass
```

---

Instead of

```
Magic Numbers
```

Use

```
Enum
```

---

Instead of

```
Repeated Calculations
```

Use

```
cached_property
```

---

Instead of

```
Many Constructors
```

Use

```
Factory Methods
```

---

Instead of

```
Missing Documentation
```

Use

```
Type Hints
```

---

# Best Practices

✅ Prefer Dataclasses for model classes.

✅ Use Enum for constants.

✅ Use cached properties for expensive computations.

✅ Add Type Hints everywhere.

✅ Use Factory Methods for alternate object creation.

✅ Keep decorators simple and reusable.

---

# Common Mistakes

❌ Using cached properties for frequently changing values.

❌ Forgetting that cached values remain unchanged until deleted.

❌ Using decorators for unrelated tasks.

❌ Writing factory methods that duplicate constructors.

❌ Ignoring Type Hints in public APIs.

---

# Summary Table

| Feature | Purpose |
|----------|---------|
| Class Decorator | Modify or extend classes |
| cached_property | Cache expensive calculations |
| Type Annotation | Improve readability |
| Forward Reference | Handle circular type references |
| Factory Method | Alternative object creation |

---

# Interview Questions

## Basic

- What is a Class Decorator?
- What is a Factory Method?
- Why use Type Hints?

---

## Intermediate

- Difference between `property` and `cached_property`?
- Why use Forward References?
- When should Factory Methods be preferred?

---

## Advanced

- Design a Product Inventory System using Dataclasses.
- Explain cached properties with a real-world example.
- How do Factory Methods improve maintainability?
- How do modern Python features reduce boilerplate code?

---

# Module 08 Summary

After completing Module 08, you can:

✅ Build concise, modern Python classes.

✅ Use Dataclasses effectively.

✅ Optimize memory with `__slots__`.

✅ Represent constants using Enums.

✅ Create immutable records with NamedTuple.

✅ Enhance classes using decorators.

✅ Cache expensive computations.

✅ Write clear Type Annotations.

✅ Handle circular references.

✅ Build flexible Factory Methods.

---

# Next Module

## Module 09 – Object-Oriented Design Principles (SOLID) & Design Patterns

Topics:

- SOLID Principles
- Dependency Injection
- Composition over Inheritance
- Creational Patterns
- Structural Patterns
- Behavioral Patterns
- Real-World Architecture
- Enterprise Design
