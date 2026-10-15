# Python Object-Oriented Programming (OOP) Using Python

# Module 06 – Python Data Model (Magic Methods)

> **Course Level:** Intermediate → Advanced
>
> **Duration:** 2 Hours
>
> **Prerequisites:** Modules 01–05

---

# Module Overview

In the previous modules, we learned:

- Classes
- Objects
- Encapsulation
- Inheritance
- Polymorphism

Now we move into one of Python's most powerful and unique features:

# Python Data Model

The Python Data Model defines how objects behave inside Python.

For example,

- Why does `len(obj)` work?
- Why can we write `obj[0]`?
- Why does `print(obj)` display meaningful information?
- Why can we compare two objects using `==`?
- Why can an object be called like a function?

The answer is:

**Magic Methods (Dunder Methods).**

These methods allow user-defined classes to behave exactly like Python's built-in objects.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand the Python Data Model.
- Implement common magic methods.
- Customize object creation and destruction.
- Create iterable objects.
- Build custom containers.
- Overload operators.
- Implement callable objects.
- Create context managers.
- Design Pythonic classes.

---

# What is the Python Data Model?

The Python Data Model is a collection of special methods that define how objects interact with the Python interpreter.

These methods begin and end with double underscores (`__`), so they are often called **dunder methods** or **magic methods**.

Example:

```python
__init__
__str__
__len__
__iter__
__getitem__
```

Python automatically calls these methods in response to built-in operations.

---

# Why Do We Need Magic Methods?

Without magic methods, custom objects behave like ordinary user-defined objects with limited functionality.

With magic methods, they can:

- Print like strings.
- Behave like lists.
- Support indexing.
- Work with `len()`.
- Be iterable in `for` loops.
- Support arithmetic operators.
- Act as context managers.

---

# Categories of Magic Methods

Magic methods can be grouped into several categories:

1. Object Lifecycle
2. Object Representation
3. Container Methods
4. Iterator Methods
5. Callable Objects
6. Comparison Methods
7. Arithmetic Operators
8. Context Managers

---

# Object Lifecycle

Object lifecycle methods control how objects are created, initialized, and destroyed.

---

## `__new__()`

The first method called when an object is created.

Responsibilities:

- Allocate memory.
- Create the object.
- Return the object instance.

Usually overridden in advanced use cases such as:

- Singleton pattern
- Immutable objects
- Object caching

---

## `__init__()`

Initializes the object after it has been created.

Responsibilities:

- Assign attributes.
- Validate input.
- Prepare object state.

Most commonly used magic method.

---

## `__del__()`

Called before an object is destroyed.

Possible uses:

- Closing files
- Releasing resources
- Logging cleanup

Avoid relying on it for critical resource management because its execution time is not guaranteed.

---

# Object Representation

---

## `__str__()`

Provides a human-readable string representation.

Used by:

```python
print(obj)
```

Goal:

Readable output for end users.

---

## `__repr__()`

Provides an unambiguous representation intended for developers.

Used by:

```python
repr(obj)
```

Goal:

Useful for debugging.

---

# Container Methods

These methods allow objects to behave like built-in collections.

---

## `__len__()`

Supports:

```python
len(obj)
```

Returns the number of elements.

---

## `__getitem__()`

Supports:

```python
obj[index]
```

Allows indexing and retrieval.

---

## `__setitem__()`

Supports:

```python
obj[index] = value
```

Allows item assignment.

---

## `__contains__()`

Supports:

```python
item in obj
```

Determines membership.

---

# Truth Value Testing

---

## `__bool__()`

Defines how an object behaves in Boolean contexts.

Examples:

```python
if obj:

while obj:
```

Returns:

- `True`
- `False`

Useful for representing valid or empty states.

---

# Iterator Protocol

Iteration is one of Python's core features.

To support iteration, Python uses two magic methods.

---

## `__iter__()`

Returns an iterator object.

Called automatically when iteration begins.

---

## `__next__()`

Returns the next element.

Raises `StopIteration` when no more items remain.

Together, these methods enable:

```python
for item in obj:
```

---

# Callable Objects

---

## `__call__()`

Allows an object to behave like a function.

Example:

```python
obj()
```

Useful for:

- Function objects
- Decorators
- Machine learning models
- Configuration objects

---

# Comparison Methods

Python allows custom comparison behavior.

---

## `__eq__()`

Implements:

```python
==
```

---

## `__lt__()`

Implements:

```python
<
```

---

## `__gt__()`

Implements:

```python
>
```

---

## `__le__()`

Implements:

```python
<=
```

---

## `__ge__()`

Implements:

```python
>=
```

These methods allow custom objects to participate in sorting and comparisons.

---

# Operator Overloading

Python operators internally call magic methods.

Examples:

| Operator | Magic Method |
|----------|--------------|
| `+` | `__add__()` |
| `-` | `__sub__()` |
| `*` | `__mul__()` |
| `/` | `__truediv__()` |
| `==` | `__eq__()` |
| `<` | `__lt__()` |

Operator overloading makes custom objects feel like built-in types.

---

# Context Managers

Python provides automatic resource management through context managers.

Two methods are required.

---

## `__enter__()`

Called when entering a `with` block.

Responsible for:

- Opening resources.
- Initializing connections.

---

## `__exit__()`

Called when leaving a `with` block.

Responsible for:

- Closing resources.
- Cleaning up resources.
- Handling exceptions if necessary.

Example:

```python
with FileManager() as file:
    ...
```

---

# Real-World Applications

Magic methods are used extensively in:

- NumPy
- Pandas
- Django ORM
- SQLAlchemy
- PyTorch
- TensorFlow
- Scikit-Learn
- Flask
- FastAPI

Almost every major Python library uses the Python Data Model.

---

# Hands-on Projects

In this module, you will build:

- Custom List
- Vector Class
- Shopping Cart
- Matrix Operations
- Custom Iterator
- Context Manager
- Python Collection Class

---

# Mini Assignment

## Python Collection Class

Design a custom collection that supports:

- `len()`
- Indexing
- Assignment
- Iteration
- Membership testing
- Printing
- Equality comparison

The class should behave similarly to a built-in Python list.

---

# Best Practices

- Override only the magic methods you need.
- Keep implementations intuitive.
- Follow Python conventions.
- Ensure overloaded operators have clear meaning.
- Raise appropriate exceptions.
- Use context managers for resource handling.

---

# Common Mistakes

- Calling magic methods directly instead of using built-in operations.
- Misusing `__del__()` for important cleanup.
- Returning incorrect types from magic methods.
- Implementing inconsistent comparison methods.
- Forgetting to raise `StopIteration` in iterators.
- Overloading operators with unexpected behavior.

---

# Skills Gained

After completing this module, you will be able to:

- Understand the Python Data Model.
- Implement custom containers.
- Build iterable classes.
- Overload operators.
- Create callable objects.
- Design context managers.
- Develop Pythonic APIs.
- Make custom objects behave like built-in types.

---

# Expected Learning Outcome

By the end of this module, you will understand how Python internally interacts with objects through magic methods. You will be able to design custom classes that integrate naturally with the language, making them behave like native Python types.

These concepts form the foundation for advanced Python libraries, framework development, metaprogramming, descriptors, decorators, asynchronous programming, and professional software design.
