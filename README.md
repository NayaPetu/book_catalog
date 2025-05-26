# Каталог Книг API

Это RESTful API для управления каталогом книг, построенный с использованием FastAPI и PostgreSQL.

## 📚 Возможности

- ✅ Полное управление книгами (добавление, чтение, обновление, удаление)
- 👤 Аутентификация пользователей с помощью JWT
- ⭐ Система рейтингов и отзывов
- 🎯 Система рекомендаций книг на основе предпочтений пользователя
- 🔄 Автоматические миграции базы данных
- 🧪 Автоматическое тестирование (покрытие >70%)

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.8+
- Docker и Docker Compose
- PostgreSQL (если запускаете без Docker)

### Установка и запуск

1. **Клонирование репозитория**
   ```bash
   git clone <repository-url>
   cd project
   ```

2. **Настройка окружения**
   ```bash
   # Создание виртуального окружения
   python -m venv .venv
   
   # Активация окружения
   # Для Windows:
   .venv\Scripts\activate
   # Для Linux/Mac:
   source .venv/bin/activate
   
   # Установка зависимостей
   pip install -r requirements.txt
   ```

3. **Настройка переменных окружения**
   - Создайте файл `.env` на основе `.env.example`
   - Укажите необходимые параметры (DATABASE_URL, SECRET_KEY и т.д.)

4. **Запуск с помощью Docker**
   ```bash
   docker-compose up --build
   ```

5. **Применение миграций**
   ```bash
   alembic upgrade head
   ```

## 📖 Использование API

### Документация API
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Основные эндпоинты

- `POST /auth/register` - Регистрация нового пользователя
- `POST /auth/login` - Вход в систему
- `GET /books` - Получение списка книг
- `POST /books` - Добавление новой книги
- `GET /books/{id}` - Получение информации о конкретной книге
- `PUT /books/{id}` - Обновление информации о книге
- `DELETE /books/{id}` - Удаление книги

## 🧪 Тестирование

```bash
# Запуск всех тестов
pytest

# Запуск тестов с отчетом о покрытии
pytest --cov=app tests/
```

## 📦 Структура проекта

```
project/
├── app/
│   ├── api/
│   ├── core/
│   ├── crud/
│   ├── models/
│   ├── schemas/
│   └── utils/
├── migrations/
├── tests/
├── alembic.ini
├── docker-compose.yml
└── requirements.txt
```

## 🔄 Работа с миграциями

```bash
# Создание новой миграции
alembic revision --autogenerate -m "описание_изменений"

# Применение всех миграций
alembic upgrade head

# Откат последней миграции
alembic downgrade -1

# Просмотр истории миграций
alembic history
```

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для ваших изменений
3. Внесите изменения
4. Отправьте пулл-реквест

## 📝 Лицензия

MIT License - подробности в файле LICENSE

