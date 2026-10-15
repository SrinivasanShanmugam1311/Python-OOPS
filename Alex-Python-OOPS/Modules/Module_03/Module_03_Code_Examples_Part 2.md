# Python Object-Oriented Programming (OOP) Using Python

# Module 03 – Encapsulation & Data Protection

## Module_03_Code_Examples.md (Part 2)

**Course Level:** Intermediate → Advanced

---

# Topic 12 – Input Validation

## What is Input Validation?

Validation ensures that only valid data is accepted before updating an object's state.

Without validation, objects may contain incorrect or inconsistent data.

---

## Example 1 – Age Validation

```python
class Person:

    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):

        if 0 <= value <= 120:
            self.__age = value
        else:
            print("Invalid Age")

person = Person()

person.age = 25

print(person.age)

person.age = -10
```

### Output

```text
25
Invalid Age
```

---

## Example 2 – Marks Validation

```python
class Student:

    def __init__(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):

        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Marks should be between 0 and 100")

student = Student()

student.marks = 92

print(student.marks)
```

Output

```text
92
```

---

# Topic 13 – Business Rules

Business rules are validations based on application requirements.

---

## Example – Minimum Balance

```python
class BankAccount:

    MINIMUM_BALANCE = 1000

    def __init__(self):
        self.__balance = 5000

    def withdraw(self, amount):

        if self.__balance - amount >= self.MINIMUM_BALANCE:

            self.__balance -= amount

            print("Withdrawal Successful")

        else:

            print("Minimum Balance Rule Violated")

    def display(self):
        print(self.__balance)

account = BankAccount()

account.withdraw(3000)

account.display()
```

### Output

```text
Withdrawal Successful
2000
```

---

# Topic 14 – Exception Handling

Validation should raise exceptions whenever appropriate.

---

## Example 1

```python
class Student:

    def __init__(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):

        if value < 0:

            raise ValueError("Marks cannot be negative")

        self.__marks = value

student = Student()

try:

    student.marks = -5

except ValueError as error:

    print(error)
```

Output

```text
Marks cannot be negative
```

---

## Example 2

```python
class Employee:

    def __init__(self):
        self.__salary = 0

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):

        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be numeric")

        if value <= 0:
            raise ValueError("Salary must be positive")

        self.__salary = value

employee = Employee()

try:

    employee.salary = "abc"

except Exception as error:

    print(error)
```

Output

```text
Salary must be numeric
```

---

# Topic 15 – Data Integrity

A class should always remain in a valid state.

---

## Example

```python
class Product:

    def __init__(self, price):

        if price <= 0:
            raise ValueError("Invalid Price")

        self.__price = price

    @property
    def price(self):
        return self.__price

product = Product(500)

print(product.price)
```

Output

```text
500
```

---

# Topic 16 – Controlled Updates

Instead of changing variables directly, expose methods.

---

## Example

```python
class Employee:

    def __init__(self):

        self.__salary = 50000

    def increment(self, amount):

        if amount > 0:
            self.__salary += amount

    def display(self):

        print(self.__salary)

employee = Employee()

employee.increment(5000)

employee.display()
```

Output

```text
55000
```

---

# Topic 17 – Immutable Objects

An immutable object cannot be modified after creation.

---

## Example

```python
class Student:

    def __init__(self, roll):

        self.__roll = roll

    @property
    def roll(self):

        return self.__roll

student = Student(101)

print(student.roll)
```

Output

```text
101
```

Attempting

```python
student.roll = 200
```

Results in

```text
AttributeError
```

---

# Hands-on Project 1 – Secure Bank Account

```python
class BankAccount:

    def __init__(self, account_number):

        self.__account_number = account_number

        self.__balance = 0

    @property
    def account_number(self):

        return self.__account_number

    @property
    def balance(self):

        return self.__balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

        else:

            print("Insufficient Balance")

account = BankAccount("SB1001")

account.deposit(5000)

account.withdraw(1200)

print(account.account_number)

print(account.balance)
```

Output

```text
SB1001
3800
```

---

# Hands-on Project 2 – ATM

```python
class ATM:

    def __init__(self, pin, balance):

        self.__pin = pin

        self.__balance = balance

    def withdraw(self, entered_pin, amount):

        if entered_pin != self.__pin:

            print("Invalid PIN")

            return

        if amount > self.__balance:

            print("Insufficient Balance")

            return

        self.__balance -= amount

        print("Remaining:", self.__balance)

atm = ATM(1234, 10000)

atm.withdraw(1234, 2500)
```

Output

```text
Remaining: 7500
```

---

# Hands-on Project 3 – Wallet

```python
class Wallet:

    def __init__(self):

        self.__money = 0

    def add_money(self, amount):

        if amount > 0:
            self.__money += amount

    def spend(self, amount):

        if amount <= self.__money:
            self.__money -= amount

    @property
    def balance(self):

        return self.__money

wallet = Wallet()

wallet.add_money(3000)

wallet.spend(800)

print(wallet.balance)
```

Output

```text
2200
```

---

# Hands-on Project 4 – Employee Salary

```python
class Employee:

    def __init__(self):

        self.__salary = 30000

    @property
    def salary(self):

        return self.__salary

    @salary.setter
    def salary(self, value):

        if value > 0:
            self.__salary = value

employee = Employee()

employee.salary = 45000

print(employee.salary)
```

Output

```text
45000
```

---

# Hands-on Project 5 – Student Marks

```python
class Student:

    def __init__(self):

        self.__marks = 0

    @property
    def marks(self):

        return self.__marks

    @marks.setter
    def marks(self, value):

        if 0 <= value <= 100:
            self.__marks = value

student = Student()

student.marks = 96

print(student.marks)
```

Output

```text
96
```

---

# Mini Assignment

Build a **Secure Banking System** with:

- Private Account Number
- Private Balance
- Deposit
- Withdraw
- PIN Validation
- Minimum Balance Rule
- Transaction History
- Read-only Account Number
- Exception Handling
- Properties

---

# Best Practices

✅ Keep sensitive data private.

✅ Validate all external inputs.

✅ Raise meaningful exceptions.

✅ Use `@property` for controlled access.

✅ Prefer methods like `deposit()` and `withdraw()` instead of directly modifying data.

✅ Preserve object integrity at all times.

---

# Common Mistakes

❌ Making sensitive variables public.

❌ Skipping validation.

❌ Ignoring business rules.

❌ Returning mutable internal objects directly.

❌ Catching every exception without proper handling.

---

# Interview Questions

## Basic

- What is Encapsulation?
- Difference between Public, Protected, and Private Members?
- Why is `@property` used?

---

## Intermediate

- Explain Name Mangling.
- Difference between Getter/Setter and Property.
- What is Data Integrity?
- Why should validation be performed?

---

## Advanced

- Explain Business Rules with examples.
- How would you design a secure Bank Account class?
- What are immutable objects?
- How do properties improve API design?
- Why is encapsulation important in enterprise applications?

---

# Module Summary

After completing Module 03, you can:

✅ Implement Encapsulation

✅ Use Public, Protected, and Private Members

✅ Understand Name Mangling

✅ Build Read-only and Computed Properties

✅ Validate Inputs

✅ Enforce Business Rules

✅ Handle Exceptions

✅ Preserve Data Integrity

✅ Design Secure Classes

✅ Build Pythonic APIs using `@property`

---

# Next Module

**Module 04 – Inheritance & Code Reusability**

Topics include:

- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance
- Hybrid Inheritance
- Method Overriding
- `super()`
- Method Resolution Order (MRO)
- Mixins
- Composition vs Inheritance
