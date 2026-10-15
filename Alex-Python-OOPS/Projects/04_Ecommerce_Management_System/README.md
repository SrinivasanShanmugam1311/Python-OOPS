# Project 04 – E-commerce Management System

**Level:** Intermediate → Advanced  
**Domain:** Online Shopping / Backend Application  
**Type:** Runnable, in-memory Python OOPS learning simulation

## 1. Project Overview

The system manages customers, products, shopping carts, orders, simulated payments, stock, and cancellations. **No real payments are processed.**

## 2. Objectives

Learn classes, objects, encapsulation, abstraction, inheritance, polymorphism, composition, dataclasses, packages, service layers, custom exceptions, and unit tests.

## 3. Project Structure

```text
04_Ecommerce_Management_System/
├── main.py
├── models/
│   ├── customer.py
│   ├── product.py
│   ├── cart.py
│   ├── payment.py
│   └── order.py
├── services/shop_service.py
├── exceptions/errors.py
├── tests/test_shop.py
├── requirements.txt
└── README.md
```

Each package also contains `__init__.py`.

## 4. Architecture

```text
User -> main.py -> ShopService
                     |-- Customer (buyer)
                     |-- Product (name, price, stock)
                     |-- Cart (product IDs and quantities)
                     |-- PaymentMethod (abstract base)
                     |      |-- UPIPayment
                     |      `-- CardPayment
                     `-- Order -> OrderLine(s)
```

## 5. Models

| Model | Main data | Responsibility |
|---|---|---|
| Customer | ID, name, email | Buyer details |
| Product | ID, name, price, stock | Control stock |
| Cart | customer ID, items | Collect purchases |
| PaymentMethod | abstract pay() | Payment interface |
| OrderLine | product, quantity, price | Immutable purchase snapshot |
| Order | customer, lines, total, status | Completed purchase |

## 6. OOPS Concepts

- **Encapsulation:** `Product.reserve()` and `Product.restock()` control stock changes.
- **Abstraction:** `PaymentMethod` defines `pay()` without specifying how.
- **Inheritance:** `UPIPayment` and `CardPayment` inherit from `PaymentMethod`.
- **Polymorphism:** `payment_method.pay(total)` works for either method.
- **Composition:** An `Order` HAS-A list of `OrderLine` objects.
- **Dataclass:** Customer, Product, Cart, Order, and OrderLine.
- **Service layer:** `ShopService` coordinates the checkout workflow.

## 7. Checkout Simulation

```text
Create customer -> Add products -> Add to cart
   -> Check stock -> Calculate total -> Simulate payment
   -> Reduce stock -> Create order -> Clear cart
```

**Example:** Laptop ₹49,999 + 2 mice × ₹599 = **₹51,197**.

## 8. Service Operations

`create_customer()`, `add_product()`, `add_to_cart()`, `checkout()`, `cancel_order()`.

## 9. Exceptions

`ShopError` is the base exception. Specific errors include `NotFoundError`, `InvalidQuantityError`, `InsufficientStockError`, `EmptyCartError`, and `InvalidOrderStateError`.

## 10. Run the Project

Requires Python 3.10+. From this directory:

```bash
python main.py
python -m unittest discover -v
```

## 11. Testing

Tests cover checkout totals, inventory changes, insufficient stock, empty carts, invalid quantities, cancellation, and payment polymorphism.

## 12. Limitations

- In-memory only; all data disappears on exit.
- Payments are simulated, not real.
- Cancellation restores stock but does **not** perform refunds.
- No database, authentication, REST API, shipping, or tax handling.
- Not concurrency-safe or production-ready. Real systems require atomic inventory updates, idempotent payment processing, and durable storage.

## 13. Future Enhancements

Add SQLite/PostgreSQL, FastAPI, authentication, discounts, taxes, shipping, real payment integration, concurrency-safe inventory reservation, refunds, integration tests, and deployment.

## 14. Learning Progression

```text
Classes -> Objects -> Encapsulation -> Inheritance
-> Polymorphism -> Abstraction -> Composition
-> Service Layer -> Exceptions -> Unit Tests -> Backend Architecture
```

## 15. Completion Checklist

- [x] Models and service layer
- [x] Cart and checkout
- [x] Simulated payment and order
- [x] Stock tracking and cancellation
- [x] Custom exceptions
- [x] Unit tests and README
- [ ] Database, API, real payment integration (future work)
