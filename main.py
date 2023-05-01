# main.py

from flask import Flask, jsonify
from repositories.xml_product_repository import XmlProductRepository
from services.product_service import ProductService

app = Flask(__name__)

product_repository = XmlProductRepository(file_path="products.xml")
product_service = ProductService(product_repository)

@app.route('/products')
def get_products():
    products = product_service.get_all_products()
    return jsonify([product.to_dict() for product in products])

if __name__ == '__main__':
    app.run()




# from repositories.xml_product_repository import XmlProductRepository
# from services.product_service import ProductService
#
# # Создаем экземпляр репозитория, указывая путь к XML-файлу
# product_repository = XmlProductRepository('products.xml')
#
# # Создаем экземпляр сервиса, передавая ему репозиторий
# product_service = ProductService(product_repository)
#
# # Получаем все продукты и выводим их на экран
# products = product_service.get_all_products()
# for product in products:
#     print(product.name)
