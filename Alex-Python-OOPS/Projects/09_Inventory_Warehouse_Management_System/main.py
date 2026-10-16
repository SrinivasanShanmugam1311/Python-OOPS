from services.inventory_service import InventoryService
from models.alert import ConsoleAlert

def main():
    service = InventoryService()
    laptop = service.create_product('LAP-001', 'Laptop', '50000.00')
    bengaluru = service.create_warehouse('Bengaluru')
    mysuru = service.create_warehouse('Mysuru')
    service.receive_stock(bengaluru.warehouse_id, laptop.product_id, 10)
    service.transfer_stock(bengaluru.warehouse_id, mysuru.warehouse_id, laptop.product_id, 3)
    service.dispatch_stock(mysuru.warehouse_id, laptop.product_id, 1)
    print('INVENTORY & WAREHOUSE OOPS SIMULATION')
    print('Bengaluru stock:', service.get_quantity(bengaluru.warehouse_id, laptop.product_id))
    print('Mysuru stock:', service.get_quantity(mysuru.warehouse_id, laptop.product_id))
    print('Total stock:', service.total_quantity(laptop.product_id))
    print('Bengaluru stock value: INR', service.inventory_value(bengaluru.warehouse_id))
    print('Recorded movements:', len(service.movements))
    print(ConsoleAlert().notify('Review low stock when needed'))
if __name__ == '__main__': main()
