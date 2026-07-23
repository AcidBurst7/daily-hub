# 🚀 Daily Hub

Daily Hub — веб-приложение для управления задачами в формате Kanban.

Проект разработан на Django и предназначен для организации личных задач: создание досок, колонок и карточек задач, установка сроков выполнения и управление статусами.

Проект разворачивается с использованием Docker, PostgreSQL и Gunicorn.

---

## ✨ Возможности

### Пользователи

- Регистрация пользователей
- Авторизация
- Личный профиль
- Загрузка фотографии профиля
- Разграничение доступа к пользовательским данным


### Kanban-доски

- Создание нескольких досок
- Создание колонок внутри досок
- Создание задач
- Редактирование задач
- Удаление задач
- Цветовые метки
- Дедлайны
- Архивирование задач


---

# 🛠 Технологический стек

## Backend

- Python 3.12
- Django 5.2
- Django ORM
- Django Authentication
- PostgreSQL


## Frontend

- HTML5
- CSS3
- JavaScript
- Django Templates


## Инфраструктура

- Docker
- Docker Compose
- Gunicorn
- PostgreSQL


## Дополнительно

- Pillow
- django-environ
- Git


---

# 🏗 Архитектура проекта

Daily Hub

Browser

↓

Gunicorn

↓

Django

↓

PostgreSQL



В production окружении планируется:

Browser

↓

Nginx

↓

Gunicorn

↓

Django

↓

PostgreSQL




---

# 📂 Структура проекта

daily-hub/

├── applications/
│
│ ├── account/
│ │
│ └── tasks/
│
├── config/
│
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── static/
│
├── media/
│
├── templates/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md




---

# 🚀 Запуск проекта


## 1. Клонирование


```bash
git clone <repository_url>

cd daily-hub
```

## 2. Создание файла окружения. Создать файл .env:

DEBUG=True
SECRET_KEY=your_secret_key
DB_NAME=dailyhub
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=postgres
DB_PORT=5432

### Запуск через Docker

Собрать контейнеры:

```bash
docker compose up --build
```

После запуска приложение доступно: http://localhost:8000


### Миграции

Выполнить:

```bash
docker exec -it dailyhub_web python manage.py migrate
```

Создать администратора:
```bash
docker exec -it dailyhub_web python manage.py createsuperuser
```

## 📸 Скриншоты
Главная страница

Добавить изображение
Kanban-доска

Добавить изображение
Профиль пользователя

Добавить изображение

## 🗄 База данных

В проекте используется PostgreSQL. База данных запускается отдельным Docker-контейнером.

Django
 |
 |
PostgreSQL container


## 📌 План развития
Version 1.0

[x] Регистрация
[x] Авторизация
[x] Профиль пользователя
[x] Kanban-доски
[x] CRUD задач
[x] CRUD колонок
[x] PostgreSQL
[x] Docker

Version 1.1
[ ] Чек-листы
[ ] Поиск задач
[ ] Фильтрация
[ ] История изменений
[ ] Dashboard

Version 2.0
[ ] Nginx
[ ] HTTPS
[ ] CI/CD
[ ] Deploy на VPS


## 📚 Изученные технологии
В процессе разработки были изучены:
    Django ORM
    Models
    ForeignKey
    OneToOne relationships
    Class Based Views
    Function Based Views
    Authentication
    Django Templates
    Static and Media files
    PostgreSQL
    Docker
    Environment variables
    Gunicorn

## 🤝 Contribution
Если у вас есть идеи по улучшению проекта — создавайте Issue или Pull Request.

👩‍💻 Автор

Разработано с ❤️

Backend developer