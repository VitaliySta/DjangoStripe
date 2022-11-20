# Тестовое задание Django + Stripe API 

### Используемые технологии
- Django
- Django Rest Framework
- Docker
- Docker-compose
- Stripe

### Подготовка
**Обязательно** - регистрация на сайте - [https://stripe.com](https://stripe.com)  
- Клонировать проект с помощью git clone или скачать ZIP-архив:  
``` git clone <название репозитория> ```
- Перейти в папку TaskStrip и создать файл .env со следущим содержимым:
```
SECRET_KEY=<любой набор символов>
STRIPE_PUBLIC_KEY=<Ваш Publishable key с сайта stripe.com>
STRIPE_SECRET_KEY=<Ваш Secret key с сайта stripe.com>
```
Для получения Publishable key и Secret key зайдите на сайт stripe.com и авторизуетесь.
В верхнем правом углу нажмите *Developers*, затем слева нажмите *API keys*.

### Запуск проекта если установлен Docker  
- Запустите docker-compose:   
``` docker compose up ```  
- Не закрывая первую консоль, открыть вторую и в ней выполнить:
  - Создайте миграции:    
  ``` docker-compose exec web python manage.py makemigrations ```
  - Примените миграции   
  ``` docker-compose exec web python manage.py migrate ```
  - Загрузить подготовленный список предметов  
  ``` docker-compose exec web python manage.py loaddata items.json ```

### Запуск проекта если Docker не установлен
- Установите виртуальное окружение:  
``` python -m venv venv ```  
- Активируйте виртуальное окружение:     
``` source venv/Scripts/activate ``` 
- Установите зависимости из файла requirements.txt:   
``` pip install -r requirements.txt ```
- Создайте миграции:    
``` python manage.py makemigrations ```
- Примените миграции:   
``` python manage.py migrate ```
- Загрузите тестовые данные:  
``` python manage.py loaddata items.json ```
- Выполните команду:   
``` python manage.py runserver ``` 

#### Доступ в админку
- Если вы загрузили тестовые данные:
  - Перейдите по адресу:        
    ``` GET /admin/ ``` 
  - Логин и пароль - admin
- Если не загружали тестовые данные:
  - Создаете суперпользователя Django:  
    - если установлен Docker  
    ``` docker-compose exec web python manage.py createsuperuser ```
    - если Docker не установлен  
    ``` python manage.py createsuperuser ```

#### Примеры некоторых запросов API:
Получение Stripe Session Id:  
``` GET /buy/1/ ```  
Получение данных своей учетной записи:  
``` GET /item/3/ ```  

Форму для отправки тестового платежа можно заполнять любыми данными, кроме номера карты.
Используйте следующие номера карт для тестирования:
- 4242 4242 4242 4242
- 4000 0000 0000 3220
- 4000 0000 0000 9995


#### Автор:
Стацюк Виталий - [https://github.com/VitaliySta](https://github.com/VitaliySta)
