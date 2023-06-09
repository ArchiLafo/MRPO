# 
Данный код реализует систему управления заказами и складами.

Основные классы:

Order: класс, представляющий заказ. Содержит информацию о клиенте, заказанных продуктах, общей стоимости заказа и идентификатор заказа.
Product: класс, представляющий товар. Содержит информацию об идентификаторе товара, названии, описании, цене и доступном количестве.
Customer: класс, представляющий клиента. Содержит информацию об идентификаторе клиента, имени и адресе электронной почты.
Warehouse: класс, представляющий склад. Содержит информацию об идентификаторе склада, названии и местоположении.
OrderRepository: класс, представляющий репозиторий заказов. Он сохраняет заказы и предоставляет доступ к сохраненным заказам по их идентификаторам.
WarehouseRepository: класс, представляющий репозиторий складов. Он сохраняет склады и предоставляет доступ к сохраненным складам по их идентификаторам.
Тесты:

TestOrder: содержит тесты для класса Order.
TestWarehouse: содержит тесты для класса Warehouse.
TestOrderRepository: содержит тесты для класса OrderRepository.
TestWarehouseRepository: содержит тесты для класса WarehouseRepository.
В функции main пользователь может создавать экземпляры классов Order и Warehouse, сохранять их в соответствующие репозитории и затем получать их по идентификаторам.

В качестве бизнес-правил для нашей предметной области были выбраны:
1.Заказы должны обрабатываться в течение 24 часов со дня получения заказа, чтобы обеспечить быструю доставку продукта.
2.Цены на продукты должны быть оптимальными и соответствовать среднему уровню рынка. Также магазин должен регулярно проводить скидочные акции и предлагать специальные предложения, чтобы поддерживать конкурентоспособность и привлекать новых покупателей.
3.Магазин должен убедиться, что все продукты соответствуют требованиям безопасности и качества, а гарантийный период должен быть приемлемым и устраивать клиентов.
4.Интернет-магазин должен предоставлять простой и безопасный способ оплаты, а также обеспечивать удобную систему доставки, которая позволяет клиентам получать товары в удобное время и место.
5.Магазин должен регулярно обновлять свой ассортимент и предлагать новинки, чтобы следовать тенденциям и предлагать актуальные продукты. Идеальное соотношение между широким выбором товаров и высоким качеством обслуживания – важнейшее условие успеха.
6.Клиентское обслуживание должно быть максимально качественным и ответственным, решение вопросов и проблем клиентов должно осуществляться оперативно и эффективно, чтобы обеспечить наилучший опыт покупок и удовлетворение клиентов. 
![image](https://user-images.githubusercontent.com/103525441/230876178-463e4971-32c1-4c9a-9c15-7516751a6609.png)

