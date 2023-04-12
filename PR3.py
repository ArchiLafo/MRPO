import uuid
import unittest

class Order:
    def __init__(self, customer_name, total_price, shipping_address):
        self.id = str(uuid.uuid4())
        self.customer_name = customer_name
        self.total_price = total_price
        self.shipping_address = shipping_address

class Warehouse:
    def __init__(self, name, location):
        self.id = str(uuid.uuid4())
        self.name = name
        self.location = location

class OrderRepository:
    def __init__(self):
        self.orders = {}

    def save(self, order):
        self.orders[order.id] = order

    def get(self, order_id):
        return self.orders.get(order_id)

class WarehouseRepository:
    def __init__(self):
        self.warehouses = {}

    def save(self, warehouse):
        self.warehouses[warehouse.id] = warehouse

    def get(self, warehouse_id):
        return self.warehouses.get(warehouse_id)

class TestOrder(unittest.TestCase):
    def test_create_order(self):
        order = Order("John Smith", 1000, "New York")
        self.assertIsNotNone(order.id)
        self.assertIsInstance(order.id, str)
        self.assertEqual(len(order.id), 36)


class TestWarehouse(unittest.TestCase):
    def test_create_warehouse(self):
        warehouse = Warehouse("Warehouse 1", "Chicago")
        self.assertIsNotNone(warehouse.id)
        self.assertEqual(warehouse.name, "Warehouse 1")
        self.assertEqual(warehouse.location, "Chicago")

class TestOrderRepository(unittest.TestCase):
    def test_save_and_get_order(self):
        repository = OrderRepository()
        order = Order("John Smith", 1000, "New York")
        repository.save(order)

        saved_order = repository.get(order.id)
        self.assertEqual(saved_order, order)

    def test_get_nonexistent_order(self):
        repository = OrderRepository()

        nonexistent_order = repository.get(str(uuid.uuid4()))
        self.assertIsNone(nonexistent_order)
class TestWarehouseRepository(unittest.TestCase):
    def test_save_and_get_warehouse(self):
        repository = WarehouseRepository()
        warehouse = Warehouse("Warehouse 1", "Chicago")
        repository.save(warehouse)

        saved_warehouse = repository.get(warehouse.id)
        self.assertEqual(saved_warehouse, warehouse)

    def test_get_nonexistent_warehouse(self):
        repository = WarehouseRepository()

        nonexistent_warehouse = repository.get(str(uuid.uuid4()))
        self.assertIsNone(nonexistent_warehouse)



if __name__ == "__main__":
    unittest.main()
