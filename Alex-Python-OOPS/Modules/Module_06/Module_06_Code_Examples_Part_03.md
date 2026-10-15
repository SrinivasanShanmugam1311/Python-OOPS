# Python Object-Oriented Programming (OOP)

# Module 06 – Python Data Model (Magic Methods)

# Module_06_Code_Examples.md (Part 3)

**Course Level:** Intermediate → Advanced

---

# Comparison Magic Methods

Python uses magic methods for comparison operators.

| Operator | Magic Method |
|----------|--------------|
| == | __eq__() |
| != | __ne__() |
| < | __lt__() |
| <= | __le__() |
| > | __gt__() |
| >= | __ge__() |

---

# 1. __eq__()

## Purpose

Defines equality between two objects.

---

## Example

```python
class Student:

    def __init__(self, roll):
        self.roll = roll

    def __eq__(self, other):
        return self.roll == other.roll


s1 = Student(101)
s2 = Student(101)
s3 = Student(102)

print(s1 == s2)
print(s1 == s3)
```

Output

```
True
False
```

---

# 2. __lt__(), __gt__(), __le__(), __ge__()

```python
class Product:

    def __init__(self, price):
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product(500)
p2 = Product(800)

print(p1 < p2)
print(p1 > p2)
```

Output

```
True
False
```

---

# Operator Overloading

Python operators internally call magic methods.

| Operator | Magic Method |
|----------|--------------|
| + | __add__() |
| - | __sub__() |
| * | __mul__() |
| / | __truediv__() |

---

# 3. Vector Class

```python
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(2, 4)
v2 = Vector(6, 8)

print(v1 + v2)
```

Output

```
(8, 12)
```

---

# 4. Matrix Addition

```python
class Matrix:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):

        result = []

        for r1, r2 in zip(self.value, other.value):

            row = []

            for c1, c2 in zip(r1, r2):
                row.append(c1 + c2)

            result.append(row)

        return Matrix(result)

    def __str__(self):
        return str(self.value)


m1 = Matrix([
    [1,2],
    [3,4]
])

m2 = Matrix([
    [5,6],
    [7,8]
])

print(m1 + m2)
```

Output

```
[[6, 8], [10, 12]]
```

---

# 5. Shopping Cart

```python
class Cart:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        return f"Cart : {self.items}"


cart = Cart()

cart.add("Laptop")
cart.add("Mouse")

print(cart)

print(len(cart))

print("Laptop" in cart)
```

Output

```
Cart : ['Laptop', 'Mouse']
2
True
```

---

# Context Managers

Magic Methods

```
__enter__()

↓

Resource

↓

__exit__()
```

Used with

```python
with
```

statement.

---

# 6. __enter__() and __exit__()

```python
class Database:

    def __enter__(self):

        print("Database Connected")

        return self

    def query(self):

        print("Executing Query")

    def __exit__(self,
                 exc_type,
                 exc_value,
                 traceback):

        print("Database Closed")


with Database() as db:

    db.query()
```

Output

```
Database Connected
Executing Query
Database Closed
```

---

# Another Context Manager

```python
class FileManager:

    def __enter__(self):

        print("Opening File")

        return self

    def write(self):

        print("Writing Data")

    def __exit__(self,
                 exc_type,
                 exc_value,
                 traceback):

        print("Closing File")


with FileManager() as file:

    file.write()
```

---

# Mini Project

# Python Collection Class

```python
class MyCollection:

    def __init__(self):

        self.data = []

    def add(self, value):

        self.data.append(value)

    def __len__(self):

        return len(self.data)

    def __getitem__(self, index):

        return self.data[index]

    def __setitem__(self, index, value):

        self.data[index] = value

    def __contains__(self, item):

        return item in self.data

    def __iter__(self):

        return iter(self.data)

    def __str__(self):

        return str(self.data)


collection = MyCollection()

collection.add("Python")
collection.add("Java")
collection.add("C++")

print(collection)

print(len(collection))

print(collection[1])

collection[1] = "JavaScript"

print(collection)

print("Python" in collection)

for item in collection:
    print(item)
```

Output

```
['Python', 'Java', 'C++']
3
Java
['Python', 'JavaScript', 'C++']
True
Python
JavaScript
C++
```

---

# Real-World Uses

Python Data Model powers

- list
- tuple
- dict
- set
- pathlib
- pandas
- numpy
- sqlalchemy
- django ORM
- pytorch tensors

Almost every major Python library uses these magic methods.

---

# Best Practices

✅ Override only meaningful operators.

✅ Keep comparison methods consistent.

✅ Always return appropriate data types.

✅ Use context managers for resource handling.

✅ Follow Python's built-in behavior.

---

# Common Mistakes

❌ Returning incorrect types.

❌ Forgetting `StopIteration`.

❌ Misusing `__del__()`.

❌ Overloading operators with unexpected meanings.

❌ Implementing inconsistent comparison logic.

---

# Interview Questions

## Basic

- What are Magic Methods?
- Difference between `__str__()` and `__repr__()`?
- What is operator overloading?

---

## Intermediate

- Explain `__call__()`.
- Explain Context Managers.
- Difference between `__getitem__()` and `__iter__()`?

---

## Advanced

- Design a custom collection class.
- How does `with` work internally?
- Explain Python's Data Model.
- Why are magic methods important for frameworks like NumPy and Pandas?

---

# Module Summary

After completing Module 06, you can:

✅ Understand Python's Data Model.

✅ Implement object lifecycle methods.

✅ Customize object representation.

✅ Create iterable objects.

✅ Build custom containers.

✅ Implement callable objects.

✅ Overload comparison operators.

✅ Overload arithmetic operators.

✅ Create context managers.

✅ Design Pythonic classes that behave like built-in objects.

---

# Module Completion

You have completed one of the most advanced Python OOP modules.

These concepts are heavily used in:

- NumPy
- Pandas
- Django
- Flask
- FastAPI
- SQLAlchemy
- PyTorch
- TensorFlow

Understanding this module prepares you for professional Python development and advanced library design.

---

# Next Module

## Module 07 – Abstract Base Classes (ABC), Interfaces & SOLID Principles

Topics:

- abc Module
- ABC Class
- @abstractmethod
- Abstract Properties
- Interface Design
- Multiple Abstract Classes
- SOLID Principles
- Dependency Injection
- Enterprise Architecture
- Real-world Framework Design
