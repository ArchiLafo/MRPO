# # models/product.py
#
# class Product:
#     def __init__(self, id: int, name: str, price: float, description: str):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.description = description
#
#     def __str__(self):
#         return f"Product {self.name} (id: {self.id}) - ${self.price}"
#     # @classmethod
#     # def from_dict(cls, adict):
#     #     return cls(adict["name"], adict["price"], adict["description"])
#
#     @classmethod
#     def from_dict(cls, adict):
#         return cls(**adict)
# models/product.py

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    @classmethod
    def from_dict(cls, dict):
        return cls(**dict)

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

