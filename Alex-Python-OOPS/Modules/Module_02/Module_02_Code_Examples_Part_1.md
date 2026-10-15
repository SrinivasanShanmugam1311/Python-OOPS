# Python Object-Oriented Programming (OOP) Using Python

# Module 02 – Advanced Class Design & Relationships

## Module_02_Code_Examples.md (Part 1)

**Course Level:** Intermediate → Advanced

---

# Topic 1 – Instance Methods

---

## What is an Instance Method?

An **Instance Method** is a method that belongs to an object (instance) of a class.

It always receives the current object as the first parameter, traditionally named `self`.

Instance methods operate on **instance variables**.

---

## Syntax

```python
class ClassName:

    def method_name(self):
        pass
```

---

## Example 1 – Simple Instance Method

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name :", self.name)
        print("Marks:", self.marks)

student = Student("Alex", 95)

student.display()
```

### Output

```text
Name : Alex
Marks: 95
```

---

## Example 2 – Updating Object Data

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        print("Balance :", self.balance)

account = BankAccount(10000)

account.deposit(500)

account.withdraw(1200)

account.display()
```

### Output

```text
Balance : 9300
```

---

## Passing Objects

```python
class Employee:

    def __init__(self, name):
        self.name = name

class Department:

    def show(self, employee):
        print(employee.name)

emp = Employee("John")

dept = Department()

dept.show(emp)
```

Output

```text
John
```

---

## Returning Objects

```python
class Student:

    def __init__(self, name):
        self.name = name

    def duplicate(self):
        return Student(self.name)

student1 = Student("Alex")

student2 = student1.duplicate()

print(student2.name)
```

Output

```text
Alex
```

---

## Best Practices

- Keep methods focused on one responsibility.
- Modify only the object's own state.
- Avoid unnecessary global variables.

---

## Common Mistakes

❌ Forgetting `self`

```python
def display():
```

✔ Correct

```python
def display(self):
```

---

# Topic 2 – Class Methods

---

## What is a Class Method?

A class method belongs to the **class**, not to an individual object.

It receives `cls` instead of `self`.

---

## Syntax

```python
class Sample:

    @classmethod
    def method(cls):
        pass
```

---

## Example 1 – Counting Objects

```python
class Student:

    total_students = 0

    def __init__(self):
        Student.total_students += 1

    @classmethod
    def total(cls):
        print(cls.total_students)

Student()

Student()

Student.total()
```

Output

```text
2
```

---

## Example 2 – Alternative Constructor

```python
class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, text):

        name, salary = text.split(",")

        return cls(name, int(salary))

employee = Employee.from_string("Alex,60000")

print(employee.name)

print(employee.salary)
```

Output

```text
Alex
60000
```

---

## Factory Method Example

```python
class Shape:

    @classmethod
    def create_circle(cls):
        return "Circle Created"

print(Shape.create_circle())
```

Output

```text
Circle Created
```

---

## Best Practices

- Use class methods for creating objects.
- Access class variables using `cls`.
- Prefer class methods over hardcoded constructors when multiple creation paths exist.

---

# Topic 3 – Static Methods

---

## What is a Static Method?

A static method belongs to a class but does not use `self` or `cls`.

It behaves like a normal function placed inside the class.

---

## Syntax

```python
class Utility:

    @staticmethod
    def calculate():
        pass
```

---

## Example 1 – Tax Calculator

```python
class Tax:

    @staticmethod
    def calculate(amount):

        return amount * 0.18

print(Tax.calculate(1000))
```

Output

```text
180.0
```

---

## Example 2 – Email Validation

```python
class Validator:

    @staticmethod
    def is_valid(email):

        return "@" in email

print(Validator.is_valid("abc@gmail.com"))

print(Validator.is_valid("abcgmail.com"))
```

Output

```text
True

False
```

---

## When Should You Use Static Methods?

- Validation
- Utility Functions
- Mathematical Calculations
- Formatting

---

## Best Practices

- Do not access instance variables.
- Do not modify class variables.
- Keep static methods stateless.

---

# Topic 4 – Association

---

## What is Association?

Association means **two independent objects communicate with each other**.

Neither object owns the other.

Both can exist independently.

---

## Example

Teacher teaches Student.

Both can exist without each other.

---

### Code Example

```python
class Teacher:

    def __init__(self, name):
        self.name = name

class Student:

    def __init__(self, name):
        self.name = name

    def learn(self, teacher):

        print(self.name, "learns from", teacher.name)

teacher = Teacher("Dr. Rao")

student = Student("Alex")

student.learn(teacher)
```

Output

```text
Alex learns from Dr. Rao
```

---

## Characteristics

- Loose coupling
- Independent lifecycle
- Flexible relationship

---

# Topic 5 – Aggregation

---

## What is Aggregation?

Aggregation represents a **Has-A** relationship.

The child object can exist independently.

---

## Example

Department has Employees.

Employees can exist even if the department is removed.

---

### Code Example

```python
class Employee:

    def __init__(self, name):
        self.name = name

class Department:

    def __init__(self, employees):

        self.employees = employees

    def display(self):

        for employee in self.employees:

            print(employee.name)

emp1 = Employee("Alex")

emp2 = Employee("John")

department = Department([emp1, emp2])

department.display()
```

Output

```text
Alex

John
```

---

## Characteristics

- Weak ownership
- Child objects survive independently
- Reusable objects

---

# Topic 6 – Composition

---

## What is Composition?

Composition is a strong **Has-A** relationship.

The child object belongs completely to the parent.

If the parent is destroyed, the child is also destroyed conceptually.

---

## Example

A House contains Rooms.

A Room cannot logically exist without the House in this model.

---

### Code Example

```python
class Engine:

    def start(self):
        print("Engine Started")

class Car:

    def __init__(self):

        self.engine = Engine()

    def drive(self):

        self.engine.start()

        print("Car Moving")

car = Car()

car.drive()
```

Output

```text
Engine Started

Car Moving
```

---

## Aggregation vs Composition

| Feature | Aggregation | Composition |
|----------|-------------|-------------|
| Ownership | Weak | Strong |
| Lifecycle | Independent | Dependent |
| Relationship | Has-A | Owns-A |
| Reusability | High | Lower |

---

# Summary

After completing Part 1, you can:

- Write professional instance methods.
- Create reusable class methods.
- Use static methods correctly.
- Design classes using Association.
- Apply Aggregation for reusable object relationships.
- Apply Composition for strong ownership relationships.

---

# Next Part

Module_02_Code_Examples.md (Part 2)

Topics Covered:

- Object Collaboration
- Nested Objects
- Assignment vs Shallow Copy vs Deep Copy
- Object Serialization
- UML Basics
- Package Organization
- Practice Programs
- Mini Project
- Interview Questions
- Best Practices
