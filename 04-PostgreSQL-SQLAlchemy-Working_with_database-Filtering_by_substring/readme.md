## Задание №4: Фильтрация по подстроке

Необходимо изменить запрос на выборку отелей таким образом, чтобы
1. Поиск не производился по полю id (необходимо убрать id из query параметров).
2. Поиск производился по полям location и title. Причем оба поля необязательны.
3. Поиск по полям location и title должен осуществляться не по полному совпадению, 
а по вхождению вводимого пользователем значения в соответствующие столбцы таблицы.


### Уведомление
Перед запуском проекта требуется:
- Установить пакеты, указанные в файле "[requirements.txt](https://github.com/shilyas-ru/FastAPI_AS/tree/main/04-PostgreSQL-SQLAlchemy-Filtering_by_substring/requirements.txt)".
- Создать в корне проекта файл `.env` и заполнить значения, указанные в файле `.env`:
```
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=
```

## Что сделано

К реализации в задании №3 (см. папку "[03-PostgreSQL-SQLAlchemy-Models_and_Migrations](https://github.com/shilyas-ru/FastAPI_AS/tree/main/03-PostgreSQL-SQLAlchemy-Models_and_Migrations)") добавлено:

- Установлен пакет black и настроен alembic для работы с этим пакетом.
- Сделаны миграции, используя возможности пакета black (см. папку "[src/migration/versions](https://github.com/shilyas-ru/FastAPI_AS/tree/main/04-PostgreSQL-SQLAlchemy-Filtering_by_substring/src/migration/versions)").
- Схемы данных обновлены с учетом структуры данных (см. файл [src/schemas/hotels.py](https://github.com/shilyas-ru/FastAPI_AS/tree/main/04-PostgreSQL-SQLAlchemy-Filtering_by_substring/src/schemas/hotels.py)").
- Изменены методы API (теперь работа происходит с базой данных):
  - get("/hotels") - Вывод списка всех отелей с разбивкой по страницам или всего списка полностью.
  - get("/hotels/find") - Поиск отелей по заданным параметрам и вывод итогового списка с разбивкой по страницам.<br>
    Для поиска реализованы возможности:
    - искать с учётом регистра или не учитывая регистр букв;
    - искать строки, начинающиеся на заданное значение или искать строки, содержащие заданное значение.
  - delete("/hotels/{hotel_id}") - Удаление выбранной записи по идентификатору отеля.
  - delete("/hotels") - Удаление выбранных записей с выборкой, что удалять, по наименованию и адресу отеля. Для выбора удаляемых строк реализованы те же возможности, что и для поиска отелей (см. get("/hotels/find")).<br>
    Используются методы:
    - Удалить поэлементно: SELECT и удаление в цикле.
    - Удалить сразу всё: DELETE и одновременное удаление в СУБД.
  - post("/hotels") - Создание записи с новым отелем.
  - put("/hotels/{hotel_id}") - Обновление ВСЕХ данные одновременно для выбранной записи по идентификатору отеля.<br>
    Реализованы методы:
    - Обновить поэлементно: SELECT и обновление в цикле.
    - Обновить сразу всё: UPDATE и одновременное обновление в СУБД.
  - patch("/hotels/{hotel_id}") - Обновление каких-либо данных выборочно или всех данных сразу для выбранной записи по идентификатору отеля.
    

В методе API `delete("/hotels")` (удаление выбранных записей с выборкой, что удалять, по наименованию и адресу отеля, функция: `delete_hotel_param_del`) используется дополнительная возможность - получить список удаляемых записей через параметр <a href="https://docs.sqlalchemy.org/en/20/glossary.html#term-RETURNING" target="_blank">
RETURNING (описание в Glossary)</a>.
<br>См. пояснение в документации: 
<a href="https://docs.sqlalchemy.org/en/20/changelog/migration_06.html#returning-support" target="_blank">
RETURNING Support</a>:<br>
The insert(), update() and delete() constructs now support a returning() method, which 
corresponds to the SQL RETURNING clause as supported by PostgreSQL, Oracle, MS-SQL, 
and Firebird. It is not supported for any other backend at this time.<br>
Given a list of column expressions in the same manner as that of a select() construct, 
the values of these columns will be returned as a regular result set...


## Итог

- Описана структура проекта(см. файл "[04-PostgreSQL-SQLAlchemy-Filtering_by_substring/project_structure.md](https://github.com/shilyas-ru/FastAPI_AS/tree/main/04-PostgreSQL-SQLAlchemy-Filtering_by_substring/project_structure.md)").

- В файле "[ReadMe.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/04-PostgreSQL-SQLAlchemy-Filtering_by_substring/src/models/ReadMe.md)" краткая справка по командам alembic

- Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](https://github.com/shilyas-ru/FastAPI_AS/blob/main/04-PostgreSQL-SQLAlchemy-Filtering_by_substring/tables_in_database.png)".