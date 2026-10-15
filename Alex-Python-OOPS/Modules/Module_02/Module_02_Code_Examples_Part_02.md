# ==========================================================
# Module 02 – Advanced Class Design & Relationships
# Module_02_Code_Examples.md (Part 2)
# ==========================================================

---

# Topic 7 – Object Collaboration

---

## What is Object Collaboration?

Object Collaboration means **multiple objects working together** to complete a task.

Instead of writing one large class, responsibilities are divided among several classes.

Good software is built using collaborating objects.

---

## Example 1 – Customer Places an Order

```python
class Customer:

    def __init__(self, name):
        self.name = name

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:

    def __init__(self, customer):
        self.customer = customer
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display(self):

        print("Customer :", self.customer.name)

        print("\nProducts")

        total = 0

        for product in self.products:
            print(product.name, product.price)
            total += product.price

        print("\nTotal :", total)

customer = Customer("Alex")

order = Order(customer)

order.add_product(Product("Laptop",50000))
order.add_product(Product("Mouse",800))

order.display()
```

### Output

```text
Customer : Alex

Products

Laptop 50000
Mouse 800

Total : 50800
```

---

## Collaboration Types

### One-to-One

```
Person ---- Passport
```

---

### One-to-Many

```
Department

|

|--- Employee

|--- Employee

|--- Employee
```

---

### Many-to-Many

```
Student ------ Course

Student ------ Course

Student ------ Course
```

---

## Best Practices

- Divide responsibilities.
- Keep classes focused.
- Avoid one giant class.

---

# Topic 8 – Nested Objects

---

## What are Nested Objects?

One object contains another object.

Real-world software uses nested objects extensively.

Example

Employee

↓

Address

↓

City

---

## Example

```python
class Address:

    def __init__(self, city, state):

        self.city = city
        self.state = state

class Employee:

    def __init__(self, name, address):

        self.name = name
        self.address = address

address = Address("Hyderabad","Telangana")

employee = Employee("Alex",address)

print(employee.name)

print(employee.address.city)

print(employee.address.state)
```

### Output

```text
Alex

Hyderabad

Telangana
```

---

## Benefits

- Better organization
- Better encapsulation
- Easy maintenance

---

# Topic 9 – Object Copying

---

## Assignment

```python
class Student:

    def __init__(self,name):
        self.name=name

student1=Student("Alex")

student2=student1

student2.name="John"

print(student1.name)
```

Output

```text
John
```

Both variables point to the same object.

---

## Shallow Copy

```python
import copy

numbers=[1,2,[3,4]]

copy_list=copy.copy(numbers)

copy_list[2][0]=100

print(numbers)

print(copy_list)
```

Output

```text
[1,2,[100,4]]

[1,2,[100,4]]
```

Nested objects remain shared.

---

## Deep Copy

```python
import copy

numbers=[1,2,[3,4]]

copy_list=copy.deepcopy(numbers)

copy_list[2][0]=100

print(numbers)

print(copy_list)
```

Output

```text
[1,2,[3,4]]

[1,2,[100,4]]
```

Everything becomes independent.

---

## Summary

| Copy Type | Shared Objects |
|------------|---------------|
| Assignment | Yes |
| Shallow Copy | Nested Objects Shared |
| Deep Copy | No |

---

# Topic 10 – Object Serialization

---

## What is Serialization?

Serialization converts Python objects into a format that can be stored or transferred.

---

# Pickle

## Save Object

```python
import pickle

student={

"name":"Alex",

"marks":95

}

with open("student.dat","wb") as file:

    pickle.dump(student,file)
```

---

## Load Object

```python
import pickle

with open("student.dat","rb") as file:

    student=pickle.load(file)

print(student)
```

Output

```text
{'name':'Alex','marks':95}
```

---

# JSON Serialization

```python
import json

student={

"name":"Alex",

"marks":95

}

json_data=json.dumps(student)

print(json_data)
```

Output

```text
{"name":"Alex","marks":95}
```

---

## JSON to Dictionary

```python
import json

text='{"name":"Alex","marks":95}'

student=json.loads(text)

print(student["name"])
```

Output

```text
Alex
```

---

## When to Use

Pickle

- Python Applications
- Machine Learning
- Object Storage

JSON

- APIs
- Web Applications
- Data Exchange

---

# Topic 11 – UML Basics

---

## Why UML?

Professional software is designed before coding.

UML provides a visual representation.

---

## Class Diagram

```
+----------------------+

| Student |

+----------------------+

| name |

| marks |

+----------------------+

| display() |

| calculate() |

+----------------------+
```

---

## Object Diagram

```
Student

|

|-- Alex

|-- Marks = 95
```

---

## Relationship Symbols

```
Association

Teacher -------- Student

Aggregation

Department <>----- Employee

Composition

Car ◆------ Engine

Inheritance

Vehicle

↑

Car
```

---

# Topic 12 – Package Organization

---

## Why Packages?

Large applications should never be written inside one file.

Example

```
college/

|

|-- student.py

|-- teacher.py

|-- course.py

|-- department.py

|-- __init__.py

|-- main.py
```

---

## Import Example

student.py

```python
class Student:

    pass
```

main.py

```python
from student import Student

student=Student()
```

---

## Package Import

```
college/

student.py

teacher.py

main.py
```

```python
from college.student import Student
```

---

## __init__.py

Used to

- Create packages
- Initialize packages
- Export classes

---

# Hands-on Exercise 1

Hospital Management

Classes

```
Hospital

Doctor

Patient

Appointment

Medicine
```

Relationships

- Association
- Aggregation
- Composition

---

# Hands-on Exercise 2

Library Management

Classes

```
Library

Book

Student

Librarian
```

---

# Hands-on Exercise 3

School Management

```
School

Teacher

Student

Course

Department
```

---

# Hands-on Exercise 4

Banking System

```
Customer

Account

Transaction

Loan
```

---

# Mini Project

## College Management System

Create

```
College

Department

Teacher

Student

Course

Address

Library
```

Apply

- Instance Methods

- Class Methods

- Static Methods

- Association

- Aggregation

- Composition

- Nested Objects

- Packages

---

# Common Mistakes

❌ Everything inside one class

❌ Using only instance methods

❌ No package structure

❌ Tight coupling

❌ Global variables

❌ No object collaboration

---

# Best Practices

✅ Small focused classes

✅ Single Responsibility Principle

✅ Composition over inheritance where appropriate

✅ Reusable utility methods

✅ Organize code into packages

✅ Separate business logic

---

# Interview Questions

### Basic

- What is Association?

- What is Aggregation?

- What is Composition?

- Difference between Class Method and Static Method?

- Why use Packages?

---

### Intermediate

- Explain Object Collaboration.

- Difference between Shallow Copy and Deep Copy.

- Explain Serialization.

- Explain UML.

- Explain Nested Objects.

---

### Advanced

- Why Composition is preferred over Inheritance?

- When should Factory Methods be used?

- Explain Loose Coupling.

- Explain High Cohesion.

- Design a Library Management System.

- Design a Hospital Management System.

---

# Module Summary

Congratulations!

After completing Module 02, you can now:

✅ Design reusable classes

✅ Create professional object relationships

✅ Use Instance Methods effectively

✅ Use Class Methods

✅ Use Static Methods

✅ Build collaborating objects

✅ Apply Association

✅ Apply Aggregation

✅ Apply Composition

✅ Create Nested Objects

✅ Understand Object Copying

✅ Serialize Objects

✅ Read UML Diagrams

✅ Organize Projects using Packages

You now have the skills needed to design medium-sized Python applications using industry-standard object-oriented principles.

---

# Next Module

**Module 03 – Encapsulation & Data Protection**

Topics include:

- Public Members
- Protected Members
- Private Members
- Name Mangling
- Properties (`@property`)
- Getters and Setters
- Data Validation
- Read-only Objects
- Immutable Objects
- Pythonic Encapsulation
- Secure Class Design
