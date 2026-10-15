# Python Object-Oriented Programming (OOP)

# Module 08 – Modern Python OOP Features

# Module_08_Code_Examples.md (Part 1)

**Level:** Intermediate → Advanced

---

# 1. Dataclasses

## Traditional Class

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __repr__(self):

        return f"Student({self.name}, {self.age})"


student = Student("Alex", 22)

print(student)
```

Output

```
Student(Alex, 22)
```

---

## Dataclass Version

```python
from dataclasses import dataclass

@dataclass
class Student:

    name: str
    age: int


student = Student("Alex", 22)

print(student)
```

Output

```
Student(name='Alex', age=22)
```

---

## What Dataclass Generates

Automatically creates:

- `__init__()`
- `__repr__()`
- `__eq__()`

No need to write them manually.

---

## Equality Example

```python
from dataclasses import dataclass

@dataclass
class Student:

    id: int
    name: str


s1 = Student(101, "Alex")
s2 = Student(101, "Alex")

print(s1 == s2)
```

Output

```
True
```

---

## Default Values

```python
from dataclasses import dataclass

@dataclass
class Employee:

    name: str
    salary: float = 30000


employee = Employee("John")

print(employee)
```

Output

```
Employee(name='John', salary=30000)
```

---

## Using field()

```python
from dataclasses import dataclass
from dataclasses import field

@dataclass
class Product:

    name: str

    quantity: int = field(default=1)

    price: float = field(default=0.0)


product = Product("Laptop")

print(product)
```

---

## Using default_factory

```python
from dataclasses import dataclass
from dataclasses import field

@dataclass
class ShoppingCart:

    items: list = field(default_factory=list)


cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.items.append("Laptop")

print(cart1.items)

print(cart2.items)
```

Output

```
['Laptop']
[]
```

Why?

Each object gets its own list.

---

## __post_init__()

Executed after `__init__()`.

```python
from dataclasses import dataclass

@dataclass
class Student:

    name: str

    marks: int

    grade: str = ""

    def __post_init__(self):

        if self.marks >= 90:
            self.grade = "A"
        elif self.marks >= 75:
            self.grade = "B"
        else:
            self.grade = "C"


student = Student("Alex", 92)

print(student)
```

Output

```
Student(name='Alex', marks=92, grade='A')
```

---

# 2. Frozen Dataclasses

## Immutable Objects

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Employee:

    id: int
    name: str


employee = Employee(101, "Alex")

print(employee)
```

---

## Attempt to Modify

```python
employee.name = "John"
```

Output

```
FrozenInstanceError
```

---

## Real-World Example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Aadhaar:

    number: str

    owner: str


card = Aadhaar(

    "1234-5678-9012",

    "Alex"

)

print(card)
```

---

# 3. __slots__

## Normal Class

```python
class Student:

    def __init__(self):

        self.name = "Alex"


student = Student()

student.age = 25

print(student.age)
```

Output

```
25
```

Python allows adding new attributes.

---

## Using __slots__

```python
class Student:

    __slots__ = [

        "name",

        "age"

    ]

    def __init__(self):

        self.name = "Alex"

        self.age = 22


student = Student()

print(student.name)
```

---

## Invalid Attribute

```python
student.salary = 50000
```

Output

```
AttributeError
```

---

## Why __slots__?

Benefits

- Lower memory usage
- Faster attribute access
- Prevent accidental attributes

---

# 4. Enums

Enums define fixed constants.

---

## Example

```python
from enum import Enum

class Status(Enum):

    ACTIVE = 1

    INACTIVE = 2

    BLOCKED = 3


print(Status.ACTIVE)

print(Status.ACTIVE.name)

print(Status.ACTIVE.value)
```

Output

```
Status.ACTIVE
ACTIVE
1
```

---

## Comparison

```python
status = Status.ACTIVE

if status == Status.ACTIVE:

    print("User Active")
```

---

## Loop Through Enum

```python
from enum import Enum

class Day(Enum):

    MON = 1

    TUE = 2

    WED = 3


for day in Day:

    print(day)
```

---

## Real-World Example

```python
from enum import Enum

class PaymentStatus(Enum):

    PENDING = 1

    SUCCESS = 2

    FAILED = 3


status = PaymentStatus.SUCCESS

print(status.name)
```

---

# 5. NamedTuple

A lightweight immutable object.

---

## Example

```python
from typing import NamedTuple

class Student(NamedTuple):

    id: int

    name: str

    marks: int


student = Student(

    101,

    "Alex",

    95

)

print(student.id)

print(student.name)

print(student.marks)
```

Output

```
101
Alex
95
```

---

## Immutable

```python
student.name = "John"
```

Output

```
AttributeError
```

---

## NamedTuple vs Tuple

```python
from typing import NamedTuple

class Point(NamedTuple):

    x: int

    y: int


point = Point(10,20)

print(point.x)

print(point.y)
```

Instead of

```python
point[0]

point[1]
```

Named fields improve readability.

---

# Mini Project – Student Record

```python
from dataclasses import dataclass
from enum import Enum

class Grade(Enum):

    A = "Excellent"

    B = "Good"

    C = "Average"


@dataclass
class Student:

    id: int

    name: str

    grade: Grade


student = Student(

    101,

    "Alex",

    Grade.A

)

print(student)
```

Output

```
Student(id=101,
        name='Alex',
        grade=<Grade.A: 'Excellent'>)
```

---

# Best Practices

✅ Use Dataclasses for data models.

✅ Use `field(default_factory=...)` for mutable objects.

✅ Use Frozen Dataclasses for immutable data.

✅ Use Enums instead of magic numbers.

✅ Use NamedTuple for lightweight records.

✅ Use `__slots__` only when memory optimization is needed.

---

# Common Mistakes

❌ Using mutable default values without `default_factory`.

❌ Expecting Frozen Dataclasses to allow modification.

❌ Overusing `__slots__`.

❌ Using strings instead of Enums.

❌ Treating NamedTuple as mutable.

---

# Summary Table

| Feature | Purpose |
|----------|---------|
| Dataclass | Automatic class generation |
| field() | Customize fields |
| default_factory | Safe mutable defaults |
| __post_init__ | Post initialization |
| Frozen Dataclass | Immutable objects |
| __slots__ | Memory optimization |
| Enum | Named constants |
| NamedTuple | Lightweight immutable records |

---

# Interview Questions

### Basic

- What is a Dataclass?
- Why use Enums?
- What is NamedTuple?

### Intermediate

- Difference between Dataclass and Normal Class?
- What is `__post_init__()`?
- Why use `default_factory`?

### Advanced

- Explain Frozen Dataclasses.
- When should you use `__slots__`?
- Dataclass vs NamedTuple?
- How does Enum improve software quality?

---

# Next Part

**Module_08_Code_Examples.md (Part 2)**

Topics:

- Class Decorators
- Cached Properties
- Type Annotations
- Forward References
- Class Factories
- Modern Python Design Patterns
```
