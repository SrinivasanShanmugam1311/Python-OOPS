# Python Object-Oriented Programming (OOP)

# Module 06 – Python Data Model (Magic Methods)

# Module_06_Code_Examples.md (Part 2)

**Course Level:** Intermediate → Advanced

---

# Iterator Protocol

```
Object

↓

__iter__()

↓

Iterator

↓

__next__()

↓

StopIteration
```

Python automatically uses this protocol in:

- for loops
- list()
- tuple()
- set()
- dict()
- comprehensions

---

# 1. __iter__()

## Purpose

Returns an iterator object.

Usually returns `self`.

---

## Example

```python
class Numbers:

    def __init__(self):
        self.data = [10, 20, 30]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.data):
            raise StopIteration

        value = self.data[self.index]
        self.index += 1
        return value


numbers = Numbers()

for number in numbers:
    print(number)
```

### Output

```
10
20
30
```

---

# 2. __next__()

## Purpose

Returns one item at a time.

Raises

```
StopIteration
```

when iteration finishes.

---

## Example

```python
class Counter:

    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


for value in Counter(5):
    print(value)
```

### Output

```
1
2
3
4
5
```

---

# 3. __getitem__()

## Purpose

Supports indexing.

```
obj[index]
```

---

## Example

```python
class StudentList:

    def __init__(self):
        self.students = [
            "Alex",
            "John",
            "Sara"
        ]

    def __getitem__(self, index):
        return self.students[index]


students = StudentList()

print(students[0])
print(students[2])
```

### Output

```
Alex
Sara
```

---

# Slicing Support

```python
print(students[0:2])
```

Output

```
['Alex', 'John']
```

---

# 4. __setitem__()

## Purpose

Supports assignment.

```
obj[index] = value
```

---

## Example

```python
class Marks:

    def __init__(self):
        self.data = [80, 85, 90]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __getitem__(self, index):
        return self.data[index]


marks = Marks()

marks[1] = 95

print(marks[1])
```

### Output

```
95
```

---

# 5. __contains__()

## Purpose

Supports

```
in
```

operator.

---

## Example

```python
class Team:

    def __init__(self):
        self.members = [
            "Alex",
            "John",
            "Sara"
        ]

    def __contains__(self, name):
        return name in self.members


team = Team()

print("Alex" in team)

print("David" in team)
```

### Output

```
True
False
```

---

# 6. __call__()

## Purpose

Makes an object behave like a function.

```
obj()
```

---

## Example

```python
class Calculator:

    def __call__(self, a, b):
        return a + b


calc = Calculator()

print(calc(10, 20))
```

### Output

```
30
```

---

## Logger Example

```python
class Logger:

    def __call__(self, message):
        print(f"LOG : {message}")


logger = Logger()

logger("Application Started")
logger("Database Connected")
```

### Output

```
LOG : Application Started
LOG : Database Connected
```

---

# Project 1 – Custom List

```python
class MyList:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items


my_list = MyList()

my_list.add("Python")
my_list.add("Java")

print(len(my_list))
print(my_list[0])
print("Python" in my_list)
```

### Output

```
2
Python
True
```

---

# Project 2 – Student Collection

```python
class StudentCollection:

    def __init__(self):
        self.students = []

    def add(self, name):
        self.students.append(name)

    def __iter__(self):
        return iter(self.students)

    def __len__(self):
        return len(self.students)


students = StudentCollection()

students.add("Alex")
students.add("John")
students.add("Sara")

for student in students:
    print(student)

print(len(students))
```

---

# Best Practices

✅ Raise `StopIteration` correctly.

✅ Return iterators from `__iter__()`.

✅ Support slicing in `__getitem__()` when possible.

✅ Keep `__call__()` focused on a single responsibility.

✅ Make container behavior intuitive.

---

# Common Mistakes

❌ Forgetting to raise `StopIteration`.

❌ Returning incorrect types from `__iter__()`.

❌ Breaking indexing rules.

❌ Misusing `__call__()` for unrelated logic.

❌ Returning mutable internal state without care.

---

# Summary Table

| Method | Purpose |
|---------|---------|
| `__iter__()` | Return Iterator |
| `__next__()` | Next Element |
| `__getitem__()` | Index Access |
| `__setitem__()` | Item Assignment |
| `__contains__()` | Membership Test |
| `__call__()` | Callable Object |

---

# Interview Questions

### Basic

- What is the Iterator Protocol?
- Difference between `__iter__()` and `__next__()`?
- What does `__getitem__()` do?

### Intermediate

- Why is `StopIteration` required?
- How does Python implement `for` loops?
- Difference between `__contains__()` and `__getitem__()`?

### Advanced

- How would you design a custom container?
- Why should `__iter__()` usually return an iterator?
- When is a callable object better than a function?

---

# Next Part

**Module_06_Code_Examples.md (Part 3)**

Topics:

- `__eq__()`
- `__lt__()`
- `__gt__()`
- `__le__()`
- `__ge__()`
- Operator Overloading (`__add__`, `__sub__`, `__mul__`)
- Context Managers (`__enter__`, `__exit__`)
- Vector Class
- Shopping Cart
- Matrix Operations
- Python Collection Class (Mini Project)
- Module Summary
