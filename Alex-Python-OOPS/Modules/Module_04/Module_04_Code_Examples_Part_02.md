# Python Object-Oriented Programming (OOP)

# Module 04 – Inheritance & Method Resolution Order (MRO)

## Module_04_Code_Examples.md (Part 2)

**Course Level:** Intermediate → Advanced

---

# Topic 7 – Multiple Inheritance

---

## What is Multiple Inheritance?

A child class inherits from **two or more parent classes**.

```
      Father
         │
         │
      Mother
         │
         ▼
        Child
```

The child receives members from both parent classes.

---

## Syntax

```python
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
```

---

## Example 1

```python
class Father:

    def skills(self):
        print("Programming")

class Mother:

    def hobbies(self):
        print("Painting")

class Child(Father, Mother):
    pass

child = Child()

child.skills()

child.hobbies()
```

### Output

```text
Programming
Painting
```

---

## Example 2 – Employee Skills

```python
class Technical:

    def coding(self):
        print("Coding")

class Management:

    def planning(self):
        print("Planning")

class TeamLead(Technical, Management):

    def manage_team(self):
        print("Managing Team")

lead = TeamLead()

lead.coding()

lead.planning()

lead.manage_team()
```

### Output

```text
Coding
Planning
Managing Team
```

---

# Topic 8 – Hybrid Inheritance

---

Hybrid inheritance combines two or more inheritance types.

```
          Person
         /      \
    Student   Employee
         \      /
          TeachingAssistant
```

---

## Example

```python
class Person:

    def display(self):
        print("Person")

class Student(Person):

    def study(self):
        print("Studying")

class Employee(Person):

    def work(self):
        print("Working")

class TeachingAssistant(Student, Employee):

    def assist(self):
        print("Teaching Assistant")

ta = TeachingAssistant()

ta.display()

ta.study()

ta.work()

ta.assist()
```

### Output

```text
Person
Studying
Working
Teaching Assistant
```

---

# Topic 9 – Method Resolution Order (MRO)

---

## Why MRO?

When multiple parent classes contain methods with the same name, Python needs a rule to decide which one to execute.

This rule is called **Method Resolution Order (MRO)**.

Python follows the **C3 Linearization Algorithm**.

---

## Example

```python
class A:

    def show(self):
        print("A")

class B(A):

    def show(self):
        print("B")

class C(A):

    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()

obj.show()
```

### Output

```text
B
```

Python searches according to the MRO.

---

## Viewing the MRO

```python
print(D.mro())
```

Output

```text
[
D,
B,
C,
A,
object
]
```

---

# Topic 10 – Diamond Problem

---

The Diamond Problem occurs when the same base class is inherited through multiple paths.

```
          A
        /   \
       B     C
        \   /
          D
```

---

## Example

```python
class A:

    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

obj = D()

obj.show()
```

### Output

```text
A
```

Python avoids ambiguity using the MRO.

---

# Topic 11 – mro()

---

Every Python class provides an `mro()` method.

It returns the complete lookup order.

---

## Example

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro())
```

### Output

```text
[
C,
B,
A,
object
]
```

---

# Topic 12 – Cooperative Inheritance

---

Cooperative inheritance allows every class in the inheritance chain to execute its implementation by using `super()`.

---

## Example

```python
class A:

    def display(self):

        print("A")

class B(A):

    def display(self):

        super().display()

        print("B")

class C(B):

    def display(self):

        super().display()

        print("C")

obj = C()

obj.display()
```

### Output

```text
A
B
C
```

---

## Multiple Inheritance with super()

```python
class A:

    def show(self):

        print("A")

class B(A):

    def show(self):

        super().show()

        print("B")

class C(A):

    def show(self):

        super().show()

        print("C")

class D(B, C):

    def show(self):

        super().show()

        print("D")

obj = D()

obj.show()
```

### Output

```text
A
C
B
D
```

Notice that `super()` follows the **MRO**, not simply the immediate parent.

---

# Topic 13 – Composition vs Inheritance

---

## Inheritance (IS-A)

```
Car

↓

Vehicle
```

A **Car is a Vehicle**.

---

## Composition (HAS-A)

```
Car

↓

Engine
```

A **Car has an Engine**.

---

## Composition Example

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

### Output

```text
Engine Started
Car Moving
```

---

## Comparison

| Feature | Inheritance | Composition |
|----------|-------------|-------------|
| Relationship | IS-A | HAS-A |
| Coupling | Tighter | Looser |
| Reuse | Through inheritance | Through objects |
| Flexibility | Lower | Higher |
| Recommended | True hierarchies | Object collaboration |

---

# Hands-on Project 1 – Animal Hierarchy

```python
class Animal:

    def eat(self):
        print("Eating")

class Mammal(Animal):

    def walk(self):
        print("Walking")

class Dog(Mammal):

    def bark(self):
        print("Barking")

dog = Dog()

dog.eat()

dog.walk()

dog.bark()
```

---

# Hands-on Project 2 – Employee Hierarchy

```python
class Person:

    def details(self):
        print("Person Details")

class Employee(Person):

    def salary(self):
        print("Salary Processing")

class Manager(Employee):

    def approve_leave(self):
        print("Leave Approved")

manager = Manager()

manager.details()

manager.salary()

manager.approve_leave()
```

---

# Hands-on Project 3 – Vehicle System

```python
class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):

    def drive(self):
        print("Driving")

class ElectricCar(Car):

    def charge(self):
        print("Charging")

car = ElectricCar()

car.start()

car.drive()

car.charge()
```

---

# Hands-on Project 4 – Shape Calculator

```python
class Shape:

    def area(self):
        print("Generic Area")

class Rectangle(Shape):

    def area(self):
        print("Length × Width")

class Circle(Shape):

    def area(self):
        print("π × r²")

rectangle = Rectangle()
circle = Circle()

rectangle.area()
circle.area()
```

---

# Mini Assignment – University Staff Hierarchy

Create the following classes:

```
Person

↓

Employee

├── Faculty

└── Administrator
```

### Requirements

- Use inheritance.
- Override methods.
- Use `super()`.
- Display MRO.
- Demonstrate polymorphism.
- Show constructor chaining.

---

# Best Practices

✅ Keep inheritance hierarchies simple.

✅ Use `super()` instead of direct parent calls.

✅ Follow the IS-A relationship.

✅ Prefer composition when appropriate.

✅ Keep parent classes generic and reusable.

✅ Avoid unnecessary multiple inheritance.

---

# Common Mistakes

❌ Deep inheritance chains.

❌ Ignoring MRO.

❌ Calling parent constructors directly.

❌ Using inheritance only to reuse code.

❌ Creating unrelated parent-child relationships.

---

# Interview Questions

## Basic

- What is inheritance?
- What is multiple inheritance?
- What is hybrid inheritance?

---

## Intermediate

- Explain Method Resolution Order (MRO).
- What is the Diamond Problem?
- How does `super()` work in multiple inheritance?
- What is cooperative inheritance?

---

## Advanced

- Explain the C3 Linearization Algorithm.
- Difference between inheritance and composition.
- When should composition be preferred?
- How does Python resolve method conflicts?

---

# Module Summary

After completing Module 04, you can:

✅ Implement Single, Multiple, Multilevel, Hierarchical, and Hybrid Inheritance

✅ Override methods effectively

✅ Use `super()` correctly

✅ Understand Constructor Chaining

✅ Interpret and use Method Resolution Order (MRO)

✅ Solve the Diamond Problem

✅ Apply Cooperative Inheritance

✅ Choose between Inheritance and Composition

✅ Design reusable object hierarchies

---

# Next Module

**Module 05 – Polymorphism, Duck Typing & Operator Overloading**

Topics include:

- Runtime Polymorphism
- Duck Typing
- Method Overriding vs Polymorphism
- Method Overloading Alternatives
- Operator Overloading
- Magic (Dunder) Methods
- Built-in Polymorphism
- Practical OOP Design
