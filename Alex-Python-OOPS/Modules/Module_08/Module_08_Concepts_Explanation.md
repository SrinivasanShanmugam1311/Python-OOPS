# Python Object-Oriented Programming (OOP)

# Module 08 – Modern Python OOP Features

**File:** `Module_08_Concepts_Explanation.md`

**Level:** Intermediate → Advanced

**Duration:** 2 Hours

---

# Module Overview

In the previous modules, we learned **Classical Object-Oriented Programming**.

We wrote classes like this:

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age
```

Modern Python provides features that make code:

- Shorter
- Cleaner
- Faster
- More Readable
- Easier to Maintain

These features are widely used in modern frameworks like:

- Django
- FastAPI
- Pydantic
- SQLAlchemy
- Pandas
- NumPy

---

# Learning Objectives

After completing this module, you will be able to:

- Reduce boilerplate code.
- Create immutable objects.
- Save memory.
- Create constants using Enums.
- Build lightweight objects.
- Use decorators with classes.
- Cache expensive computations.
- Write better type annotations.
- Create objects using factory methods.

---

# Evolution of Python Classes

```
Traditional Classes

↓

Dataclasses

↓

Frozen Dataclasses

↓

__slots__

↓

Enums

↓

NamedTuple

↓

Cached Properties

↓

Modern Python Classes
```

---

# 1. Dataclasses

## What?

A **Dataclass** automatically generates common methods like:

- __init__()
- __repr__()
- __eq__()

You only define the data members.

---

## Why?

Without Dataclass

```
Many lines of code
```

With Dataclass

```
Few lines

Cleaner code

Less maintenance
```

---

## Benefits

- Less code
- Automatic constructor
- Better readability
- Easier debugging
- Automatic comparisons

---

## Where Used?

- Student Records
- Employee Data
- API Models
- Configuration Objects
- Database Models

---

# 2. Frozen Dataclasses

## What?

A Frozen Dataclass creates **immutable objects**.

After an object is created,

its values cannot be modified.

---

## Why?

Sometimes data should never change.

Examples

- Aadhaar Number
- Passport Details
- Product ID
- Invoice Number

---

## Benefits

- Safer objects
- Prevent accidental changes
- Thread-safe design
- Predictable behavior

---

# 3. __slots__

## What?

Normally Python stores object attributes in a dictionary.

```
Object

↓

__dict__

↓

Attributes
```

Using `__slots__` removes this dictionary.

---

## Why?

Benefits

- Uses less memory
- Faster attribute access
- Prevents adding unknown attributes

---

## Where Used?

- Millions of Objects
- Large Data Processing
- Scientific Computing
- Games
- IoT Devices

---

# 4. Enums

## What?

Enum stands for **Enumeration**.

It represents a fixed set of constant values.

Example

```
Traffic Signal

↓

RED

YELLOW

GREEN
```

---

## Why?

Instead of writing

```
status = 1

status = 2
```

Use

```
Status.ACTIVE

Status.INACTIVE
```

Much easier to understand.

---

## Where Used?

- Order Status
- Payment Status
- User Roles
- Days
- Months
- Error Codes

---

# 5. NamedTuple

## What?

NamedTuple is an immutable tuple with named fields.

Instead of

```
student[0]

student[1]
```

Use

```
student.name

student.age
```

---

## Benefits

- Readable
- Immutable
- Lightweight
- Faster than normal classes

---

## Where Used?

- Coordinates
- Records
- API Responses
- Database Rows

---

# 6. Class Decorators

## What?

A decorator modifies or enhances a class.

```
Original Class

↓

Decorator

↓

Enhanced Class
```

---

## Why?

Instead of modifying every class,

add common functionality once.

Examples

- Logging
- Validation
- Security
- Timing

---

## Where Used?

- Django
- Flask
- FastAPI
- Custom Frameworks

---

# 7. Cached Properties

## What?

Some calculations are expensive.

Instead of calculating every time,

calculate once,

store the result,

reuse it.

---

## Example

```
Area of Large Polygon

↓

First Call

↓

Calculated

↓

Stored

↓

Next Call

↓

Returned Immediately
```

---

## Benefits

- Faster applications
- Better performance
- Less CPU usage

---

# 8. Type Annotations

## What?

Type annotations describe the expected data type.

Example

```
name : str

age : int

salary : float
```

---

## Why?

They improve

- Readability
- IDE support
- Documentation
- Error detection

---

## Important

Python **does not enforce** type annotations at runtime.

They are mainly for developers and tools.

---

# 9. Forward References

## Problem

Sometimes one class refers to another class

before it is defined.

Example

```
Employee

↓

Department

↓

Employee
```

Circular references.

---

## Solution

Use Forward References.

This allows type annotations to reference classes defined later.

---

## Where Used?

- Tree Structures
- Linked Lists
- Organization Charts
- Parent-Child Objects

---

# 10. Class Factories

## What?

A Class Factory creates objects using a class method,

instead of calling the constructor directly.

Example

Instead of

```
Student(...)
```

Use

```
Student.from_dict(...)

Student.from_json(...)

Student.from_database(...)
```

---

## Benefits

- Cleaner object creation
- Multiple constructors
- Better readability
- Easier maintenance

---

# Comparison

| Feature | Purpose |
|----------|---------|
| Dataclass | Reduce Boilerplate Code |
| Frozen Dataclass | Immutable Objects |
| __slots__ | Save Memory |
| Enum | Constants |
| NamedTuple | Lightweight Immutable Records |
| Class Decorator | Enhance Classes |
| Cached Property | Performance |
| Type Annotation | Better Documentation |
| Forward Reference | Circular Type References |
| Class Factory | Flexible Object Creation |

---

# Real-World Applications

## Inventory System

- Dataclass
- Enum
- Factory Methods

---

## Hospital Records

- Frozen Dataclass
- Type Hints
- NamedTuple

---

## Student Database

- Dataclass
- Enum
- Cached Property

---

## Banking System

- Frozen Dataclass
- Enum
- Factory Methods

---

## E-Commerce

- Product Models
- Order Status
- Inventory Objects

---

# Best Practices

✅ Use Dataclasses for data models.

✅ Use Frozen Dataclasses for immutable data.

✅ Use Enums instead of magic numbers or strings.

✅ Use `__slots__` only when memory optimization is needed.

✅ Add Type Annotations to public APIs.

✅ Use Cached Properties only for expensive computations.

✅ Use Factory Methods for complex object creation.

---

# Common Mistakes

❌ Using Dataclasses for classes with complex business logic.

❌ Overusing `__slots__` without understanding its limitations.

❌ Using strings instead of Enums.

❌ Expecting Type Annotations to enforce types at runtime.

❌ Forgetting that NamedTuple objects are immutable.

❌ Recalculating expensive values instead of caching them.

---

# Skills Gained

After completing this module, you will be able to:

- Write modern Python classes.
- Reduce boilerplate code.
- Design immutable objects.
- Optimize memory usage.
- Improve application performance.
- Build maintainable enterprise applications.
- Follow modern Python coding practices.

---

# Expected Learning Outcome

By the end of this module, you will understand:

- Why Modern Python introduced Dataclasses.
- When to use Frozen Dataclasses.
- Why `__slots__` improves memory efficiency.
- How Enums make code readable.
- When NamedTuple is preferable to a class.
- How Cached Properties improve performance.
- Why Type Annotations improve developer productivity.
- How Forward References solve circular dependencies.
- Why Factory Methods simplify object creation.

These features are commonly used in modern Python applications, web frameworks, APIs, cloud services, data science libraries, and enterprise software.

---

# Next

## Module_08_Code_Examples.md (Part 1)

Topics:

- Dataclasses
- Frozen Dataclasses
- `__slots__`
- Enums
- NamedTuple
