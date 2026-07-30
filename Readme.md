# 🚀 Daily Hub

> Kanban-приложение для управления личными задачами, разработанное на Django.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📖 О проекте

Daily Hub — веб-приложение для организации задач по методологии Kanban.

Каждый пользователь может создавать несколько досок, добавлять колонки и задачи, устанавливать сроки выполнения и управлять личным пространством.

Проект создавался как учебный, но постепенно был доведен до уровня production-ready приложения.

---

## Возможности

- регистрация пользователей
- авторизация
- профиль пользователя
- загрузка аватара
- несколько Kanban-досок
- CRUD досок
- CRUD колонок
- CRUD задач
- дедлайны
- цветовые метки

---

## Используемые технологии

### Backend

- Python 3.12
- Django 5.2
- PostgreSQL
- Gunicorn

### Frontend

- HTML
- CSS
- JavaScript
- Django Templates

### Infrastructure

- Docker
- Docker Compose
- Nginx
- GitHub Actions (планируется)

---

## Архитектура

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

## Структура проекта

applications/

config/

templates/

static/

media/

nginx/

scripts/

---

## Локальный запуск

```bash
git clone ...

docker compose up --build
```

---

## Production

```bash
docker compose -f docker-compose.prod.yml up -d
```

---

## Переменные окружения

```
DEBUG=False

SECRET_KEY=...

DB_NAME=dailyhub

DB_USER=postgres

DB_PASSWORD=...

DB_HOST=postgres

DB_PORT=5432
```

---

## Roadmap

### Version 1

- [x] Авторизация
- [x] Профиль
- [x] Kanban
- [x] Docker
- [x] PostgreSQL

### Version 2

- [ ] Архивирование задач
- [ ] Dashboard
- [ ] Drag&Drop
- [ ] Поиск
- [ ] Фильтрация

### Version 3

- [ ] CI/CD
- [ ] VPS Deploy
- [ ] HTTPS
- [ ] Monitoring

---

## Документация

- Architecture
- Deployment
- Docker
- Database

---

## Автор

Алла Вараксина
