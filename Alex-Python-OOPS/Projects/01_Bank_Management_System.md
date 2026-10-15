# Project 01 – Bank Management System

## File Name

```
01_Bank_Management_System.md
```

---

# Level

```
Intermediate → Advanced
```

---

# Domain

```
Banking Application
```

---

# Project Overview

A real-world banking system developed using Python OOP principles.

The application manages:

- Customers
- Bank Accounts
- Transactions
- Deposits
- Withdrawals
- Money Transfers
- Account Types
- Transaction History

The project demonstrates professional Python application architecture.

---

# 1. Project Objective

Build a scalable banking application using:

- Object-Oriented Programming
- SOLID Principles
- Design Patterns
- Exception Handling
- Logging
- Testing
- Modular Architecture

---

# 2. Real World Problem

A banking application needs to manage different entities:

```
Customer

     |

     |

Accounts

     |

     |

Transactions
```

Different account types have different rules.

Example:

```
Savings Account

- Normal withdrawal
- Interest calculation


Current Account

- Overdraft facility
```

A good design should allow adding:

```
New Account Types

New Payment Methods

New Banking Rules
```

without modifying existing code.

---

# 3. Project Features

## Customer Management

Features:

- Create Customer
- Update Customer
- View Customer Details
- Manage Multiple Accounts


---

## Account Management

Supported Accounts:

```
Savings Account

Current Account

Fixed Deposit Account
```

Operations:

```
Deposit Money

Withdraw Money

Check Balance

Transfer Money
```

---

## Transaction Management

Transaction Types:

```
Deposit

Withdrawal

Transfer
```

Stores:

```
Transaction ID

Date

Amount

Type
```

---

## Security Features

- Balance Protection
- Input Validation
- Custom Exceptions
- Account Validation

---

# 4. OOP Concepts Used

| Concept | Usage |
|---|---|
| Class | Customer, Account, Transaction |
| Object | Real entities |
| Encapsulation | Protect balance |
| Inheritance | Account hierarchy |
| Polymorphism | Different account behavior |
| Abstraction | Account interface |
| Composition | Customer contains accounts |
| Dataclass | Transaction model |

---

# 5. Design Principles Used

## SOLID

### Single Responsibility

Separate:

```
Models

Services

Repositories

Utilities
```

---

### Open Closed Principle

Adding new account types:

```
SavingsAccount

CurrentAccount

NewAccount
```

without changing existing classes.

---

### Dependency Inversion

Services depend on abstractions.

---

# 6. Design Patterns Used

## Factory Pattern

Account creation:

```
AccountFactory

       |

-----------------

|               |

Savings       Current
```

---

## Singleton Pattern

Used for:

```
Application Logger
```

---

## Strategy Pattern

Used for:

```
Payment Processing

Transaction Rules
```

---

# 7. Project Folder Structure

```
01_Bank_Management_System/

│
├── main.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
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
│   ├── bank_service.py
│   └── transaction_service.py
│
├── repositories/
│   ├── __init__.py
│   ├── customer_repository.py
│   └── account_repository.py
│
├── exceptions/
│   ├── __init__.py
│   └── bank_exceptions.py
│
├── patterns/
│   ├── __init__.py
│   └── account_factory.py
│
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── validator.py
│
├── database/
│   └── bank_data.json
│
├── tests/
│   ├── test_customer.py
│   ├── test_account.py
│   └── test_transaction.py
│
├── requirements.txt
│
└── README.md
```

---

# 8. File Responsibilities

| File | Responsibility |
|-|-|
| main.py | Application entry |
| customer.py | Customer entity |
| account.py | Base account |
| savings_account.py | Savings rules |
| current_account.py | Current rules |
| transaction.py | Transaction model |
| services | Business logic |
| repositories | Data storage |
| exceptions | Error handling |
| patterns | Design patterns |
| utils | Helper classes |

---

# 9. Code Implementation

---

# Model Layer

---

# models/account.py

```python
from abc import ABC, abstractmethod


class Account(ABC):


    def __init__(
        self,
        account_number,
        holder,
        balance=0
    ):

        self.account_number = account_number
        self.holder = holder

        self.__balance = balance



    def deposit(self, amount):

        if amount <= 0:

            raise ValueError(
                "Invalid Amount"
            )

        self.__balance += amount



    def get_balance(self):

        return self.__balance



    def reduce_balance(self, amount):

        self.__balance -= amount



    @abstractmethod
    def withdraw(self, amount):

        pass
```

---

# models/savings_account.py

```python
from models.account import Account


class SavingsAccount(Account):


    def withdraw(self, amount):

        if amount > self.get_balance():

            raise Exception(
                "Insufficient Balance"
            )


        self.reduce_balance(amount)

        print(
            "Savings withdrawal successful"
        )
```

---

# models/current_account.py

```python
from models.account import Account


class CurrentAccount(Account):


    overdraft_limit = 5000



    def withdraw(self, amount):

        available = (
            self.get_balance()
            +
            self.overdraft_limit
        )


        if amount > available:

            raise Exception(
                "Withdrawal limit exceeded"
            )


        self.reduce_balance(amount)

        print(
            "Current withdrawal successful"
        )
```

---

# models/customer.py

```python
class Customer:


    def __init__(
        self,
        customer_id,
        name
    ):

        self.customer_id = customer_id

        self.name = name

        self.accounts = []



    def add_account(
        self,
        account
    ):

        self.accounts.append(account)
```

---

# models/transaction.py

```python
from dataclasses import dataclass


@dataclass
class Transaction:

    transaction_id:int

    transaction_type:str

    amount:float
```

---

# Exception Layer

---

# exceptions/bank_exceptions.py

```python
class BankException(Exception):

    pass



class InsufficientBalanceError(
    BankException
):

    pass



class InvalidAccountError(
    BankException
):

    pass
```

---

# Factory Pattern

---

# patterns/account_factory.py

```python
from models.savings_account import SavingsAccount

from models.current_account import CurrentAccount



class AccountFactory:


    @staticmethod
    def create_account(
        account_type,
        number,
        holder
    ):


        if account_type == "saving":

            return SavingsAccount(
                number,
                holder
            )


        elif account_type == "current":

            return CurrentAccount(
                number,
                holder
            )


        else:

            raise Exception(
                "Invalid account type"
            )
```

---

# Service Layer

---

# services/bank_service.py

```python
class BankService:


    def transfer(
        self,
        sender,
        receiver,
        amount
    ):


        sender.withdraw(amount)

        receiver.deposit(amount)


        print(
            "Transfer completed"
        )
```

---

# Logging

---

# utils/logger.py

```python
import logging



class Logger:


    _instance = None



    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            logging.basicConfig(
                level=logging.INFO
            )


        return cls._instance
```

---

# Main Application

---

# main.py

```python
from patterns.account_factory import AccountFactory

from services.bank_service import BankService



account1 = AccountFactory.create_account(

    "saving",

    1001,

    "Alex"

)


account2 = AccountFactory.create_account(

    "current",

    1002,

    "John"

)



account1.deposit(10000)

account2.deposit(5000)



service = BankService()


service.transfer(

    account1,

    account2,

    2000

)


print(
    account1.get_balance()
)


print(
    account2.get_balance()
)
```

---

# Output

```
Transfer completed

8000

7000
```

---

# 10. Testing

## tests/test_account.py

```python
import unittest

from models.savings_account import SavingsAccount



class TestAccount(unittest.TestCase):


    def test_deposit(self):

        account = SavingsAccount(
            101,
            "Alex"
        )


        account.deposit(5000)


        self.assertEqual(

            account.get_balance(),

            5000

        )



if __name__=="__main__":

    unittest.main()
```

---

# 11. Execution Flow

```
main.py

   |

AccountFactory

   |

Account Object

   |

Service Layer

   |

Transaction

   |

Logger
```

---

# 12. Future Enhancements

Add:

```
Database Integration

REST API

Authentication

Mobile Banking

Payment Gateway

Notification System
```

---

# 13. Learning Outcome

After completing this project:

You can design:

✅ Professional Python OOP applications

✅ Banking domain models

✅ Layered architecture

✅ SOLID based classes

✅ Factory pattern

✅ Exception framework

✅ Testable code

---

# Project Completion Level

```
Python OOP Basics        ⭐⭐⭐⭐⭐

Advanced OOP             ⭐⭐⭐⭐⭐

SOLID Design             ⭐⭐⭐⭐

Design Patterns          ⭐⭐⭐⭐

Real Application Design  ⭐⭐⭐⭐⭐
```

---

# Next Project

```
02_Hospital_Management_System.md
```

Focus:

- Composition
- Object Relationships
- Doctor-Patient Management
- Appointment Scheduling
- Medical Records
- Service Architecture
