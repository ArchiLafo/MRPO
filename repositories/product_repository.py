from abc import ABC, abstractmethod
from typing import List
from models.product import Product

class ProductRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def add(self, product: Product) -> None:
        pass

    @abstractmethod
    def update(self, product: Product) -> None:
        pass
