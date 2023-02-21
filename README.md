# richat
Тестовое задание для ООО Ришат

### Описание
Django-проект: реализован простой сервер с одной html-страницей, который общается со Stripe и создает платёжные формы для товаров. 
\
\
Структура проекта:
- Django Модель Item с полями (name, description, price)
- API с двумя методами:\
-- GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item.\
-- GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy.

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```
### Технологии
- Python 3.9.0
- Django 2.2.19
- Stripe= 5.2.0
- Python-dotenv

### Автор
Иван Голенко
