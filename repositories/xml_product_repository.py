from typing import List
from models.product import Product
from repositories.product_repository import ProductRepository
from lxml import etree


class XmlProductRepository(ProductRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _get_next_id(self, products: List[Product]) -> int:
        if len(products) == 0:
            return 1
        else:
            return max(product.id for product in products) + 1

    def get_all(self) -> List[Product]:
        with open(self.file_path, "rb") as f:
            xml = f.read()
            root = etree.fromstring(xml)

        products = []
        for product_xml in root.xpath("//product"):
            product_dict = {key: value for key, value in product_xml.attrib.items()}
            product = Product.from_dict(product_dict)

            products.append(product)

        return products

    def get_by_id(self, product_id: int) -> Product:
        with open(self.file_path, "rb") as f:
            xml = f.read()
            root = etree.fromstring(xml)

        product_xml = root.xpath(f"//product[@id='{product_id}']")[0]
        return Product.from_dict(product_xml.attrib)

    def add(self, product: Product) -> None:
        with open(self.file_path, "rb") as f:
            xml = f.read()
            root = etree.fromstring(xml)

        products = []
        for product_xml in root.xpath("//product"):
            product_dict = {key: value for key, value in product_xml.attrib.items()}
            product = Product.from_dict(product_dict)

            products.append(product)

        product.id = self._get_next_id(products)
        product_xml = etree.Element("product", product.to_dict())
        product_xml.set("id", str(product.id))
        root.append(product_xml)

        with open(self.file_path, "wb") as f:
            f.write(etree.tostring(root, pretty_print=True))

    def update(self, product: Product) -> None:
        with open(self.file_path, "rb") as f:
            xml = f.read()
            root = etree.fromstring(xml)

        product_xml = root.xpath(f"//product[@id='{product.id}']")[0]
        for attr, value in product.to_dict().items():
            product_xml.set(attr, str(value))

        with open(self.file_path, "wb") as f:
            f.write(etree.tostring(root, pretty_print=True))

    def delete(self, product_id: int) -> None:
        with open(self.file_path, "rb") as f:
            xml = f.read()
            root = etree.fromstring(xml)

        product_xml = root.xpath(f"//product[@id='{product_id}']")[0]
        root.remove(product_xml)

        with open(self.file_path, "wb") as f:
            f.write(etree.tostring(root, pretty_print=True))
