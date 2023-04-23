from abc import ABC, abstractmethod
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import List

Base = declarative_base()
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

class IRepository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def delete(self, obj):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass

class ProductRepository(IRepository):
    def __init__(self, session):
        self.session = session

    def add(self, product: Product):
        self.session.add(product)
        self.session.commit()

    def delete(self, product: Product):
        self.session.delete(product)
        self.session.commit()

    def update(self, product: Product):
        self.session.merge(product)
        self.session.commit()

    def get(self, id: int) -> Product:
        return self.session.query(Product).get(id)

    def get_all(self) -> List[Product]:
        return self.session.query(Product).all()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()
    product_repository = ProductRepository(session)
    product1 = Product(name='Laptop', description='Acer Predator', price=1000.0, quantity=10)
    product_repository.add(product1)
    session.close()
