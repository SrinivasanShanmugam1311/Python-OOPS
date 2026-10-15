from services.shop_service import ShopService
from models.payment import UPIPayment

def main():
    shop=ShopService()
    customer=shop.create_customer('Alex','alex@example.com')
    laptop=shop.add_product('Laptop','49999',5)
    mouse=shop.add_product('Mouse','599',10)
    shop.add_to_cart(customer.customer_id,laptop.product_id,1)
    shop.add_to_cart(customer.customer_id,mouse.product_id,2)
    order=shop.checkout(customer.customer_id,UPIPayment())
    print('E-COMMERCE OOPS SIMULATION')
    print('Customer:',customer.name)
    print('Order:',order.order_id,'Total: INR',order.total)
    print('Status:',order.status)
    print('Payment:',order.payment_reference)
    print('Remaining laptop stock:',laptop.stock)

if __name__ == '__main__': main()
