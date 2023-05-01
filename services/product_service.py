from typing import List
from models.product import Product
from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_all_products(self) -> List[Product]:
        return self.product_repository.get_all()

    def get_product_by_id(self, product_id: int) -> Product:
        return self.product_repository.get_by_id(product_id)

    def add_product(self, product: Product) -> None:
        self.product_repository.add(product)

    def update_product(self, product: Product) -> None:
        self.product_repository.update(product)
