# Project 09 – Inventory & Warehouse Management System

**Level:** Intermediate → Advanced  
**Domain:** Supply Chain, Logistics, Inventory / Backend Systems  
**Type:** In-memory Python OOPS simulation (no external packages)

## 1. Project Overview
Manage products, multiple warehouses, stock receipts, dispatches, warehouse transfers, movement history, low-stock reporting and stock valuation.

## 2. Objectives
Learn classes and objects, encapsulation, abstraction, inheritance, polymorphism, composition, dataclasses, custom exceptions, service layers, package structure and unit testing.

## 3. Project Structure
```text
09_Inventory_Warehouse_Management_System/
├── main.py
├── models/
│   ├── __init__.py
│   ├── product.py
│   ├── warehouse.py
│   ├── movement.py
│   └── alert.py
├── services/
│   ├── __init__.py
│   └── inventory_service.py
├── exceptions/
│   ├── __init__.py
│   └── inventory_exceptions.py
├── tests/
│   ├── __init__.py
│   └── test_inventory.py
├── requirements.txt
└── README.md
```

## 4. Application Architecture
```text
main.py (demonstration)
    |
    v
InventoryService (business operations)
    |---- Product (SKU, name, price)
    |---- Warehouse (stock per product)
    |---- StockMovement (history)
    `---- StockAlert (abstract base class)
             |---- ConsoleAlert
             `---- EmailAlert (simulated)
```

## 5. Models
- `Product`: identifies a product using an ID and unique SKU.
- `Warehouse`: stores a private dictionary of stock quantities. `receive()` adds; `dispatch()` removes; `quantity_of()` reads.
- `StockMovement`: immutable record of a stock receipt, dispatch or transfer.
- `StockAlert`: defines the `notify()` interface.
- `ConsoleAlert` and `EmailAlert`: two implementations of `notify()`.

## 6. Inventory Workflow
```text
Create Product + Two Warehouses
          |
Receive 10 Laptops in Bengaluru
          |
Transfer 3 Laptops to Mysuru
          |
Dispatch 1 Laptop from Mysuru
          |
Bengaluru = 7, Mysuru = 2, Total = 9
          |
Read Movement History + Inventory Value
```

## 7. OOPS Concepts
| Concept | Example |
|---|---|
| Class/Object | `Warehouse`, `Product` |
| Encapsulation | `Warehouse.__stock`, `quantity_of()` |
| Abstraction | `StockAlert(ABC)` |
| Inheritance | `EmailAlert(StockAlert)` |
| Polymorphism | Different `notify()` implementations |
| Composition | Service holds warehouse/product objects |
| Dataclass | `Product`, `StockMovement` |
| Service layer | `InventoryService` |
| Custom exceptions | `InsufficientStockError`, `ProductNotFoundError` |

## 8. Main Service Methods
`create_product()`, `create_warehouse()`, `receive_stock()`, `dispatch_stock()`, `transfer_stock()`, `get_quantity()`, `total_quantity()`, `low_stock_report()`, `inventory_value()`.

## 9. Validation and Corner Cases
- Quantity must be positive for receipts, dispatches and transfers.
- Cannot dispatch or transfer more stock than available.
- Cannot transfer between the same warehouse.
- Warehouse and product IDs must exist.
- SKU must be unique.
- Invalid operations do not create stock movement records.

## 10. Run
From the project folder:
```bash
python main.py
python -m unittest discover -v
```

## 11. Sample Output
```text
INVENTORY & WAREHOUSE OOPS SIMULATION
Bengaluru stock: 7
Mysuru stock: 2
Total stock: 9
Bengaluru stock value: INR 350000.00
Recorded movements: 3
CONSOLE ALERT: Review low stock when needed
```

## 12. Unit Tests
Tests cover stock receipt, dispatch, transfer, validation, stock totals, low-stock reports, valuation, data encapsulation, alert polymorphism and movement history.

## 13. Current Limitations
- Data lives in memory and disappears when the program exits.
- No database, barcode scanner, authentication, REST API or real email integration.
- No concurrent transaction handling or atomic rollback for unexpected runtime failures.
- No purchase-order, supplier or shipment workflows yet.
- Not production-ready; intended to teach OOPS and application structure.

## 14. Future Enhancements
SQLite/PostgreSQL, FastAPI, purchase orders, supplier management, barcode scanning, reservations, inventory adjustments, stock audits, real alerts, role-based access, database transactions and integration tests.

## 15. Learning Progression
```text
Class -> Object -> Encapsulation -> Inheritance -> Polymorphism
 -> Abstraction -> Composition -> Dataclasses -> Service Layer
 -> Exceptions -> Unit Tests -> Application Architecture
```

## 16. Project Completion Checklist
- [x] Multiple Python modules
- [x] Product and warehouse models
- [x] Receive, dispatch, transfer
- [x] Movement history
- [x] Stock valuation and low-stock report
- [x] Custom exceptions
- [x] Abstract alert and child classes
- [x] Unit tests
- [x] Runnable main.py
- [ ] Database and APIs (future work)
