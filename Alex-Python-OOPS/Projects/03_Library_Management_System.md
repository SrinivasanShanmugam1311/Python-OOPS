# Project 03 – Library Management System

## File Name

```
03_Library_Management_System.md
```

---

# Level

```
Intermediate → Advanced
```

---

# Domain

```
Library Automation Application
```

---

# Project Overview

A real-world library management system developed using Python OOP concepts.

The system manages:

- Books
- Authors
- Members
- Librarians
- Book Inventory
- Borrowing
- Returning
- Fines
- Notifications

This project focuses on:

- Object Relationships
- Collection Handling
- Encapsulation
- Iterators
- Magic Methods
- SOLID Architecture

---

# 1. Project Objective

Build a scalable library application using:

- Object-Oriented Programming
- Data Structures
- Design Patterns
- Exception Handling
- Testing Framework

---

# 2. Real World Problem

A library contains multiple entities:

```
Library

 |

 |------------|

Books       Members

 |

 |

Borrow Transactions
```

A good system should handle:

- Thousands of books
- Multiple users
- Search functionality
- Borrowing rules
- Fine calculation

---

# 3. Project Features

---

# Book Management

Features:

- Add Book
- Remove Book
- Search Book
- Update Book Details


Book Information:

```
Book ID

Title

Author

Category

Availability
```

---

# Member Management

Features:

- Register Member
- Update Member
- View Borrow History


Member Information:

```
Member ID

Name

Email

Phone

Books Borrowed
```

---

# Borrow / Return System

Operations:

```
Issue Book

Return Book

Renew Book

Calculate Fine
```

---

# Search System

Search By:

```
Title

Author

Category

ISBN
```

---

# Fine Management

Rules:

```
Late Return

Lost Book

Damaged Book
```

---

# 4. OOP Concepts Used

| Concept | Usage |
|-|-|
| Classes | Book, Member, Library |
| Encapsulation | Book availability |
| Composition | Library contains books |
| Association | Member borrows books |
| Inheritance | User hierarchy |
| Polymorphism | Fine calculation |
| Dataclass | Book records |
| Iterator | Book collection traversal |
| Magic Methods | Custom collection |

---

# 5. Object Relationships

---

# Library → Books

One-to-Many

```
Library

 |

 |---- Book

 |---- Book

 |---- Book
```

---

# Member → Borrow Records

One-to-Many

```
Member

 |

Borrow History
```

---

# Book ↔ Author

Many-to-One

```
Book

 |

Author
```

---

# 6. Design Principles Used

---

# Single Responsibility

Separate:

```
Book Service

Member Service

Borrow Service

Fine Service
```

---

# Open Closed Principle

New book types:

```
Physical Book

EBook

Magazine
```

can be added easily.

---

# Dependency Inversion

Services depend on interfaces.

---

# 7. Design Patterns Used

---

# Factory Pattern

Create different resources:

```
BookFactory

      |

----------------

Book

Magazine

EBook
```

---

# Strategy Pattern

Fine calculation:

```
Fine Strategy

      |

----------------

Normal Fine

Premium Member Fine

Student Fine
```

---

# Iterator Pattern

Custom book collection traversal.

---

# Observer Pattern

Notifications:

```
Book Returned

      |

Member Notification
```

---

# 8. Project Folder Structure

```
03_Library_Management_System/

│
├── main.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── models/
│   ├── __init__.py
│   ├── book.py
│   ├── author.py
│   ├── member.py
│   ├── librarian.py
│   ├── borrow_record.py
│   └── fine.py
│
├── collections/
│   ├── __init__.py
│   └── book_collection.py
│
├── services/
│   ├── __init__.py
│   ├── book_service.py
│   ├── member_service.py
│   ├── borrow_service.py
│   └── fine_service.py
│
├── factories/
│   └── book_factory.py
│
├── strategies/
│   └── fine_strategy.py
│
├── exceptions/
│   └── library_exceptions.py
│
├── utils/
│   ├── logger.py
│   └── validator.py
│
├── database/
│   └── library.json
│
├── tests/
│   ├── test_book.py
│   ├── test_member.py
│   └── test_borrow.py
│
├── requirements.txt
│
└── README.md
```

---

# 9. File Responsibilities

| File | Responsibility |
|-|-|
| book.py | Book entity |
| author.py | Author details |
| member.py | Library member |
| borrow_record.py | Issue/return tracking |
| fine.py | Fine calculation |
| services | Business logic |
| collections | Custom containers |
| factories | Object creation |
| strategies | Dynamic behavior |

---

# 10. Code Implementation

---

# models/book.py

```python
from dataclasses import dataclass


@dataclass
class Book:


    book_id:int

    title:str

    author:str

    available:bool=True



    def borrow(self):

        if not self.available:

            raise Exception(
                "Book not available"
            )


        self.available=False



    def return_book(self):

        self.available=True
```

---

# models/member.py

```python
class Member:


    def __init__(
        self,
        member_id,
        name
    ):

        self.member_id = member_id

        self.name = name

        self.books=[]



    def borrow_book(
        self,
        book
    ):

        self.books.append(book)
```

---

# 11. Custom Collection Class

## collections/book_collection.py

Using Python Data Model.

```python
class BookCollection:


    def __init__(self):

        self.books=[]



    def add_book(
        self,
        book
    ):

        self.books.append(book)



    def __len__(self):

        return len(self.books)



    def __iter__(self):

        return iter(self.books)



    def __getitem__(
        self,
        index
    ):

        return self.books[index]
```

---

# Usage

```python
collection = BookCollection()


collection.add_book(
    "Python OOP"
)


print(len(collection))
```

---

# Concepts Used

Magic Methods:

```
__len__

__iter__

__getitem__
```

---

# 12. Factory Pattern

## factories/book_factory.py

```python
from models.book import Book



class BookFactory:


    @staticmethod
    def create_book(
        book_type,
        id,
        title,
        author
    ):


        return Book(

            id,

            title,

            author

        )
```

---

# 13. Strategy Pattern

## strategies/fine_strategy.py

```python
from abc import ABC,abstractmethod



class FineStrategy(ABC):


    @abstractmethod
    def calculate(self,days):

        pass



class NormalFine(FineStrategy):


    def calculate(
        self,
        days
    ):

        return days * 5



class StudentFine(FineStrategy):


    def calculate(
        self,
        days
    ):

        return days * 2
```

---

# 14. Service Layer

## services/borrow_service.py

```python
class BorrowService:


    def issue_book(
        self,
        member,
        book
    ):


        book.borrow()

        member.borrow_book(book)


        print(
            "Book Issued"
        )



    def return_book(
        self,
        book
    ):

        book.return_book()

        print(
            "Book Returned"
        )
```

---

# 15. Main Application

## main.py

```python
from models.book import Book

from models.member import Member

from services.borrow_service import BorrowService



book = Book(

    101,

    "Python OOP",

    "Alex"

)



member = Member(

    1,

    "John"

)



service = BorrowService()



service.issue_book(

    member,

    book

)



print(book.available)


service.return_book(book)


print(book.available)
```

---

# Output

```
Book Issued

False

Book Returned

True
```

---

# 16. Testing

## tests/test_book.py

```python
import unittest

from models.book import Book



class TestBook(unittest.TestCase):


    def test_book_borrow(self):


        book = Book(

            1,

            "Python",

            "Author"

        )


        book.borrow()


        self.assertFalse(

            book.available

        )



if __name__=="__main__":

    unittest.main()
```

---

# 17. Execution Flow

```
main.py

 |

Book

 |

Member

 |

Borrow Service

 |

Fine Strategy

 |

Notification
```

---

# 18. Future Enhancements

Add:

```
Database Integration

Online Search

Barcode System

User Login

Email Notifications

Book Recommendation System
```

---

# 19. Learning Outcome

After completing this project:

You understand:

✅ Object Relationships

✅ Custom Collection Classes

✅ Magic Methods

✅ Iterator Pattern

✅ Strategy Pattern

✅ Factory Pattern

✅ Library Domain Modeling

✅ Professional Python Architecture

---

# Project Completion Level

```
Python OOP              ⭐⭐⭐⭐⭐

Data Model              ⭐⭐⭐⭐⭐

Relationships           ⭐⭐⭐⭐⭐

Design Patterns         ⭐⭐⭐⭐

Real Application        ⭐⭐⭐⭐⭐
```

---

# Next Project

```
04_Ecommerce_Management_System.md
```

Focus:

- Product Catalog
- Cart System
- Payment Framework
- Strategy Pattern
- Observer Pattern
- Order Processing
