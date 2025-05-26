@echo off
chcp 65001 > nul
echo ============================================================
echo Описание структуры FastAPI проекта
echo ============================================================
echo.
echo Это проект на FastAPI с следующей структурой:
echo.
echo 1. Основные компоненты:
echo    - app/                    : Основная директория приложения
echo    - app/main.py            : Главный файл приложения
echo    - app/config.py          : Конфигурация приложения
echo    - app/dependencies.py     : Зависимости FastAPI
echo.
echo 2. Модули приложения:
echo    - app/models/            : Модели SQLAlchemy для базы данных
echo    - app/schemas/           : Pydantic модели для валидации данных
echo    - app/crud/              : CRUD операции
echo    - app/routers/           : Маршруты API (endpoints)
echo    - app/utils/             : Вспомогательные функции
echo.
echo 3. База данных:
echo    - app/db/                : Настройки базы данных
echo    - migrations/            : Миграции Alembic
echo    - alembic.ini           : Конфигурация Alembic
echo.
echo 4. Тестирование:
echo    - app/tests/            : Модульные и интеграционные тесты
echo.
echo 5. Docker:
echo    - Dockerfile            : Сборка образа приложения
echo    - docker-compose.yml    : Оркестрация контейнеров
echo    - .dockerignore         : Исключения для Docker
echo.
echo 6. Зависимости:
echo    - requirements.txt      : Список Python пакетов
echo.
echo 7. Документация:
echo    - README.md            : Основная документация проекта
echo    - LICENSE              : Лицензия проекта
echo.
echo Описание моделей:
echo    - Book: Модель книги с полями:
echo      * title (String)         : Название книги
echo      * description (Text)     : Описание книги
echo      * author_id (Integer)    : ID автора
echo      * isbn (String)          : ISBN книги
echo      * average_rating (Float) : Средний рейтинг
echo      * ratings_count (Integer): Количество оценок
echo.
echo ============================================================
echo Для запуска проекта:
echo 1. Установите зависимости: pip install -r requirements.txt
echo 2. Запустите через Docker: docker-compose up
echo    или
echo    Запустите локально: uvicorn app.main:app --reload
echo ============================================================
pause 