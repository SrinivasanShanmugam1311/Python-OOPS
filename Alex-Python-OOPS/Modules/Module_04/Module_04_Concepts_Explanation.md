# Python Object-Oriented Programming (OOP) Using Python

# Module 04 – Inheritance & Method Resolution Order (MRO)

> **Course Level:** Intermediate → Advanced
>
> **Duration:** 1–2 Hours
>
> **Prerequisites:** Modules 01, 02 & 03

---

# Module Overview

In previous modules, we learned how to create classes, design relationships between objects, and protect data using encapsulation.

However, when developing large applications, we often encounter situations where multiple classes share common attributes and methods. Writing the same code repeatedly leads to duplication, increased maintenance effort, and inconsistent implementations.

Python solves this problem through **Inheritance**.

Inheritance allows a new class to reuse, extend, and customize the behavior of an existing class. It promotes **code reusability**, **maintainability**, and **hierarchical design**.

This module also introduces **Method Resolution Order (MRO)**, one of Python's most powerful features for handling multiple inheritance.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand the concept of inheritance.
- Reuse code effectively.
- Extend existing classes safely.
- Override inherited behavior.
- Use `super()` correctly.
- Understand Python's Method Resolution Order (MRO).
- Solve the Diamond Problem.
- Apply cooperative inheritance.
- Decide when to use inheritance and when composition is a better choice.

---

# What is Inheritance?

Inheritance is an Object-Oriented Programming mechanism where one class acquires the properties and behaviors of another class.

The existing class is called the **Parent Class**, **Base Class**, or **Superclass**.

The new class is called the **Child Class**, **Derived Class**, or **Subclass**.

The child class automatically inherits accessible attributes and methods from the parent class.

---

# Why Do We Need Inheritance?

Without inheritance, developers often duplicate code across multiple classes.

For example:

- Car
- Bike
- Bus
- Truck

All of them may have:

- start()
- stop()
- speed
- fuel

Instead of rewriting these members, create a common `Vehicle` class and inherit from it.

Benefits include:

- Code Reusability
- Reduced Duplication
- Easier Maintenance
- Better Extensibility
- Improved Readability

---

# The IS-A Relationship

Inheritance models an **IS-A** relationship.

Examples:

- Car **is a** Vehicle.
- Dog **is an** Animal.
- Manager **is an** Employee.
- Student **is a** Person.

If the relationship is not naturally "IS-A", inheritance may not be appropriate.

---

# Types of Inheritance

Python supports multiple inheritance models.

---

## 1. Single Inheritance

One child class inherits from one parent class.

Example:

```
Animal
   │
   ▼
Dog
```

Use when there is one clear parent-child relationship.

---

## 2. Multiple Inheritance

A child class inherits from two or more parent classes.

Example:

```
Teacher
      \
       \
        ▼
   TeachingAssistant
       ▲
      /
Student
```

Advantages:

- Combines features from multiple classes.
- Encourages code reuse.

Challenges:

- Method conflicts.
- Requires understanding MRO.

---

## 3. Multilevel Inheritance

Inheritance occurs across multiple levels.

```
Person
   │
Employee
   │
Manager
```

Each level extends the previous one.

---

## 4. Hierarchical Inheritance

Multiple child classes inherit from the same parent.

```
Vehicle

├── Car

├── Bike

└── Bus
```

Useful when many specialized classes share common functionality.

---

## 5. Hybrid Inheritance

A combination of two or more inheritance types.

Example:

```
Person

├── Student

│

└── Employee

      │

TeachingAssistant
```

Hybrid inheritance often appears in enterprise applications.

---

# Method Overriding

Sometimes a child class needs different behavior than its parent.

Method Overriding allows the child class to redefine an inherited method while keeping the same method name.

Benefits:

- Customization
- Runtime flexibility
- Polymorphism support

Example scenarios:

- Animal → sound()
- Shape → area()
- Employee → calculate_salary()

---

# The super() Function

The `super()` function allows a child class to call methods from its parent class.

Common uses:

- Reusing constructor logic.
- Extending existing behavior.
- Avoiding duplicate code.

Benefits:

- Cleaner code.
- Better maintainability.
- Supports cooperative inheritance.

---

# Constructor Chaining

When both parent and child classes define constructors, `super()` enables constructor chaining.

Benefits:

- Proper initialization.
- Reuse of parent initialization.
- Consistent object creation.

---

# Method Resolution Order (MRO)

When multiple inheritance is used, Python needs a rule to determine which method should be executed.

This rule is called the **Method Resolution Order (MRO)**.

MRO defines the order in which Python searches classes for methods and attributes.

Python uses the **C3 Linearization Algorithm** to compute the MRO.

---

# Why MRO is Important

Without a consistent lookup order:

- Ambiguous method calls occur.
- Multiple inheritance becomes unpredictable.

MRO ensures:

- Deterministic behavior.
- Consistent method lookup.
- Reliable multiple inheritance.

---

# The Diamond Problem

The Diamond Problem occurs when a class inherits from two classes that both inherit from the same base class.

Example structure:

```
       Animal
       /    \
      /      \
   Bird     Mammal
      \      /
       \    /
      Bat
```

If both `Bird` and `Mammal` define the same method, Python uses the MRO to determine which implementation to execute.

---

# The mro() Method

Every Python class provides the `mro()` method.

It returns the exact order Python follows when resolving methods.

This is useful for:

- Debugging
- Understanding inheritance chains
- Verifying multiple inheritance behavior

---

# Cooperative Inheritance

Cooperative inheritance allows multiple classes to work together correctly using `super()`.

Instead of directly calling parent class methods, each class calls `super()`, allowing every class in the inheritance chain to participate.

Benefits:

- Cleaner code
- Better extensibility
- Correct behavior in multiple inheritance

---

# Favor Composition vs Inheritance

Inheritance is powerful but should not be overused.

Sometimes **Composition** provides a better design.

Inheritance represents an **IS-A** relationship.

Composition represents a **HAS-A** relationship.

Examples:

Inheritance:

- Car is a Vehicle.

Composition:

- Car has an Engine.

General guideline:

- Use inheritance when objects naturally form a hierarchy.
- Use composition when objects collaborate.

Many modern software architectures prefer composition because it provides greater flexibility.

---

# Best Practices

- Keep inheritance hierarchies shallow.
- Prefer meaningful parent classes.
- Avoid unnecessary multiple inheritance.
- Use `super()` instead of directly calling parent methods.
- Follow the Single Responsibility Principle.
- Favor composition when inheritance is not natural.
- Design reusable base classes.
- Override methods only when necessary.

---

# Common Mistakes

- Creating deep inheritance trees.
- Using inheritance only for code reuse.
- Forgetting to call `super().__init__()`.
- Overusing multiple inheritance.
- Ignoring MRO.
- Violating the IS-A relationship.
- Misusing inheritance where composition is more appropriate.

---

# Hands-on Programs

Throughout this module, you will implement:

- Animal Hierarchy
- Employee Hierarchy
- Vehicle Management System
- Shape Calculator
- Banking Hierarchy
- University Staff Hierarchy

Each example demonstrates a different inheritance concept.

---

# Mini Assignment

## University Staff Hierarchy

Design the following classes:

```
Person

↓

Employee

↓

Faculty

↓

Administrator
```

Requirements:

- Use inheritance.
- Override methods where appropriate.
- Use `super()` for constructors.
- Demonstrate MRO.
- Show polymorphic behavior.

---

# Skills Gained

After completing this module, you will be able to:

- Build reusable class hierarchies.
- Apply all inheritance models.
- Override inherited methods.
- Use `super()` effectively.
- Understand Python's C3 Linearization.
- Resolve multiple inheritance safely.
- Design scalable object-oriented systems.
- Decide between inheritance and composition.

---

# Expected Learning Outcome

By the end of this module, you will have a strong understanding of Python inheritance, method overriding, constructor chaining, multiple inheritance, Method Resolution Order (MRO), and cooperative inheritance.

These concepts form the foundation for advanced OOP topics such as Polymorphism, Abstract Base Classes, Mixins, Design Patterns, Framework Development, and Enterprise Software Design.
