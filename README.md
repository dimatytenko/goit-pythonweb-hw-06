# University Database

Проект для роботи з базою даних університету, використовуючи SQLAlchemy та PostgreSQL.

## Вимоги

- Python 3.8+
- PostgreSQL
- Docker (опціонально)

## Встановлення

1. Клонуйте репозиторій:
```bash
git clone <repository-url>
cd university-db
```

2. Встановіть залежності за допомогою Poetry:
```bash
poetry install
```

3. Запустіть PostgreSQL (якщо використовуєте Docker):
```bash
docker run --name halamadrid-postgres -p 5432:5432 -e POSTGRES_PASSWORD=halamadrid -d postgres
```

4. Створіть базу даних:
```bash
docker exec -it halamadrid-postgres psql -U postgres -c "CREATE DATABASE university;"
```

5. Застосуйте міграції:
```bash
PYTHONPATH=. poetry run alembic upgrade head
```

6. Заповніть базу даних тестовими даними:
```bash
poetry run python seed.py
```

## Структура проекту

- `models.py` - моделі SQLAlchemy
- `config.py` - конфігурація підключення до бази даних
- `seed.py` - скрипт для заповнення бази даних тестовими даними
- `my_select.py` - функції для запитів до бази даних
- `alembic/` - міграції бази даних

## Використання

Для виконання запитів до бази даних використовуйте функції з файлу `my_select.py`:

```python
from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10

