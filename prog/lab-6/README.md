# FastAPI Глоссарий (SQLite + Docker + Nginx)

Простое API-приложение для управления терминами глоссария, реализованное на FastAPI с использованием SQLite, Docker и Nginx.

---

## Развертывание

1. **Клонируй/распакуй проект**  
2. **Сборка контейнеров**

```bash
docker-compose up --build
```

3. **Тест работы с помощью Swagger**  
http://localhost/docs

---

## Как должен выглядеть проект после развертывания  
<img src="https://raw.githubusercontent.com/ArtemijKarandashov/term4/refs/heads/main/prog/lab-6/screenshots/swagger.jpg"/>  

---

## Очистка контейнера и БД

```bash
docker-compose down -v
```

---
