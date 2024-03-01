# developer_website
Этот проект представляет портфолио разработчика, в котором представлены его профессиональные навыки, проекты и достижения. Портфолио разработчика предназначено для демонстрации его опыта и компетенций потенциальным работодателям или заказчикам.



## Установка и запуск

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com/JonyMalikov/developer_website

cd developer_website
```

- Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv

source venv/bin/activate
```

- Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

- Выполнить миграции:

```
python3 manage.py migrate
```

- Запустить проект:

```
python manage.py runserver
```


## Используемые технологии
+ [Python](https://www.python.org/) - язык программирования, на котором написан проект.
+ [Django](https://www.djangoproject.com/) - фреймворк для разработки веб-приложений на языке Python.
+ [Django](https://www.django-rest-framework.org/) Rest Framework - надстройка над Django, облегчающая разработку RESTful API.


## Авторы
+ **Евгений Маликов** [JonyMalikov](https://github.com/JonyMalikov)