## Структура проекта

```
Project
├── .env    Содержит описание переменных окружения. 
│           Этот файл никому не показывать, на гитхаб не выкладывать.
├── .gitignore      Какие файлы запрещено загружать на гитхаб
├── alembic.ini     Файл с настройками alembic
│                   В нём указан путь до папки с миграциями:
│                   script_location = src\migration
│                   Надо добавить папки в параметре
│                   prepend_sys_path = . src
│                   Если папку с миграциями переместить в другое место,
│                   то надо будет поменять эти параметры.
│                   Для работы с пакетом black:
│                   - Раскомментируем строки 73-76
│                   hooks = black
│                   black.type = console_scripts
│                   black.entrypoint = black
│                   black.options = -l 79 REVISION_SCRIPT_FILENAME
│                   В последней строке меняем 79 на 88 – это количество символов в строке.
│                   - Раскомментируем строку 12:
│                   file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s
├── project_structure.md
├── requirements.txt
├── src
│   ├── config.py       Импорт переменных окружения из файла .env и 
│   │                   подготавливает их для использования в программе.
│   ├── database.py     Основной файл для работы с подключением к базе данных.
│   ├── main.py         Файл запуска приложения
│   ├── api: файлы приложения
│   │   ├── dependencies
│   │   │   ├── dependencies.py     Часто используемые классы (в моём 
│   │   │   │                       случае - описание пагинации).
│   │   ├── routers
│   │   │   ├── hotels.py           Обработка конечных точек FastAPI
│   ├── migration: файлы для миграций
│   │   ├── env.py          Настройки alembic
│   │   │                   - Добавляем код с новыми моделями (пример для модели RoomsORM)
│   │   │                     (from src.models.rooms import RoomsORM)
│   │   │                   - Изменяем код для обработки метаданных
│   │   │                     (from src.database import Base
│   │   │                     target_metadata = Base.metadata)
│   │   │                   - Устанавливаем параметр для правильной обработки миграций:
│   │   │                     config.set_main_option("sqlalchemy.url", f"{settings.DB_URL}?async_fallback=True")
│   │   ├── README
│   │   ├── script.py.mako
│   │   ├── versions    файлы со сгенерированным кодом для миграций
│   │   │   ├── 2024_12_16_2358-5142f000848b_001_create_table_hotels.py
│   │   │   ├── 2024_12_17_0004-5711a9787c99_002_create_rooms_hotels.py
│   ├── models: файлы с моделями для работы с базой данных
│   │   ├── hotels.py       модель для работы с отелями (создаваемые таблицы)
│   │   ├── rooms.py        модель для работы с номерами (создаваемые таблицы)
│   ├── schemas: файлы со схемами данных
│   │   ├── hotels.py       файлы со схемами данных, используются в src/api/routers/hotels.py
```

### Как создавалась структура проекта.

1. Код проекта находится в папке src.

2. Сначала написан код для обработки конечных точек FastAPI:
src/main.py - файл запуска приложения.
файлы с кодом:
    - src/api/routers/hotels.py: обработка конечных точек FastAPI.
    - src/api/dependencies/dependencies.py: часто используемые классы (в моём случае - описание пагинации).
    - src/schemas/hotels.py: файлы со схемами данных. Используются в src/api/routers/hotels.py.
    - src/models/rooms.py: модель для работы с отелями (создаваемые таблицы).
    - src/models/rooms.py: модель для работы с номерами (создаваемые таблицы).

3. Сделана обработка переменных окружения:
    - .env: содержит описание переменных окружения. Этот файл никому не показывать, на гитхаб не выкладывать.
    - src/config.py: делает импорт переменных окружения из файла .env и подготавливает их для использования в программе.

4. Работа с базой данных:
    - src/database.py - основной файл для работы с подключением к базе данных.

5. Установлен alembic, добавились файлы:
    - alembic.ini
    - src/migration/env.py
    - src/migration/README
    - src/migration/script.py.mako
    - src/migration/versions

6. Сделаны миграции, добавлены файлы миграций:
    - src/migration/versions/2024_12_16_2358-5142f000848b_001_create_table_hotels.py
    - src/migration/versions/2024_12_17_0004-5711a9787c99_002_create_rooms_hotels.py