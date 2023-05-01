 Мы создали простое Flask-приложение, которое предоставляет API для получения списка товаров. Для этого мы использовали модели данных, сервисы и репозитории, которые позволяют нам разделить логику на отдельные компоненты и упростить поддержку приложения в будущем.


### Описание приложения

Наше приложение представляет собой Flask-приложение, которое предоставляет API для получения списка товаров. Для упрощения поддержки приложения мы разделили логику на следующие компоненты:

- Модели данных, которые описывают объекты, с которыми мы работаем в нашем приложении.
- Сервисы, которые содержат бизнес-логику нашего приложения.
- Репозитории, которые предоставляют доступ к данным нашего приложения.


### API

Наше приложение предоставляет следующие API:

#### Получение списка товаров

Метод: GET

Путь: /products

Возвращаемые данные: список товаров в формате JSON.

### Теория

Мы использовали подход MVC (Model-View-Controller) для разделения логики нашего приложения на отдельные компоненты. Этот подход позволяет упростить поддержку приложения в будущем, так как каждый компонент содержит только свою логику и не зависит от других компонентов.

Модели данных описывают объекты, с которыми мы работаем в нашем приложении. Они могут содержать поля и методы, которые позволяют нам управлять этими объектами.

Сервисы содержат бизнес-логику нашего приложения. Они могут вызывать методы моделей данных и репозиториев для получения и обработки данных.

Репозитории предоставляют доступ к данным нашего приложения. Они могут использовать базы данных или файлы для хранения данных и предоставлять методы для получения и изменения этих данных.

В нашем проекте мы использовали XML файлы для хранения информации о продуктах, и создали репозиторий XmlProductRepository, который отвечает за получение и сохранение данных из этих файлов.

Кроме того, мы создали сервисы для управления данными нашего приложения. Сервисы используют репозитории для доступа к данным и предоставляют удобный интерфейс для работы с этими данными. В нашем проекте мы создали ProductService, который предоставляет методы для получения и изменения информации о продуктах.

Наконец, мы создали эндпойнты нашего веб-приложения, которые используют сервисы для получения и изменения данных, и возвращают эти данные в формате JSON.

