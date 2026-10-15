# Python Object-Oriented Programming (OOP)

# Module 04 – Inheritance & Method Resolution Order (MRO)

## Module_04_Code_Examples.md (Part 1)

**Course Level:** Intermediate → Advanced

---

# Topic 1 – Single Inheritance

---

## What is Single Inheritance?

Single inheritance means **one child class inherits from one parent class**.

```
Animal
   │
   ▼
 Dog
```

The child class automatically inherits all accessible members from the parent.

---

## Syntax

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

## Example 1 – Basic Inheritance

```python
class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

dog = Dog()

dog.eat()
```

### Output

```text
Animal is eating
```

---

## Example 2 – Parent + Child Methods

```python
class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):

    def drive(self):
        print("Car is Moving")

car = Car()

car.start()

car.drive()
```

### Output

```text
Vehicle Started
Car is Moving
```

---

## Advantages

- Code Reuse
- Easy Maintenance
- Simple Design

---

# Topic 2 – Multilevel Inheritance

---

## What is Multilevel Inheritance?

A child class becomes the parent of another class.

```
Person

   │

Employee

   │

Manager
```

---

## Example

```python
class Person:

    def display_name(self):
        print("Person")

class Employee(Person):

    def display_employee(self):
        print("Employee")

class Manager(Employee):

    def display_manager(self):
        print("Manager")

manager = Manager()

manager.display_name()

manager.display_employee()

manager.display_manager()
```

### Output

```text
Person
Employee
Manager
```

---

## Advantages

- Gradual Extension
- Better Organization
- High Code Reuse

---

# Topic 3 – Hierarchical Inheritance

---

## What is Hierarchical Inheritance?

Multiple child classes inherit from one parent.

```
Vehicle

├── Car

├── Bike

└── Bus
```

---

## Example

```python
class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):

    def drive(self):
        print("Driving Car")

class Bike(Vehicle):

    def ride(self):
        print("Riding Bike")

class Bus(Vehicle):

    def transport(self):
        print("Transporting Passengers")

car = Car()

bike = Bike()

bus = Bus()

car.start()

bike.start()

bus.start()
```

### Output

```text
Vehicle Started
Vehicle Started
Vehicle Started
```

---

# Topic 4 – Method Overriding

---

## What is Method Overriding?

A child class provides its own implementation of a parent method.

The method name remains the same.

---

## Example 1

```python
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()

dog.sound()
```

### Output

```text
Bark
```

---

## Example 2

```python
class Shape:

    def area(self):
        print("Area")

class Rectangle(Shape):

    def area(self):
        print("Length × Width")

rectangle = Rectangle()

rectangle.area()
```

### Output

```text
Length × Width
```

---

## Why Override?

- Customize behavior
- Extend parent functionality
- Implement polymorphism

---

# Topic 5 – super()

---

## What is super()?

`super()` refers to the immediate parent class.

It allows the child class to reuse parent methods instead of rewriting them.

---

## Example 1

```python
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):

        super().sound()

        print("Dog Bark")

dog = Dog()

dog.sound()
```

### Output

```text
Animal Sound
Dog Bark
```

---

## Example 2 – Constructor

```python
class Person:

    def __init__(self, name):

        self.name = name

class Student(Person):

    def __init__(self, name, roll):

        super().__init__(name)

        self.roll = roll

student = Student("Alex",101)

print(student.name)

print(student.roll)
```

### Output

```text
Alex
101
```

---

# Topic 6 – Constructor Chaining

---

## What is Constructor Chaining?

When a child object is created, both parent and child constructors execute.

This is achieved using `super().__init__()`.

---

## Example

```python
class Person:

    def __init__(self):

        print("Person Constructor")

class Employee(Person):

    def __init__(self):

        super().__init__()

        print("Employee Constructor")

employee = Employee()
```

### Output

```text
Person Constructor
Employee Constructor
```

---

## Multi-Level Constructor Chaining

```python
class A:

    def __init__(self):

        print("A")

class B(A):

    def __init__(self):

        super().__init__()

        print("B")

class C(B):

    def __init__(self):

        super().__init__()

        print("C")

obj = C()
```

### Output

```text
A
B
C
```

---

# Real-World Example – Employee Hierarchy

```python
class Person:

    def __init__(self, name):

        self.name = name

    def display(self):

        print("Name :", self.name)

class Employee(Person):

    def __init__(self, name, salary):

        super().__init__(name)

        self.salary = salary

    def display_salary(self):

        print("Salary :", self.salary)

employee = Employee("Alex",60000)

employee.display()

employee.display_salary()
```

### Output

```text
Name : Alex
Salary : 60000
```

---

# Real-World Example – Vehicle Hierarchy

```python
class Vehicle:

    def start(self):

        print("Vehicle Started")

class Car(Vehicle):

    def drive(self):

        print("Driving Car")

class ElectricCar(Car):

    def charge(self):

        print("Charging Battery")

car = ElectricCar()

car.start()

car.drive()

car.charge()
```

### Output

```text
Vehicle Started
Driving Car
Charging Battery
```

---

# Comparison

| Feature | Single | Multilevel | Hierarchical |
|----------|---------|------------|--------------|
| Parent Classes | 1 | Chain | 1 |
| Child Classes | 1 | Multiple Levels | Many |
| Code Reuse | High | High | High |
| Complexity | Low | Medium | Medium |

---

# Best Practices

✅ Model only true **IS-A** relationships.

✅ Keep inheritance trees shallow.

✅ Use `super()` instead of directly calling parent methods.

✅ Override methods only when behavior changes.

✅ Reuse constructors with `super().__init__()`.

---

# Common Mistakes

❌ Forgetting `super().__init__()`.

❌ Overriding methods without understanding parent behavior.

❌ Creating deep inheritance hierarchies.

❌ Using inheritance only to reuse code when composition is more appropriate.

---

# Interview Questions

### Basic

- What is inheritance?
- What is single inheritance?
- What is multilevel inheritance?
- What is hierarchical inheritance?

---

### Intermediate

- What is method overriding?
- Why do we use `super()`?
- Explain constructor chaining.

---

### Advanced

- When should inheritance be avoided?
- Explain the IS-A relationship.
- What are the advantages and disadvantages of inheritance?

---

# Summary

After completing Part 1, you can:

✅ Implement Single Inheritance

✅ Build Multilevel Inheritance

✅ Design Hierarchical Inheritance

✅ Override Parent Methods

✅ Use `super()` Correctly

✅ Understand Constructor Chaining

---

# Next Part

**Module_04_Code_Examples.md (Part 2)**

Topics Covered:

- Multiple Inheritance
- Hybrid Inheritance
- Method Resolution Order (MRO)
- Diamond Problem
- `mro()`
- Cooperative Inheritance
- Composition vs Inheritance
- Animal Hierarchy
- Employee Hierarchy
- Vehicle System
- Shape Calculator
- University Staff Hierarchy Mini Project
- Best Practices
- Common Mistakes
- Interview Questions
