# Python Object-Oriented Programming (OOP)

# Module 05 – Polymorphism & Duck Typing

# Module_05_Code_Examples.md (Part 1A)

Course Level : Intermediate → Advanced

---

# Topic 1 – Runtime Polymorphism

---

## What is Runtime Polymorphism?

Runtime Polymorphism means the method that executes depends on the actual object created during program execution.

Same method.

Different implementations.

---

## Example 1 – Animal Sounds

```python
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


class Cat(Animal):

    def sound(self):
        print("Cat Meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

### Output

```
Dog Barks
Cat Meows
```

---

## Example 2 – Shape Area

```python
class Shape:

    def area(self):
        print("Generic Area")


class Rectangle(Shape):

    def area(self):
        print("Rectangle Area")


class Circle(Shape):

    def area(self):
        print("Circle Area")


shapes = [Rectangle(), Circle()]

for shape in shapes:
    shape.area()
```

### Output

```
Rectangle Area
Circle Area
```

---

## Example 3 – Employee Salary

```python
class Employee:

    def salary(self):
        print("Employee Salary")


class Manager(Employee):

    def salary(self):
        print("Manager Salary")


class Developer(Employee):

    def salary(self):
        print("Developer Salary")


employees = [Manager(), Developer()]

for emp in employees:
    emp.salary()
```

### Output

```
Manager Salary
Developer Salary
```

---

# Why Runtime Polymorphism?

Without Polymorphism

```
if employee=="Manager"

elif employee=="Developer"

elif employee=="Tester"
```

With Polymorphism

```
employee.salary()
```

Cleaner.

Flexible.

Extensible.

---

# Topic 2 – Method Overriding

---

## What is Method Overriding?

The child class replaces the parent's implementation.

Rules

- Same method name
- Same purpose
- Different implementation

---

## Example 1

```python
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def start(self):
        print("Car Started")


car = Car()

car.start()
```

Output

```
Car Started
```

---

## Example 2 – Using Parent Method

```python
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def start(self):

        super().start()

        print("Car Started")


car = Car()

car.start()
```

Output

```
Vehicle Started
Car Started
```

---

## Example 3 – Banking

```python
class Account:

    def interest(self):
        print("General Interest")


class SavingsAccount(Account):

    def interest(self):
        print("Savings Interest")


class CurrentAccount(Account):

    def interest(self):
        print("Current Interest")


accounts = [
    SavingsAccount(),
    CurrentAccount()
]

for account in accounts:
    account.interest()
```

Output

```
Savings Interest
Current Interest
```

---

# Topic 3 – Built-in Polymorphism

---

Python's built-in functions work with many object types.

---

## Example 1 – len()

```python
print(len("Python"))

print(len([10,20,30]))

print(len((1,2,3)))

print(len({1,2,3}))
```

Output

```
6
3
3
3
```

---

## Example 2 – max()

```python
print(max(10,20))

print(max([5,8,3]))

print(max("PYTHON"))
```

Output

```
20
8
Y
```

---

## Example 3 – sum()

```python
print(sum([10,20,30]))

print(sum((5,5,5)))
```

Output

```
60
15
```

---

## Example 4 – print()

```python
print(100)

print("Python")

print([1,2,3])

print({"Name":"Alex"})
```

Python prints every object correctly.

This is also polymorphism.

---

# Topic 4 – Operator Polymorphism

---

Same operator.

Different behavior.

---

## Example 1

```python
print(10+20)

print("Hello "+"Python")

print([1,2]+[3,4])
```

Output

```
30

Hello Python

[1, 2, 3, 4]
```

---

## Example 2

```python
print(5*4)

print("Hi "*3)

print([1]*4)
```

Output

```
20

Hi Hi Hi

[1, 1, 1, 1]
```

---

## Why?

Internally Python calls Magic Methods.

```
+

↓

__add__()
```

```
*

↓

__mul__()
```

---

# Topic 5 – Magic Methods

---

Magic Methods are also called

Special Methods

or

Dunder Methods.

Examples

```
__init__

__str__

__repr__

__len__

__add__
```

---

## Example 1 – __str__()

```python
class Student:

    def __init__(self,name):

        self.name=name

    def __str__(self):

        return self.name


student=Student("Alex")

print(student)
```

Output

```
Alex
```

---

## Example 2 – __len__()

```python
class Playlist:

    def __init__(self,songs):

        self.songs=songs

    def __len__(self):

        return len(self.songs)


playlist=Playlist(
["A","B","C","D"]
)

print(len(playlist))
```

Output

```
4
```

---

## Example 3 – __add__()

```python
class Number:

    def __init__(self,value):

        self.value=value

    def __add__(self,other):

        return Number(
            self.value+other.value
        )

    def __str__(self):

        return str(self.value)


n1=Number(100)

n2=Number(200)

print(n1+n2)
```

Output

```
300
```

---

# Summary

You have learned

✅ Runtime Polymorphism

✅ Method Overriding

✅ Built-in Polymorphism

✅ Operator Polymorphism

✅ Magic Methods

These concepts form the foundation for Python's dynamic behavior.

---

# Best Practices

- Override only when behavior changes.
- Use `super()` where appropriate.
- Prefer polymorphism over long `if-elif` chains.
- Implement magic methods only when they make sense.
- Keep overridden methods consistent with the parent class contract.

---

# Common Mistakes

❌ Confusing overriding with overloading.

❌ Forgetting to call `super()` when parent initialization is required.

❌ Overloading classes with unnecessary magic methods.

❌ Breaking expected behavior of operators.

---

# Next Part

Module_05_Code_Examples.md (Part 1B)

Topics

- Duck Typing

- EAFP

- LBYL

- Interface Concept

- Practical Examples

- Interview Questions
