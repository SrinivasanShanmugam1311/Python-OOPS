# Python Object-Oriented Programming (OOP) Using Python

# Module 03 – Encapsulation & Data Protection

## Module_03_Code_Examples.md (Part 1)

**Course Level:** Intermediate → Advanced

---

# Topic 1 – Public Members

## What are Public Members?

Public members are accessible from anywhere.

Python variables are **public by default**.

---

## Syntax

```python
class Student:

    def __init__(self):

        self.name = "Alex"
```

---

## Example 1

```python
class Student:

    def __init__(self):

        self.name="Alex"
        self.marks=95

student=Student()

print(student.name)

print(student.marks)
```

### Output

```text
Alex
95
```

---

## Example 2

```python
class Employee:

    def __init__(self):

        self.salary=50000

employee=Employee()

employee.salary=65000

print(employee.salary)
```

Output

```text
65000
```

---

## Advantages

- Easy to access

- Easy to understand

- Good for non-sensitive data

---

## Disadvantages

- Anyone can modify data

- No validation

- Poor security

---

# Topic 2 – Protected Members

---

## What are Protected Members?

Protected members use

```
_single_underscore
```

Example

```python
_balance
```

Python does not enforce protection.

It is a developer convention.

---

## Example 1

```python
class Employee:

    def __init__(self):

        self._salary=50000

employee=Employee()

print(employee._salary)
```

Output

```text
50000
```

---

## Example 2

```python
class Employee:

    def __init__(self):

        self._salary=50000

class Manager(Employee):

    def display(self):

        print(self._salary)

manager=Manager()

manager.display()
```

Output

```text
50000
```

---

## Best Practice

Protected members are mainly used inside child classes.

---

# Topic 3 – Private Members

---

## What are Private Members?

Private members begin with

```
__
```

Python performs **Name Mangling**.

---

## Example 1

```python
class BankAccount:

    def __init__(self):

        self.__balance=10000

account=BankAccount()

print(account.__balance)
```

Output

```text
AttributeError
```

---

## Why?

Python changes

```
__balance
```

to

```
_BankAccount__balance
```

---

## Example 2

```python
class BankAccount:

    def __init__(self):

        self.__balance=10000

account=BankAccount()

print(account._BankAccount__balance)
```

Output

```text
10000
```

---

## Example 3

```python
class Employee:

    def __init__(self):

        self.__salary=60000

    def display(self):

        print(self.__salary)

employee=Employee()

employee.display()
```

Output

```text
60000
```

---

# Topic 4 – Name Mangling

---

## What is Name Mangling?

Python changes

```
__variable
```

into

```
_ClassName__variable
```

internally.

---

## Example

```python
class Student:

    def __init__(self):

        self.__marks=95

student=Student()

print(dir(student))
```

Output

```
_Student__marks
```

---

## Purpose

- Avoid accidental access

- Prevent naming conflicts

---

# Topic 5 – Getter Methods

---

## Why Getter?

Instead of

```
student.__marks
```

Use

```
student.get_marks()
```

---

## Example

```python
class Student:

    def __init__(self):

        self.__marks=95

    def get_marks(self):

        return self.__marks

student=Student()

print(student.get_marks())
```

Output

```text
95
```

---

# Topic 6 – Setter Methods

---

Setter updates values after validation.

---

## Example

```python
class Student:

    def __init__(self):

        self.__marks=0

    def set_marks(self,marks):

        if 0<=marks<=100:

            self.__marks=marks

student=Student()

student.set_marks(90)

print(student.get_marks())
```

Output

```text
90
```

---

## Example with Validation

```python
class Employee:

    def __init__(self):

        self.__salary=0

    def set_salary(self,salary):

        if salary>0:

            self.__salary=salary

        else:

            print("Invalid Salary")

    def get_salary(self):

        return self.__salary

employee=Employee()

employee.set_salary(-100)

employee.set_salary(60000)

print(employee.get_salary())
```

Output

```text
Invalid Salary

60000
```

---

# Topic 7 – @property

---

Python provides a cleaner solution.

Instead of

```
get_salary()

set_salary()
```

Python uses

```
employee.salary
```

internally.

---

## Example

```python
class Employee:

    def __init__(self):

        self.__salary=50000

    @property

    def salary(self):

        return self.__salary

employee=Employee()

print(employee.salary)
```

Output

```text
50000
```

---

# Topic 8 – Setter Property

---

## Example

```python
class Employee:

    def __init__(self):

        self.__salary=0

    @property

    def salary(self):

        return self.__salary

    @salary.setter

    def salary(self,value):

        if value>0:

            self.__salary=value

employee=Employee()

employee.salary=70000

print(employee.salary)
```

Output

```text
70000
```

---

# Topic 9 – Deleter Property

---

## Example

```python
class Employee:

    def __init__(self):

        self.__salary=60000

    @property

    def salary(self):

        return self.__salary

    @salary.deleter

    def salary(self):

        print("Salary Deleted")

        del self.__salary

employee=Employee()

del employee.salary
```

Output

```text
Salary Deleted
```

---

# Topic 10 – Read-only Property

---

Only Getter.

No Setter.

---

## Example

```python
class Student:

    def __init__(self):

        self.__roll=101

    @property

    def roll(self):

        return self.__roll

student=Student()

print(student.roll)
```

Output

```text
101
```

---

Trying

```python
student.roll=200
```

Produces

```
AttributeError
```

---

# Topic 11 – Computed Property

---

Properties need not store data.

They can compute values.

---

## Example

```python
class Rectangle:

    def __init__(self,length,width):

        self.length=length

        self.width=width

    @property

    def area(self):

        return self.length*self.width

rectangle=Rectangle(10,5)

print(rectangle.area)
```

Output

```text
50
```

---

## Example 2

```python
class Student:

    def __init__(self,m1,m2,m3):

        self.m1=m1

        self.m2=m2

        self.m3=m3

    @property

    def percentage(self):

        return (self.m1+self.m2+self.m3)/3

student=Student(90,95,80)

print(student.percentage)
```

Output

```text
88.33333333333333
```

---

# Summary Table

| Feature | Public | Protected | Private |
|----------|--------|-----------|----------|
| Access Everywhere | ✅ | ⚠ Convention | ❌ |
| Security | Low | Medium | High |
| Validation | No | No | Yes |
| Recommended for Sensitive Data | No | Sometimes | Yes |

---

# Best Practices

✅ Keep sensitive data private.

✅ Use properties instead of Java-style getters.

✅ Validate data before updating.

✅ Expose only necessary information.

✅ Use read-only properties whenever possible.

---

# Common Mistakes

❌ Accessing private members directly.

❌ Making every variable public.

❌ Forgetting validation.

❌ Misusing protected variables.

❌ Using getter/setter everywhere instead of `@property`.

---

# Interview Questions

### Basic

- What is Encapsulation?

- Difference between Public and Private Members?

- What is Name Mangling?

---

### Intermediate

- Why use @property?

- Difference between Getter and Property?

- What is Read-only Property?

---

### Advanced

- Explain Computed Properties.

- Explain Name Mangling Internals.

- Why does Python discourage Java-style getters and setters?

---

# Next Part

Module_03_Code_Examples.md (Part 2)

Topics Covered

- Validation
- Business Rules
- Exception Handling
- Data Integrity
- Immutable Objects
- Controlled Updates
- Secure Bank Account
- ATM System
- Wallet
- Employee Salary Project
- Student Marks Project
- Mini Project
