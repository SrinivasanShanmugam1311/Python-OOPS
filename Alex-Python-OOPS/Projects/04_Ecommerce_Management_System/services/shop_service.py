from datetime import datetime
from decimal import Decimal
from models.customer import Customer
from models.product import Product
from models.cart import Cart
from models.order import Order,OrderLine
from exceptions.errors import NotFoundError,InsufficientStockError,EmptyCartError,InvalidOrderStateError
class ShopService:
    # Service layer coordinates models; each model owns its own rules.
    def __init__(self):
        self.customers={}; self.products={}; self.carts={}; self.orders={}
    def create_customer(self,name,email):
        customer=Customer(len(self.customers)+1,name,email)
        self.customers[customer.customer_id]=customer
        return customer
    def add_product(self,name,price,stock):
        price=Decimal(str(price))
        if price < 0 or stock < 0: raise ValueError('Price/stock cannot be negative')
        product=Product(len(self.products)+1,name,price,stock)
        self.products[product.product_id]=product
        return product
    def add_to_cart(self,customer_id,product_id,quantity):
        if customer_id not in self.customers or product_id not in self.products:
            raise NotFoundError('Customer or product not found')
        cart=self.carts.setdefault(customer_id,Cart(customer_id))
        cart.add_item(product_id,quantity)
        return cart
    def checkout(self,customer_id,payment_method):
        if customer_id not in self.customers: raise NotFoundError('Customer not found')
        cart=self.carts.get(customer_id)
        if not cart or not cart.items: raise EmptyCartError('Cart is empty')
        # Check ALL items before changing stock.
        for pid,quantity in cart.items.items():
            if quantity > self.products[pid].stock: raise InsufficientStockError('Not enough stock')
        lines=[OrderLine(pid,self.products[pid].name,q,self.products[pid].price) for pid,q in cart.items.items()]
        total=sum((line.unit_price*line.quantity for line in lines),Decimal('0'))
        # Simulation only: no real payment gateway.
        payment_reference=payment_method.pay(total)
        for line in lines: self.products[line.product_id].reserve(line.quantity)
        order=Order(len(self.orders)+1,customer_id,lines,total,payment_reference,datetime.now())
        self.orders[order.order_id]=order
        cart.clear()
        return order
    def cancel_order(self,order_id):
        if order_id not in self.orders: raise NotFoundError('Order not found')
        order=self.orders[order_id]
        if order.status != 'PAID': raise InvalidOrderStateError('Order already cancelled')
        for line in order.lines: self.products[line.product_id].restock(line.quantity)
        order.status='CANCELLED'
        # Refund integration intentionally not included.
        return order
