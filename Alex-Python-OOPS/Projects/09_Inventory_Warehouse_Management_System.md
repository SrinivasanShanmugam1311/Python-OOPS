# Project 09 – Inventory Warehouse Management System

## File Name

```
09_Inventory_Warehouse_Management_System.md
```

---

# Level

```
Intermediate → Advanced
```

---

# Domain

```
Supply Chain / Warehouse Management Application
```

---

# Project Overview

A real-world inventory and warehouse management system developed using Python OOP principles.

The application manages:

- Products
- Categories
- Suppliers
- Warehouses
- Stock
- Purchase Orders
- Sales Orders
- Inventory Movement
- Reports

This project focuses on:

- Enterprise Data Modeling
- Repository Pattern
- Inventory Workflow
- SOLID Principles
- Design Patterns
- Business Rule Management

---

# 1. Project Objective

Build a scalable inventory management system using:

- Object-Oriented Programming
- Clean Architecture
- Design Patterns
- Database Ready Design
- Exception Handling
- Testing

---

# 2. Real World Problem

Large companies manage thousands of products.

The workflow:

```
Supplier

    |

Purchase Order

    |

Warehouse

    |

Inventory Stock

    |

Customer Order

    |

Stock Reduction
```

The system must handle:

- Stock availability
- Product movement
- Supplier management
- Order processing
- Inventory reports

---

# 3. Project Features

---

# Product Management

Features:

- Add Product
- Update Product
- Delete Product
- Search Product


Product:

```
Product ID

Name

Category

Price

Quantity
```

---

# Category Management

Example:

```
Electronics

Furniture

Food

Clothing

Books
```

---

# Supplier Management

Features:

- Add Supplier
- View Supplier
- Manage Orders


Supplier:

```
Supplier ID

Company Name

Contact

Products
```

---

# Warehouse Management

Features:

- Create Warehouse
- Store Products
- Track Capacity


Warehouse:

```
Warehouse ID

Location

Capacity

Inventory
```

---

# Inventory Management

Operations:

```
Stock In

Stock Out

Stock Transfer

Stock Adjustment
```

---

# Purchase Order

Workflow:

```
Create Order

     |

Supplier Approval

     |

Receive Products

     |

Update Stock
```

---

# Sales Order

Workflow:

```
Customer Order

      |

Check Stock

      |

Reserve Product

      |

Dispatch

      |

Reduce Inventory
```

---

# Reporting

Reports:

```
Stock Report

Low Inventory Report

Supplier Report

Sales Report
```

---

# 4. OOP Concepts Used

| Concept | Usage |
|-|-|
| Classes | Product, Warehouse, Order |
| Encapsulation | Stock control |
| Inheritance | Product types |
| Polymorphism | Pricing rules |
| Composition | Warehouse contains inventory |
| Association | Supplier-product |
| Abstract Classes | Inventory operations |
| Dataclass | Product records |
| Exceptions | Stock validation |

---

# 5. Object Relationships

---

# Warehouse → Inventory

Composition

```
Warehouse

 |

Inventory Items
```

---

# Category → Products

One-to-Many

```
Category

 |

 |---- Product

 |---- Product
```

---

# Supplier ↔ Product

Many-to-Many

```
Supplier

     |

 Supplier Product Mapping

     |

Product
```

---

# Order → Products

Many-to-Many

```
Order

 |

Order Items

 |

Products
```

---

# 6. Design Principles Used

---

# Single Responsibility Principle

Separate:

```
Product Service

Inventory Service

Order Service

Report Service
```

---

# Open Closed Principle

New inventory rules:

```
Expiry Based Product

Batch Product

Serialized Product
```

can be added without changing existing code.

---

# Liskov Substitution Principle

All product types should work with inventory.

---

# Dependency Inversion

Services depend on repositories.

---

# 7. Design Patterns Used

---

# Repository Pattern

Database abstraction:

```
Inventory Service

        |

Repository Interface

        |

Database
```

---

# Factory Pattern

Create products:

```
Product Factory

        |

------------------

Electronic Product

Food Product

Serialized Product
```

---

# Strategy Pattern

Pricing calculation:

```
Pricing Strategy

        |

------------------

Retail Price

Wholesale Price

Discount Price
```

---

# Observer Pattern

Stock alerts:

```
Stock Low

    |

Notification

    |

Manager
```

---

# Command Pattern

Inventory actions:

```
Add Stock Command

Remove Stock Command

Transfer Command
```

---

# 8. Project Folder Structure

```
09_Inventory_Warehouse_Management_System/

│
├── main.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── models/
│   ├── __init__.py
│   ├── product.py
│   ├── category.py
│   ├── supplier.py
│   ├── warehouse.py
│   ├── inventory.py
│   ├── order.py
│   ├── order_item.py
│   └── stock_transaction.py
│
├── services/
│   ├── __init__.py
│   ├── product_service.py
│   ├── inventory_service.py
│   ├── order_service.py
│   └── report_service.py
│
├── repositories/
│   ├── repository.py
│   ├── product_repository.py
│   └── inventory_repository.py
│
├── factories/
│   └── product_factory.py
│
├── strategies/
│   └── pricing_strategy.py
│
├── commands/
│   ├── command.py
│   ├── add_stock.py
│   └── remove_stock.py
│
├── observers/
│   └── stock_notification.py
│
├── exceptions/
│   └── inventory_exception.py
│
├── utils/
│   ├── logger.py
│   └── validator.py
│
├── database/
│   └── inventory.json
│
├── tests/
│   ├── test_product.py
│   ├── test_inventory.py
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
| product.py | Product entity |
| category.py | Product grouping |
| supplier.py | Supplier details |
| warehouse.py | Warehouse management |
| inventory.py | Stock control |
| order.py | Customer orders |
| repositories | Data access layer |
| services | Business logic |
| strategies | Dynamic rules |
| commands | Inventory operations |

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

    quantity:int



    def increase_stock(
        self,
        amount
    ):

        self.quantity += amount



    def decrease_stock(
        self,
        amount
    ):


        if amount > self.quantity:

            raise Exception(
                "Insufficient Stock"
            )


        self.quantity -= amount
```

---

# Concepts Used

Encapsulation:

```
Stock updated only through methods
```

---

# 11. Warehouse Model

```python
class Warehouse:


    def __init__(
        self,
        id,
        location
    ):

        self.id=id

        self.location=location

        self.products=[]



    def add_product(
        self,
        product
    ):

        self.products.append(
            product
        )
```

---

# 12. Inventory Service

```python
class InventoryService:


    def stock_in(
        self,
        product,
        quantity
    ):


        product.increase_stock(
            quantity
        )



    def stock_out(
        self,
        product,
        quantity
    ):


        product.decrease_stock(
            quantity
        )
```

---

# 13. Repository Pattern

## repositories/repository.py

```python
from abc import ABC,abstractmethod



class Repository(ABC):


    @abstractmethod
    def save(self,data):

        pass


    @abstractmethod
    def find(self,id):

        pass
```

---

# Product Repository

```python
class ProductRepository:


    def __init__(self):

        self.products={}



    def save(
        self,
        product
    ):

        self.products[
            product.id
        ] = product



    def find(
        self,
        id
    ):

        return self.products.get(id)
```

---

# 14. Product Factory

```python
class ProductFactory:


    @staticmethod
    def create(
        product_type,
        id,
        name,
        price
    ):


        return Product(

            id,

            name,

            price,

            0

        )
```

---

# 15. Pricing Strategy

```python
from abc import ABC,abstractmethod



class PricingStrategy(ABC):


    @abstractmethod
    def price(
        self,
        product
    ):

        pass



class WholesalePricing(
    PricingStrategy
):


    def price(
        self,
        product
    ):

        return product.price * 0.8
```

---

# 16. Main Application

```python
from models.product import Product

from models.warehouse import Warehouse

from services.inventory_service import InventoryService



product = Product(

    1,

    "Laptop",

    50000,

    10

)



warehouse = Warehouse(

    101,

    "Hyderabad"

)



warehouse.add_product(
    product
)



service = InventoryService()


service.stock_out(

    product,

    2

)



print(
    product.quantity
)
```

---

# Output

```
8
```

---

# 17. Testing

## tests/test_inventory.py

```python
import unittest

from models.product import Product



class TestInventory(unittest.TestCase):


    def test_stock_update(self):


        product = Product(

            1,

            "Mobile",

            20000,

            5

        )


        product.increase_stock(5)


        self.assertEqual(

            product.quantity,

            10

        )


if __name__=="__main__":

    unittest.main()
```

---

# 18. Execution Flow

```
Supplier

 |

Purchase Order

 |

Warehouse

 |

Inventory Service

 |

Stock Update

 |

Customer Order

 |

Report
```

---

# 19. Future Enhancements

Add:

```
Barcode Scanner

RFID Integration

AI Demand Prediction

Cloud Inventory

Mobile App

Multi Warehouse Support

ERP Integration
```

---

# 20. Learning Outcome

After completing this project:

You understand:

✅ Enterprise Inventory Design

✅ Repository Pattern

✅ Business Rules

✅ Stock Management

✅ SOLID Principles

✅ Design Patterns

✅ Supply Chain Architecture

---

# Project Completion Level

```
Python OOP              ⭐⭐⭐⭐⭐

Architecture            ⭐⭐⭐⭐⭐

SOLID Principles        ⭐⭐⭐⭐⭐

Design Patterns         ⭐⭐⭐⭐⭐

Business Complexity     ⭐⭐⭐⭐⭐
```

---

# Next Project

```
10_Real_World_Application_Architecture.md
```

Focus:

- Production Project Structure
- Configuration
- Logging
- Testing
- Deployment Ready Architecture
```
