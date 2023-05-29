import asyncio
import json
import xml.etree.ElementTree as ET

# Класс товара
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return {"name": self.name, "price": self.price}

# Базовый класс для всех репозиториев
class Repository:
    def save(self, data):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError

# Репозиторий для реляционного хранения
class RelationalRepository(Repository):
    def save(self, data):
        print("Сохранение в реляционной базе данных:", data)

    def load(self):
        print("Загрузка из реляционной базы данных")

# Репозиторий для хранения в формате XML
class XMLRepository(Repository):
    def save(self, data):
        root = ET.Element("products")
        for item in data:
            product_elem = ET.SubElement(root, "product")
            name_elem = ET.SubElement(product_elem, "name")
            name_elem.text = item["name"]
            price_elem = ET.SubElement(product_elem, "price")
            price_elem.text = str(item["price"])

        tree = ET.ElementTree(root)
        tree.write("products.xml")

        print("Сохранение в XML:", data)

    def load(self):
        tree = ET.parse("products.xml")
        root = tree.getroot()

        products = []
        for product_elem in root.findall("product"):
            name_elem = product_elem.find("name")
            price_elem = product_elem.find("price")
            product = Product(name_elem.text, float(price_elem.text))
            products.append(product)

        print("Загрузка из XML")
        return products

# Репозиторий для хранения в формате JSON
class JSONRepository(Repository):
    def save(self, data):
        with open("products.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Сохранение в JSON:", data)

    def load(self):
        with open("products.json", "r") as file:
            data = json.load(file)

        products = []
        for item in data:
            product = Product(item["name"], item["price"])
            products.append(product)

        print("Загрузка из JSON")
        return products

# Фабрика репозиториев
class RepositoryFactory:
    @staticmethod
    def create_repository(storage_type):
        if storage_type == 'relational':
            return RelationalRepository()
        elif storage_type == 'xml':
            return XMLRepository()
        elif storage_type == 'json':
            return JSONRepository()
        else:
            raise ValueError("Неподдерживаемый тип хранилища")

# Класс для оформления заказа
class Order:
    def __init__(self, repository):
        self.repository = repository
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def display_order(self):
        print("Текущий заказ:")
        for product in self.products:
            print(f"Название: {product.name}, Цена: {product.price}")

    async def process_order(self):
        print("Оформление заказа")
        await asyncio.sleep(1)
        self.repository.save([product.to_dict() for product in self.products])
        print("Заказ оформлен")

# Тесты фабрики репозиториев
def test_repository_factory():
    factory = RepositoryFactory()

    # Создание репозитория с реляционным хранением
    repository_relational = factory.create_repository('relational')
    assert isinstance(repository_relational, RelationalRepository)

    # Создание репозитория с хранением в формате XML
    repository_xml = factory.create_repository('xml')
    assert isinstance(repository_xml, XMLRepository)

    # Создание репозитория с хранением в формате JSON
    repository_json = factory.create_repository('json')
    assert isinstance(repository_json, JSONRepository)

    print("Тесты фабрики репозиториев пройдены успешно")

# Тесты корутинов
async def test_coroutines(storage_type):
    factory = RepositoryFactory()
    repository = factory.create_repository(storage_type)
    order = Order(repository)

    product1 = Product("Телефон", 1000)
    product2 = Product("Ноутбук", 2000)
    order.add_product(product1)
    order.add_product(product2)

    order.display_order()

    await order.process_order()

    loaded_products = repository.load()
    for product in loaded_products:
        print(f"Загруженный товар: {product.name}, {product.price}")

    print("Тесты корутинов пройдены успешно")

# Выполнение тестов
test_repository_factory()
storage_type = input("Введите тип хранилища (relational, xml, json): ")
asyncio.run(test_coroutines(storage_type))
