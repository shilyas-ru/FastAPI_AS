## Применение паттерна DataMapper



### Уведомление
Перед запуском проекта требуется:
- Установить пакеты, указанные в файле "[requirements.txt](https://github.com/shilyas-ru/FastAPI_AS/tree/main/08-PostgreSQL-SQLAlchemy-Repository-DataMapper/requirements.txt)".
- Создать в корне проекта файл `.env` и заполнить значения, указанные в файле `.env`:
```
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=
```



## Что сделано

К реализации в задании №7 (см. папку "[07-PostgreSQL-SQLAlchemy-Repository-Getting_data](https://github.com/shilyas-ru/FastAPI_AS/tree/main/07-PostgreSQL-SQLAlchemy-Repository-Getting_data)") добавлено:

Создана схема Pydantic (см. файл "[src/schemas/hotels.py](https://github.com/shilyas-ru/FastAPI_AS/tree/main/08-PostgreSQL-SQLAlchemy-Repository-DataMapper/src/schemas/hotels.py)"), которая используется для преобразования полученных объектов SQLAlchemy к "понятному" виду.


Изменения в репозитарии в базовом классе BaseRepositoryMyCode:
- Добавлен метод:
    - edit: метод класса. Редактирует один объект в базе, когда объект для обновления 
        получаем по первичному ключу (метод session.get).
        Обновление реализовано через обновление атрибутов 
        объекта: setattr(updated_object, key, value). 
        Возвращает Возвращает None или объект, преобразованный к схеме Pydantic.
    - get_one_or_none: метод класса. Возвращает одну строку или None. Если получено более одной строки, то поднимается исключение MultipleResultsFound. Использует штатный метод scalars().one_or_none().
- При возврате значений сделано преобразование объекта SQLAlchemy в Pydantic.

Изменения в репозитарий для отелей в классе HotelsRepositoryMyCode, дочернем к родительскому классу BaseRepositoryMyCode:
- Изменены методы:
  - get_one_or_none: метод класса. переименован в метод get_one_or_none_my_err.


Итоговые методы в репозитарии в базовом классе BaseRepositoryMyCode:
    - add. Метод класса. Добавляет один объект в базу, используя метод insert.
    - delete. Метод класса. Удаляет один объект в базе, используя метод delete.
    - edit. Метод класса. Редактирует один объект в базе, используя метод update.
    - edit_id. Метод класса. Выбирает по идентификатору (поле self.model.id) один
        объект в базе, используя метод get.
        Редактирует один объект в базе, обновление реализовано через обновление
        атрибутов объекта: setattr(updated_object, key, value).
    - get_id. Метод класса. Выбирает по идентификатору (поле self.model.id) один
        объект в базе, используя метод get.
    - get_one_or_none. Метод класса. Выбирает по идентификатору (поле self.model.id)
        объект в базе.
    - get_rows. Метод класса. Выбирает заданное количество строк с заданным смещением.


Итоговые методы в репозитарии в базовом классе HotelsRepositoryMyCode:
    - delete. Метод класса. Удаляет объект или объекты в базе, используя метод
        delete.
    - edit. Метод класса. Редактирует один объект в базе, используя метод
        update. Служит обёрткой для родительского метода edit.
    - get_all. Метод класса. Выбирает все строки. Использует родительский метод get_rows.
        Возвращает пустой список: [] или список из выбранных строк, преобразованных к схеме Pydantic.
    - get_id. Метод класса. Выбирает по идентификатору (поле self.model.id) один
        объект в базе, используя метод get.
    - get_limit. Метод класса. Выбирает заданное количество строк с
        заданным смещением. Использует родительский метод get_rows.
    - get_one_or_none_my_err. Метод класса. Возвращает одну строку или None. Если получено более
        одной строки, то поднимается исключение MultipleResultsFound.
        Использует родительский метод get_rows.

## Итог

- Обновлена структура проекта(см. файл "[08-PostgreSQL-SQLAlchemy-Repository-DataMapper/project_structure.md](https://github.com/shilyas-ru/FastAPI_AS/tree/main/08-PostgreSQL-SQLAlchemy-Repository-DataMapper/project_structure.md)").

- В файле "[variables_abbreviations_and_naming.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/08-PostgreSQL-SQLAlchemy-Repository-DataMapper/src/models/variables_abbreviations_and_naming.md)" описываются используемые сокращения и именования переменных/классов/прочего.

- В файле "[ReadMe.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/08-PostgreSQL-SQLAlchemy-Repository-DataMapper/src/models/ReadMe.md)" краткая справка по командам alembic

- Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](https://github.com/shilyas-ru/FastAPI_AS/blob/main/08-PostgreSQL-SQLAlchemy-Repository-DataMapper/tables_in_database.png)".
