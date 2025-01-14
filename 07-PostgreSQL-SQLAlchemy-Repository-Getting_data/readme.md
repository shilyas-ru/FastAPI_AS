## Задание №7: Ручка на получение отеля
Необходимо создать ручку для получения конкретного отеля `GET /hotels/{hotel_id}`, которая будет вызывать соответствующий метод репозитория и отдавать в ответе данные отеля.


### Уведомление
Перед запуском проекта требуется:
- Установить пакеты, указанные в файле "[requirements.txt](https://github.com/shilyas-ru/FastAPI_AS/tree/main/07-PostgreSQL-SQLAlchemy-Repository-Getting_data/requirements.txt)".
- Создать в корне проекта файл `.env` и заполнить значения, указанные в файле `.env`:
```
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=
```



## Что сделано

К реализации в задании №6 (см. папку "[06-PostgreSQL-SQLAlchemy-Repository-Updating_Deleting_data](https://github.com/shilyas-ru/FastAPI_AS/tree/main/06-PostgreSQL-SQLAlchemy-Repository-Updating_Deleting_data)") добавлено:


Изменения в репозитарии в базовом классе BaseRepositoryMyCode:
- Удалены методы:
  - add_item_insert: метод класса. Удалён.
  - add_item: метод класса. Удалён.
- Добавлены методы:
  - get_id: метод класса. Выбирает по идентификатору (поле self.model.id) один объект в базе, используя метод get. Возвращает объект sqlalchemy.engine.result.ChunkedIteratorResult. Для получения конкретного объекта требуется сделать, например, оператор result.scalars().all().
  - add: метод класса. Добавляет один объект в базу, используя метод insert. Возвращает список, содержащий добавленный объект.
  - delete: метод класса. Удаляет один объект в базе, используя метод delete. Возвращает объект sqlalchemy.engine.result.ChunkedIteratorResult. Для получения конкретного объекта требуется сделать, например, оператор result.scalars().all().
  - edit: метод класса. Редактирует один объект в базе, используя метод update. Возвращает объект sqlalchemy.engine.result.ChunkedIteratorResult. Для получения конкретного объекта требуется сделать, например, оператор result.scalars().all().


Изменения в репозитарий для отелей в классе HotelsRepositoryMyCode, дочернем к родительскому классу BaseRepositoryMyCode:
- Изменены методы:
  - get_all: метод класса. Изменено возвращаемое значение.
  - get_limit: метод класса. Изменены наименования аргументов и возвращаемое значение.
- Удалены методы:
  - add_item_insert: метод класса. Удалён.
  - add_item: метод класса. Удалён.
- Добавлены методы:
  - get_id: метод класса. Выбирает по идентификатору (поле self.model.id) один объект в базе, используя метод get. Возвращает словарь: `{"status": str, "err_type": int, "got row": dict}`.
  - delete: метод класса. Удаляет один объект в базе, используя метод delete. Возвращает словарь: `{"status": str, "err_type": int, "deleted rows": list(dict | [])}`.
  - edit: метод класса. Редактирует один объект в базе, используя метод update. Возвращает словарь: `{"status": status, "err_type": err_type, "updated rows": updated_rows}`.


## Итог

- Структура проекта(см. файл "[07-PostgreSQL-SQLAlchemy-Repository-Getting_data/project_structure.md](https://github.com/shilyas-ru/FastAPI_AS/tree/main/07-PostgreSQL-SQLAlchemy-Repository-Getting_data/project_structure.md)").

- В файле "[ReadMe.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/07-PostgreSQL-SQLAlchemy-Repository-Getting_data/src/models/ReadMe.md)" краткая справка по командам alembic

- Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](https://github.com/shilyas-ru/FastAPI_AS/blob/main/07-PostgreSQL-SQLAlchemy-Repository-Getting_data/tables_in_database.png)".
