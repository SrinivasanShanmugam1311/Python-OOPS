# Python Object-Oriented Programming (OOP)

# Module 06 – Python Data Model (Magic Methods)

# Module_06_Code_Examples.md (Part 1)

**Course Level:** Intermediate → Advanced

---

# Object Life Cycle

```
Object Creation

↓

__new__()

↓

__init__()

↓

Object Ready

↓

Object Used

↓

__del__()
```

---

# 1. __new__()

## Purpose

- Creates the object.
- Allocates memory.
- Executes before `__init__()`.
- Must return an object.

---

## Example

```python
class Student:

    def __new__(cls):
        print("__new__ Called")
        obj = super().__new__(cls)
        return obj

    def __init__(self):
        print("__init__ Called")


student = Student()
```

### Output

```
__new__ Called
__init__ Called
```

---

## Returning Another Object

```python
class Demo:

    def __new__(cls):
        print("Creating Integer")
        return 100


obj = Demo()

print(obj)
print(type(obj))
```

Output

```
Creating Integer
100
<class 'int'>
```

---

## When to Override?

- Singleton Pattern
- Object Caching
- Immutable Objects
- Object Pools

Usually **do not override** unless required.

---

# 2. __init__()

## Purpose

Initializes an already created object.

---

## Example

```python
class Student:

    def __init__(self,name,age):

        self.name=name
        self.age=age

student=Student("Alex",25)

print(student.name)
print(student.age)
```

Output

```
Alex
25
```

---

## Default Values

```python
class Employee:

    def __init__(self,name,salary=30000):

        self.name=name
        self.salary=salary

emp=Employee("John")

print(emp.salary)
```

Output

```
30000
```

---

## Validation

```python
class Product:

    def __init__(self,price):

        if price<0:
            raise ValueError("Invalid Price")

        self.price=price

product=Product(500)

print(product.price)
```

---

# Difference

| __new__ | __init__ |
|----------|-----------|
| Creates Object | Initializes Object |
| Called First | Called Second |
| Static Method | Instance Method |
| Returns Object | Returns None |

---

# 3. __del__()

## Purpose

Executed before an object is destroyed.

---

## Example

```python
class Student:

    def __init__(self):

        print("Created")

    def __del__(self):

        print("Destroyed")


student=Student()

del student
```

Output

```
Created
Destroyed
```

---

## Use Cases

- Close Files
- Release Resources
- Logging
- Cleanup

Avoid depending on it for important cleanup.

---

# 4. __str__()

## Purpose

Returns a user-friendly string.

Called by

```python
print(obj)
```

---

## Example

```python
class Student:

    def __init__(self,name):

        self.name=name

    def __str__(self):

        return f"Student : {self.name}"


student=Student("Alex")

print(student)
```

Output

```
Student : Alex
```

---

## Without __str__()

```python
class Student:
    pass

student=Student()

print(student)
```

Output

```
<__main__.Student object at ...>
```

---

# 5. __repr__()

## Purpose

Returns a developer-friendly representation.

Used by

```python
repr(obj)
```

---

## Example

```python
class Student:

    def __init__(self,name):

        self.name=name

    def __repr__(self):

        return f"Student('{self.name}')"


student=Student("Alex")

print(repr(student))
```

Output

```
Student('Alex')
```

---

## __str__ vs __repr__

| __str__ | __repr__ |
|----------|-----------|
| User Friendly | Developer Friendly |
| print() | repr() |
| Readable | Detailed |

---

# 6. __len__()

## Purpose

Supports

```python
len(obj)
```

---

## Example

```python
class Playlist:

    def __init__(self,songs):

        self.songs=songs

    def __len__(self):

        return len(self.songs)


playlist=Playlist(
["Song1","Song2","Song3"]
)

print(len(playlist))
```

Output

```
3
```

---

## Custom Length

```python
class Team:

    def __init__(self):

        self.members=[
            "A",
            "B",
            "C",
            "D"
        ]

    def __len__(self):

        return len(self.members)


team=Team()

print(len(team))
```

---

# 7. __bool__()

## Purpose

Controls object truth value.

Used in

```python
if obj:

while obj:
```

---

## Example

```python
class BankAccount:

    def __init__(self,balance):

        self.balance=balance

    def __bool__(self):

        return self.balance>0


a1=BankAccount(500)

a2=BankAccount(0)

print(bool(a1))

print(bool(a2))
```

Output

```
True

False
```

---

## Shopping Cart Example

```python
class Cart:

    def __init__(self):

        self.items=[]

    def add(self,item):

        self.items.append(item)

    def __bool__(self):

        return len(self.items)>0


cart=Cart()

print(bool(cart))

cart.add("Laptop")

print(bool(cart))
```

Output

```
False

True
```

---

# Summary Table

| Method | Purpose |
|---------|---------|
| __new__ | Create Object |
| __init__ | Initialize Object |
| __del__ | Cleanup |
| __str__ | User-Friendly Display |
| __repr__ | Developer Representation |
| __len__ | Support len() |
| __bool__ | Boolean Evaluation |

---

# Best Practices

✅ Override `__new__()` only for advanced scenarios.

✅ Use `__init__()` for initialization.

✅ Keep `__str__()` readable.

✅ Make `__repr__()` useful for debugging.

✅ Return an integer from `__len__()`.

✅ Return `True` or `False` from `__bool__()`.

✅ Avoid relying on `__del__()` for important resource cleanup.

---

# Common Mistakes

❌ Returning non-objects from `__new__()` unintentionally.

❌ Returning values from `__init__()`.

❌ Forgetting to return a string from `__str__()`.

❌ Returning negative values from `__len__()`.

❌ Returning non-boolean values from `__bool__()`.

---

# Interview Questions

### Basic

- What is a Magic Method?
- Difference between `__new__()` and `__init__()`?
- What is `__str__()`?
- What is `__repr__()`?

### Intermediate

- When should `__new__()` be overridden?
- Why should `__repr__()` be unambiguous?
- How does `__bool__()` affect `if` statements?

### Advanced

- Explain the Python object life cycle.
- Why is `__del__()` not reliable for resource management?
- How do `__new__()` and immutable objects relate?

---

# Next Part

**Module_06_Code_Examples.md (Part 2)**

Topics:

- `__iter__()`
- `__next__()`
- `__getitem__()`
- `__setitem__()`
- `__contains__()`
- `__call__()`
- Custom Iterators
- Custom Containers
