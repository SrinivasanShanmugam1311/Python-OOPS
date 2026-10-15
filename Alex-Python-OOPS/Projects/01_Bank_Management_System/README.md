# Project 01 – Bank Management System

## Level

Intermediate → Advanced

## Domain

Banking Application

---

## 1. Project Overview

The **Bank Management System** is a Python-based application developed using Object-Oriented Programming and real-world application architecture concepts.

The application manages:

* Customers
* Bank Accounts
* Savings Accounts
* Current Accounts
* Deposits
* Withdrawals
* Account Balances
* Transactions
* Transaction History

The project demonstrates how to organize a Python OOP application into multiple modules and packages.

---

## 2. Project Objectives

The project demonstrates:

* Python Object-Oriented Programming
* Classes and Objects
* Encapsulation
* Abstraction
* Inheritance
* Polymorphism
* Composition
* Abstract Base Classes
* Dataclasses
* Custom Exceptions
* Service Layer
* Separation of Concerns
* Unit Testing
* Package Organization
* Error Handling

---

## 3. Project Structure

```text
01_Bank_Management_System/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── customer.py
│   ├── account.py
│   ├── savings_account.py
│   ├── current_account.py
│   └── transaction.py
│
├── services/
│   ├── __init__.py
│   └── bank_service.py
│
├── exceptions/
│   ├── __init__.py
│   └── bank_exceptions.py
│
├── tests/
│   ├── test_customer.py
│   ├── test_account.py
│   └── test_transaction.py
│
├── requirements.txt
└── README.md
```

---

## 4. Application Architecture

The project follows a simple layered architecture.

```text
                    main.py
                       |
                       v
                 BankService
                       |
          +------------+------------+
          |            |            |
          v            v            v
       Customer     Account    Transaction
                       |
                +------+------+
                |             |
                v             v
        SavingsAccount   CurrentAccount
                       
                       |
                       v
                  Exceptions
```

### Responsibility of Each Layer

```text
main.py
    ↓
User interaction and menu

services/
    ↓
Business logic

models/
    ↓
Domain objects

exceptions/
    ↓
Application-specific errors

tests/
    ↓
Unit testing
```

---

# 5. Models

The `models` package contains the main entities of the banking system.

```text
models/
│
├── customer.py
├── account.py
├── savings_account.py
├── current_account.py
└── transaction.py
```

---

## 5.1 Customer

`Customer` represents a bank customer.

```python
customer = Customer(
    customer_id=1,
    name="Alex",
    email="alex@example.com"
)
```

A customer can have multiple accounts.

```text
Customer
   |
   +-- SavingsAccount
   |
   +-- CurrentAccount
```

This represents a **HAS-A relationship**.

The customer maintains a collection of accounts:

```python
self.accounts = []
```

Accounts can be added using:

```python
customer.add_account(account)
```

and retrieved using:

```python
customer.get_accounts()
```

---

# 6. Account

`Account` is the base class for bank accounts.

```python
class Account(ABC):
    ...
```

It contains common functionality such as:

* Account number
* Account holder
* Balance
* Deposit
* Balance retrieval

The balance is encapsulated using:

```python
self.__balance
```

External code accesses the balance through:

```python
account.get_balance()
```

instead of directly modifying the internal balance.

---

# 7. Savings Account

`SavingsAccount` inherits from `Account`.

```python
class SavingsAccount(Account):
    ...
```

A savings account does not allow withdrawal beyond the available balance.

Example:

```python
account = SavingsAccount(
    account_number=1001,
    holder="Alex",
    balance=5000
)

account.withdraw(2000)
```

Remaining balance:

```text
3000
```

If the customer tries:

```python
account.withdraw(6000)
```

the operation fails because the available balance is insufficient.

---

# 8. Current Account

`CurrentAccount` also inherits from `Account`.

```python
class CurrentAccount(Account):
    ...
```

The current account supports an overdraft facility.

Default overdraft:

```python
overdraft_limit = 5000
```

For example:

```text
Balance          = 1000
Overdraft Limit  = 5000
Available        = 6000
```

Therefore a withdrawal within the available amount can be processed.

---

# 9. Inheritance

The account hierarchy is:

```text
                Account
                   |
          +--------+--------+
          |                 |
          v                 v
   SavingsAccount     CurrentAccount
```

Common functionality is placed in the parent class:

```text
Account
    |
    +-- account_number
    +-- holder
    +-- balance
    +-- deposit()
    +-- get_balance()
```

Specialized behavior is implemented by child classes.

---

# 10. Polymorphism

Both account types provide the same method:

```python
withdraw()
```

But the behavior is different.

```python
accounts = [
    SavingsAccount(
        account_number=1001,
        holder="Alex",
        balance=5000
    ),

    CurrentAccount(
        account_number=1002,
        holder="John",
        balance=1000
    )
]

for account in accounts:
    account.withdraw(1000)
```

The same method call:

```python
account.withdraw()
```

can execute different implementations depending on the actual object.

This demonstrates **runtime polymorphism**.

---

# 11. Abstraction

`Account` acts as the common abstraction for all bank accounts.

```python
from abc import ABC

class Account(ABC):
    ...
```

Different account types provide their own withdrawal behavior.

```text
Account
   |
   +-- SavingsAccount
   |      └── withdraw()
   |
   +-- CurrentAccount
          └── withdraw()
```

The service layer does not need to know the exact account type when calling:

```python
account.withdraw(amount)
```

---

# 12. Encapsulation

The account balance is stored internally:

```python
self.__balance
```

The class controls how the balance is changed.

Deposit:

```python
account.deposit(1000)
```

Withdrawal:

```python
account.withdraw(500)
```

Balance:

```python
account.get_balance()
```

This prevents external code from directly manipulating the internal balance.

---

# 13. Transaction

Transactions are represented using a dataclass.

```python
@dataclass
class Transaction:
    transaction_id: int
    transaction_type: str
    amount: float
    account_number: int
    timestamp: datetime
```

A transaction contains:

* Transaction ID
* Transaction Type
* Amount
* Account Number
* Timestamp

Example:

```python
transaction = Transaction(
    transaction_id=1,
    transaction_type="DEPOSIT",
    amount=5000,
    account_number=1001,
    timestamp=datetime.now()
)
```

---

# 14. Dataclass

The `Transaction` class uses:

```python
@dataclass
```

Python automatically provides useful functionality such as:

```text
__init__()
__repr__()
__eq__()
```

This reduces boilerplate code.

---

# 15. Service Layer

The `services` package contains business logic.

```text
services/
│
├── __init__.py
└── bank_service.py
```

The main service class is:

```python
BankService
```

It manages:

* Customer creation
* Customer lookup
* Account creation
* Account lookup
* Deposits
* Withdrawals
* Balance checking
* Transaction history
* Customer display
* Account display

---

# 16. Creating a Customer

```python
bank = BankService()

customer = bank.create_customer(
    "Alex",
    "alex@example.com"
)
```

The service creates a `Customer` object and stores it.

The customer receives an automatically generated ID.

```text
Customer ID : 1
```

---

# 17. Creating a Savings Account

```python
account = bank.create_savings_account(
    customer.customer_id,
    5000
)
```

The service:

1. Finds the customer
2. Validates the initial balance
3. Creates the account
4. Stores the account
5. Adds the account to the customer
6. Generates the account number

Example:

```text
Account Number : 1001
Holder         : Alex
Balance        : 5000
```

---

# 18. Creating a Current Account

```python
account = bank.create_current_account(
    customer.customer_id,
    5000
)
```

The account is created and associated with the customer.

---

# 19. Deposit

Money can be deposited through the service layer.

```python
bank.deposit(
    account.account_number,
    2000
)
```

The service:

```text
Find Account
     ↓
Validate Amount
     ↓
Deposit
     ↓
Create Transaction
     ↓
Store Transaction
```

---

# 20. Withdrawal

Money can be withdrawn through:

```python
bank.withdraw(
    account.account_number,
    1000
)
```

The service:

```text
Find Account
     ↓
Validate Amount
     ↓
account.withdraw()
     ↓
Create Transaction
     ↓
Store Transaction
```

The actual withdrawal rule is delegated to the account.

Therefore:

```text
SavingsAccount
    ↓
Savings withdrawal rules

CurrentAccount
    ↓
Current withdrawal + overdraft rules
```

This is an important example of **polymorphism**.

---

# 21. Balance

Balance can be retrieved using:

```python
balance = bank.get_balance(
    account.account_number
)
```

Example:

```text
Account Number : 1001
Balance        : 6000
```

---

# 22. Transaction History

Transaction history can be retrieved using:

```python
transactions = bank.get_transactions(
    account.account_number
)
```

Or displayed using:

```python
bank.display_transactions(
    account.account_number
)
```

Example:

```text
============================================================
TRANSACTION HISTORY
============================================================

Transaction ID : 1
Type           : DEPOSIT
Amount         : 2000
Account        : 1001
Date           : 2026-08-08 10:30:00
```

---

# 23. Custom Exceptions

The project contains a dedicated exception layer.

```text
exceptions/
│
├── __init__.py
└── bank_exceptions.py
```

The base exception is:

```python
class BankError(Exception):
    pass
```

Specific exceptions inherit from it.

```text
BankError
   |
   +-- CustomerNotFoundError
   |
   +-- CustomerAlreadyExistsError
   |
   +-- AccountNotFoundError
   |
   +-- AccountAlreadyExistsError
   |
   +-- InvalidAmountError
   |
   +-- InsufficientBalanceError
   |
   +-- TransferError
   |
   +-- AccountOperationError
```

---

# 24. Customer Not Found

Instead of:

```python
raise ValueError("Customer not found")
```

the application uses:

```python
raise CustomerNotFoundError(customer_id)
```

This makes the error more meaningful.

Example:

```text
Customer not found: 99
```

---

# 25. Account Not Found

```python
raise AccountNotFoundError(account_number)
```

Example:

```text
Account not found: 9999
```

---

# 26. Invalid Amount

An invalid amount is rejected.

Examples:

```text
0
-100
```

The service raises:

```python
raise InvalidAmountError(amount)
```

---

# 27. Insufficient Balance

If a savings account does not have enough money:

```python
raise InsufficientBalanceError(
    account_number,
    requested_amount,
    available_balance
)
```

Example:

```text
Insufficient balance in account 1001.
Requested: 10000
Available: 5000
```

---

# 28. Exception Hierarchy

Because all custom exceptions inherit from `BankError`, we can handle them together.

```python
try:
    bank.withdraw(1001, 10000)

except BankError as error:
    print(error)
```

Or handle a specific error:

```python
try:
    bank.withdraw(1001, 10000)

except InsufficientBalanceError as error:
    print(error)
```

This gives the application both general and specific error handling.

---

# 29. Main Application

`main.py` is the entry point of the application.

Its responsibility is mainly:

* Display menu
* Read user input
* Call service methods
* Display results
* Handle exceptions

It does not contain the actual banking business rules.

Architecture:

```text
User
  ↓
main.py
  ↓
BankService
  ↓
Models
```

---

# 30. Main Menu

Run:

```powershell
python main.py
```

The application displays:

```text
============================================================
              BANK MANAGEMENT SYSTEM
============================================================

1. Create Customer
2. Create Savings Account
3. Create Current Account
4. Deposit Money
5. Withdraw Money
6. Check Balance
7. View Customers
8. View Accounts
9. View Transactions
0. Exit
============================================================
```

---

# 31. Example Workflow

## Step 1 – Create Customer

```text
Enter your choice: 1

Enter customer name : Alex
Enter customer email: alex@example.com
```

Result:

```text
Customer created successfully.
Customer ID : 1
```

---

## Step 2 – Create Savings Account

```text
Enter your choice: 2

Enter customer ID    : 1
Enter initial balance: 5000
```

Result:

```text
Savings account created successfully.
Account Number : 1001
Balance        : 5000
```

---

## Step 3 – Deposit

```text
Enter your choice: 4

Enter account number: 1001
Enter deposit amount: 2000
```

New balance:

```text
7000
```

---

## Step 4 – Withdraw

```text
Enter your choice: 5

Enter account number   : 1001
Enter withdrawal amount: 1000
```

New balance:

```text
6000
```

---

## Step 5 – Check Balance

```text
Enter your choice: 6

Enter account number: 1001
```

Result:

```text
Account Number: 1001
Balance       : 6000
```

---

# 32. Unit Testing

The project uses Python's built-in `unittest` framework.

Tests are located in:

```text
tests/
│
├── test_customer.py
├── test_account.py
└── test_transaction.py
```

---

# 33. Customer Tests

`test_customer.py` verifies:

* Customer creation
* Customer properties
* Initial account collection
* Adding accounts
* Removing accounts
* Getting accounts
* String representation
* Display method

Run:

```powershell
python -m unittest tests.test_customer -v
```

---

# 34. Account Tests

`test_account.py` verifies:

* Savings account creation
* Current account creation
* Deposits
* Multiple deposits
* Invalid deposits
* Savings withdrawals
* Insufficient balance
* Current account withdrawals
* Overdraft
* Overdraft limits
* Balance encapsulation
* String representation
* Polymorphism

Run:

```powershell
python -m unittest tests.test_account -v
```

---

# 35. Transaction Tests

`test_transaction.py` verifies:

* Transaction creation
* Deposit transaction
* Withdrawal transaction
* Dataclass representation
* Dataclass equality
* Dataclass inequality
* Display method

Run:

```powershell
python -m unittest tests.test_transaction -v
```

---

# 36. Run All Tests

From the project root:

```powershell
python -m unittest discover -v
```

Expected result:

```text
----------------------------------------------------------------------
Ran ... tests

OK
```

---

# 37. Python Version

Recommended:

```text
Python 3.10+
```

The project uses Python standard library features such as:

```python
abc
dataclasses
datetime
unittest
```

---

# 38. Requirements

The project currently has **no third-party dependencies**.

`requirements.txt` therefore contains no packages that need to be installed with `pip`.

The project uses only Python's standard library.

---

# 39. Virtual Environment

Although no external packages are required, using a virtual environment is recommended for real-world projects.

Create:

```powershell
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Run the application:

```powershell
python main.py
```

Run tests:

```powershell
python -m unittest discover -v
```

---

# 40. Separation of Concerns

The project intentionally separates responsibilities.

```text
models/
    ↓
Represents data and domain objects

services/
    ↓
Contains business operations

exceptions/
    ↓
Contains application-specific errors

tests/
    ↓
Verifies application behavior

main.py
    ↓
Handles user interaction
```

This is much better than placing everything inside `main.py`.

---

# 41. Why This Architecture?

A beginner application might put everything into one file:

```text
main.py
│
├── Customer
├── Account
├── Deposit
├── Withdraw
├── Transaction
├── Validation
├── Error Handling
└── Menu
```

As the project grows, this becomes difficult to maintain.

Our structure separates responsibilities:

```text
main.py
    ↓
services
    ↓
models
    ↓
exceptions
```

This makes the project easier to:

* Understand
* Test
* Debug
* Maintain
* Extend
* Refactor

---

# 42. OOP Concepts Demonstrated

| Concept             | Implementation                  |
| ------------------- | ------------------------------- |
| Class               | Customer, Account, Transaction  |
| Object              | Customer and Account objects    |
| Encapsulation       | Private `__balance`             |
| Abstraction         | Account                         |
| Inheritance         | SavingsAccount / CurrentAccount |
| Polymorphism        | `withdraw()`                    |
| Composition         | Customer owns accounts          |
| Dataclass           | Transaction                     |
| Class Variable      | `overdraft_limit`               |
| Magic Method        | `__str__`                       |
| Abstract Base Class | Account                         |
| Custom Exceptions   | BankError hierarchy             |

---

# 43. Software Design Concepts

The project also introduces:

* Separation of Concerns
* Layered Architecture
* Service Layer
* Custom Exception Hierarchy
* Modular Design
* Loose Coupling
* Code Reusability
* Unit Testing

---

# 44. Current Limitations

The current implementation stores all information in memory.

```text
Application starts
       ↓
Data created
       ↓
Data stored in Python lists
       ↓
Application exits
       ↓
Data is lost
```

There is currently no database persistence.

---

# 45. Future Enhancements

The project can later be extended with:

* Money Transfer
* Account Closing
* Interest Calculation
* Persistent Storage
* SQLite
* MySQL
* Repository Pattern
* Logging
* Configuration Management
* Authentication
* Role-Based Access
* REST API
* Web Interface
* GUI
* pytest
* Integration Testing
* Factory Pattern
* Strategy Pattern

---

# 46. Possible Next Version

A future version can introduce:

```text
User Interface
      ↓
Service Layer
      ↓
Repository Layer
      ↓
Database
```

For example:

```text
main.py
   ↓
BankService
   ↓
BankRepository
   ↓
SQLite / MySQL
```

This allows the application to move from an in-memory project to a persistent real-world application.

---

# 47. Learning Progression

This project represents the transition from basic Python OOP to application architecture.

```text
Python Classes
       ↓
Objects
       ↓
Encapsulation
       ↓
Inheritance
       ↓
Polymorphism
       ↓
Abstraction
       ↓
Composition
       ↓
Packages
       ↓
Service Layer
       ↓
Custom Exceptions
       ↓
Unit Testing
       ↓
Application Architecture
```

---

# 48. Project Completion Checklist

```text
[✓] Project structure
[✓] Customer model
[✓] Account base class
[✓] Savings account
[✓] Current account
[✓] Transaction model
[✓] Bank service
[✓] Custom exceptions
[✓] Unit tests
[✓] Menu-driven application
[✓] Error handling
[✓] README
[✓] requirements.txt
```

---

# 49. Final Architecture

```text
01_Bank_Management_System/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── customer.py
│   ├── account.py
│   ├── savings_account.py
│   ├── current_account.py
│   └── transaction.py
│
├── services/
│   ├── __init__.py
│   └── bank_service.py
│
├── exceptions/
│   ├── __init__.py
│   └── bank_exceptions.py
│
├── tests/
│   ├── test_customer.py
│   ├── test_account.py
│   └── test_transaction.py
│
├── requirements.txt
└── README.md
```

---

# 50. Final Execution

From the project directory:

```powershell
python main.py
```

Run all tests:

```powershell
python -m unittest discover -v
```

The project demonstrates the complete journey:

```text
Python OOP
     ↓
Multiple Classes
     ↓
Inheritance + Polymorphism
     ↓
Packages + Modules
     ↓
Service Layer
     ↓
Custom Exceptions
     ↓
Unit Testing
     ↓
Menu-Driven Application
```

**Project 01 – Bank Management System Complete**
