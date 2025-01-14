## Задание №5: Вставка данных через репозиторий
Необходимо добавить в BaseRepository метод add, который будет
- принимать данные для вставки
- отдавать записанные в базу данных данные в формате модели SQLAlchemy

Внутри ручки POST /hotels необходимо вернуть
```
{"status": "OK", "data": hotel}
```
где hotel — модель Алхимии, которую вернул репозиторий.


### Уведомление
Перед запуском проекта требуется:
- Установить пакеты, указанные в файле "[requirements.txt](https://github.com/shilyas-ru/FastAPI_AS/tree/main/05-PostgreSQL-SQLAlchemy-Repository-Inserting_data/requirements.txt)".
- Создать в корне проекта файл `.env` и заполнить значения, указанные в файле `.env`:
```
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=
```

## Что сделано

К реализации в задании №4 (см. папку "[04-PostgreSQL-SQLAlchemy-Filtering_by_substring](https://github.com/shilyas-ru/FastAPI_AS/tree/main/04-PostgreSQL-SQLAlchemy-Filtering_by_substring)") добавлено:


- Сделаны репозитарии в папке src/repositories:
  - src/repositories/base.py: файл с классом базового репозитария (родительским).
  - src/repositories/hotels.py: файл с классом репозитария для отелей, дочернего базовому.
  - src/repositories/rooms.py: файл с заготовкой для класса репозитария для номеров, дочернего базовому.

Базовый репозитарий содержит класс BaseRepositoryMyCode, который включает:
- model: атрибут класса.
- session: атрибут экземпляра класса.
- __init__: метод класса. Инициализирует объект класса при создании.
- get_rows: метод класса. Выбирает заданное количество строк с заданным смещением.
- add_item_insert: метод класса. Добавляет один объект в базу, используя метод insert. Возвращает номер добавленного объекта.
- add_item: метод класса. Добавляет один объект в базу, используя метод session.add. Возвращает добавленный объект.

Репозитарий для отелей содержит класс HotelsRepositoryMyCode, дочерний к родительскому классу BaseRepositoryMyCode. Класс HotelsRepositoryMyCode включает:
- __init__: метод класса. Инициализирует объект класса при создании.
- get_all: метод класса. Выбирает все строки. Использует родительский метод get_rows.
- get_limit: метод класса. Выбирает заданное количество строк с заданным смещением. Использует родительский метод get_rows.
- get_one_or_none: метод класса. Возвращает одну строку или None. Если получено более одной строки, то поднимается исключение MultipleResultsFound. Использует родительский метод get_rows.
- add_item_insert: метод класса. Добавляет один объект в базу, используя метод insert. Возвращает номер добавленного объекта. Служит обёрткой для родительского метода add_item_insert. Возвращает номер добавленного объекта.
- add_item: метод класса. Добавляет один объект в базу, используя метод session.add. Возвращает добавленный объект. Служит обёрткой для родительского метода add_item.


Репозитарий для комнат RoomsRepository находится в стадии разработки, файл пустой.


## Итог

- Обновлена структура проекта(см. файл "[05-PostgreSQL-SQLAlchemy-Repository-Inserting_data/project_structure.md](https://github.com/shilyas-ru/FastAPI_AS/tree/main/05-PostgreSQL-SQLAlchemy-Repository-Inserting_data/project_structure.md)").

- В файле "[ReadMe.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/05-PostgreSQL-SQLAlchemy-Repository-Inserting_data/src/models/ReadMe.md)" краткая справка по командам alembic

- Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](https://github.com/shilyas-ru/FastAPI_AS/blob/main/05-PostgreSQL-SQLAlchemy-Repository-Inserting_data/tables_in_database.png)".