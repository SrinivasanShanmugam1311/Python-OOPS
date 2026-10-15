# Project 04 – E-Commerce Management System

## File Name

```
04_Ecommerce_Management_System.md
```

---

# Level

```
Intermediate → Advanced
```

---

# Domain

```
Online Shopping Application
```

---

# Project Overview

A real-world e-commerce management system developed using Python OOP principles.

The system manages:

- Customers
- Products
- Categories
- Shopping Cart
- Orders
- Payments
- Discounts
- Inventory
- Notifications

This project focuses on:

- SOLID Principles
- Design Patterns
- Object Collaboration
- Payment Framework Design
- Business Logic Separation

---

# 1. Project Objective

Build a scalable e-commerce backend system using:

- Object-Oriented Programming
- Clean Architecture
- Design Patterns
- Exception Handling
- Testing

---

# 2. Real World Problem

An e-commerce system contains multiple components:

```
Customer

    |

    |

Shopping Cart

    |

    |

Order

    |

    |

Payment

    |

    |

Delivery
```

A good system should support:

```
New Products

New Payment Methods

New Discount Rules

New Delivery Options
```

without modifying existing code.

---

# 3. Project Features

---

# Customer Management

Features:

- Register Customer
- Login
- Update Profile
- View Orders


Customer Data:

```
Customer ID

Name

Email

Address

Orders
```

---

# Product Management

Features:

- Add Product
- Remove Product
- Update Product
- Search Product


Product Information:

```
Product ID

Name

Category

Price

Stock
```

---

# Shopping Cart

Features:

- Add Product
- Remove Product
- Update Quantity
- Calculate Total


Cart:

```
Customer

Products

Quantity

Total Amount
```

---

# Order Management

Features:

- Create Order
- Track Order
- Cancel Order
- Order History


Order Status:

```
Created

Paid

Shipped

Delivered

Cancelled
```

---

# Payment System

Payment Methods:

```
Credit Card

UPI

PayPal

Net Banking
```

---

# Discount System

Discount Types:

```
Percentage Discount

Coupon Discount

Festival Discount
```

---

# Notification System

Send:

```
Order Confirmation

Payment Success

Delivery Updates
```

---

# 4. OOP Concepts Used

| Concept | Usage |
|-|-|
| Classes | Product, Cart, Order |
| Encapsulation | Product price protection |
| Composition | Cart contains products |
| Association | Customer and Orders |
| Inheritance | Payment methods |
| Polymorphism | Different payment processing |
| Abstract Classes | Payment Interface |
| Dataclass | Product models |

---

# 5. Object Relationships

---

# Customer → Orders

One-to-Many

```
Customer

 |

 |---- Order

 |---- Order
```

---

# Cart → Products

Many-to-Many

```
Cart

 |

Products
```

---

# Order → Payment

One-to-One

```
Order

 |

Payment
```

---

# Product → Category

Many-to-One

```
Products

 |

Category
```

---

# 6. Design Principles Used

---

# Single Responsibility

Separate:

```
Product Service

Cart Service

Order Service

Payment Service
```

---

# Open Closed Principle

New payment methods:

```
UPI

Card

Wallet

Crypto
```

can be added without changing existing payment logic.

---

# Dependency Inversion

Payment service depends on abstraction.

---

# 7. Design Patterns Used

---

# Strategy Pattern

Payment processing:

```
PaymentStrategy

        |

-----------------

UPI

Card

PayPal
```

---

# Factory Pattern

Product creation:

```
ProductFactory

       |

-----------------

Physical Product

Digital Product
```

---

# Observer Pattern

Order updates:

```
Order Status Changed

          |

----------------

Customer

Email

SMS
```

---

# Builder Pattern

Create complex orders:

```
Order Builder

Customer

Products

Address

Payment
```

---

# 8. Project Folder Structure

```
04_Ecommerce_Management_System/

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
│   ├── product.py
│   ├── category.py
│   ├── cart.py
│   ├── order.py
│   ├── order_item.py
│   └── payment.py
│
├── services/
│   ├── __init__.py
│   ├── product_service.py
│   ├── cart_service.py
│   ├── order_service.py
│   └── payment_service.py
│
├── factories/
│   └── product_factory.py
│
├── strategies/
│   ├── payment_strategy.py
│   └── discount_strategy.py
│
├── builders/
│   └── order_builder.py
│
├── observers/
│   └── notification_observer.py
│
├── exceptions/
│   └── ecommerce_exceptions.py
│
├── utils/
│   ├── logger.py
│   └── validator.py
│
├── database/
│   └── ecommerce.json
│
├── tests/
│   ├── test_product.py
│   ├── test_cart.py
│   └── test_order.py
│
├── requirements.txt
│
└── README.md
```

---

# 9. File Responsibilities

| File | Responsibility |
|-|-|
| customer.py | Customer entity |
| product.py | Product entity |
| cart.py | Shopping cart |
| order.py | Order management |
| payment.py | Payment model |
| services | Business rules |
| strategies | Dynamic behavior |
| builders | Complex object creation |
| observers | Notifications |

---

# 10. Code Implementation

---

# models/product.py

```python
from dataclasses import dataclass


@dataclass
class Product:


    id:int

    name:str

    price:float

    stock:int



    def reduce_stock(
        self,
        quantity
    ):

        if quantity > self.stock:

            raise Exception(
                "Out of Stock"
            )


        self.stock -= quantity
```

---

# models/cart.py

```python
class Cart:


    def __init__(self):

        self.items=[]



    def add_product(
        self,
        product,
        quantity
    ):


        self.items.append({

            "product":product,

            "quantity":quantity

        })



    def total_price(self):

        total=0


        for item in self.items:

            total += (
                item["product"].price
                *
                item["quantity"]
            )


        return total
```

---

# models/order.py

```python
class Order:


    def __init__(
        self,
        customer,
        items
    ):

        self.customer = customer

        self.items = items

        self.status = "Created"



    def update_status(
        self,
        status
    ):

        self.status = status
```

---

# 11. Payment Strategy

---

# strategies/payment_strategy.py

```python
from abc import ABC,abstractmethod



class PaymentStrategy(ABC):


    @abstractmethod
    def pay(self,amount):

        pass



class UPIPayment(
    PaymentStrategy
):


    def pay(self,amount):

        print(
            f"UPI Payment {amount}"
        )



class CardPayment(
    PaymentStrategy
):


    def pay(self,amount):

        print(
            f"Card Payment {amount}"
        )
```

---

# Usage

```python
payment = UPIPayment()

payment.pay(5000)
```

Output:

```
UPI Payment 5000
```

---

# 12. Factory Pattern

---

# factories/product_factory.py

```python
from models.product import Product



class ProductFactory:


    @staticmethod
    def create_product(
        id,
        name,
        price,
        stock
    ):


        return Product(

            id,

            name,

            price,

            stock

        )
```

---

# 13. Order Builder

---

# builders/order_builder.py

```python
class OrderBuilder:


    def __init__(self):

        self.order={}



    def add_customer(
        self,
        customer
    ):

        self.order["customer"]=customer

        return self



    def add_items(
        self,
        items
    ):

        self.order["items"]=items

        return self



    def build(self):

        return self.order
```

---

# 14. Main Application

---

# main.py

```python
from factories.product_factory import ProductFactory

from models.cart import Cart

from strategies.payment_strategy import UPIPayment



product = ProductFactory.create_product(

    1,

    "Laptop",

    50000,

    10

)



cart = Cart()


cart.add_product(

    product,

    1

)



amount = cart.total_price()


print(amount)



payment = UPIPayment()


payment.pay(amount)
```

---

# Output

```
50000

UPI Payment 50000
```

---

# 15. Testing

## tests/test_cart.py

```python
import unittest

from models.cart import Cart

from models.product import Product



class TestCart(unittest.TestCase):


    def test_total(self):


        product = Product(

            1,

            "Mobile",

            10000,

            5

        )


        cart = Cart()


        cart.add_product(
            product,
            2
        )


        self.assertEqual(

            cart.total_price(),

            20000

        )


if __name__=="__main__":

    unittest.main()
```

---

# 16. Execution Flow

```
Customer

 |

Cart

 |

Order

 |

Payment Strategy

 |

Notification
```

---

# 17. Future Enhancements

Add:

```
Database

REST API

Inventory Sync

Recommendation Engine

Coupon Engine

Payment Gateway Integration

Microservices Architecture
```

---

# 18. Learning Outcome

After completing this project:

You understand:

✅ E-Commerce Domain Modeling

✅ SOLID Principles

✅ Strategy Pattern

✅ Factory Pattern

✅ Builder Pattern

✅ Observer Pattern

✅ Payment Framework Design

✅ Professional Python Architecture

---

# Project Completion Level

```
Python OOP              ⭐⭐⭐⭐⭐

Business Logic          ⭐⭐⭐⭐⭐

Design Patterns         ⭐⭐⭐⭐⭐

SOLID Design            ⭐⭐⭐⭐⭐

Real Application        ⭐⭐⭐⭐⭐
```

---

# Next Project

```
05_Hotel_Management_System.md
```

Focus:

- Room Booking
- Reservation System
- Customer Management
- Payment Handling
- Availability Engine
- State Management
