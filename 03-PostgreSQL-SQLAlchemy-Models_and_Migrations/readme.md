## Задание №3: Миграция для номеров

Необходимо создать миграцию (в Alembic они называются ревизии/revisions) 
через терминал ровно так же, как мы делали это в уроке.
Внутри миграции должны появиться изменения: добавление новой таблицы rooms.
После создания миграцию необходимо прогнать (запустить/применить), чтобы 
в базе данных появилась таблица rooms.


## Внимание!!!

Ссылка на гитхаб, заявленная в ответе для задания №3 "Миграция для номеров":
`https://github.com/shilyas-ru/FastAPI_AS/tree/main/03-PostgreSQL-SQLAlchemy/Models_and_Migrations`.


Потом проект из папки `03-PostgreSQL-SQLAlchemy/Models_and_Migrations` был перенесён в папку `03-PostgreSQL-SQLAlchemy-Models_and_Migrations`.


## Уведомление
Перед запуском проекта требуется:
- Установить пакеты, указанные в файле "[requirements.txt](https://github.com/shilyas-ru/FastAPI_AS/tree/main/03-PostgreSQL-SQLAlchemy-Models_and_Migrations/requirements.txt)".
- Создать в корне проекта файл `.env` и заполнить значения, указанные в файле `.env`:
```
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=
```



## Что сделано

К реализации в задании №2.2 (см. папку "[02-HotelsPagination/02_2-HotelsDependencies](https://github.com/shilyas-ru/FastAPI_AS/tree/main/02-HotelsPagination/02_2-HotelsDependencies)") добавлено:

- Установлен и настроен alembic.
- Сделаны миграции (см. папку "[src/migration/versions](https://github.com/shilyas-ru/FastAPI_AS/tree/main/03-PostgreSQL-SQLAlchemy-Models_and_Migrations/src/migration/versions)").



## Итог
Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](https://github.com/shilyas-ru/FastAPI_AS/blob/main/03-PostgreSQL-SQLAlchemy-Models_and_Migrations/tables_in_database.png)".
