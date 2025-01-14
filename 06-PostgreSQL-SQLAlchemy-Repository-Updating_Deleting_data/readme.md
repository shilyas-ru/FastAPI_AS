## Задание №6: Обновление и удаление данных через репозиторий

Необходимо создать 2 метода внутри BaseRepository по заданным сигнатурам (см. [скриншот](https://github.com/shilyas-ru/FastAPI_AS/blob/main/06-PostgreSQL-SQLAlchemy-Repository-Updating_Deleting_data/Screenshot_at_Aug_28_23-35-20.png)), а также переписать ручки PUT и DELETE.

***Скриншот:***<br>
<img src="https://github.com/shilyas-ru/FastAPI_AS/blob/main/06-PostgreSQL-SQLAlchemy-Repository-Updating_Deleting_data/Screenshot_at_Aug_28_23-35-20.png" alt="скриншот" height="135">

Не нужно переписывать PATCH ручку!

- Метод edit изменяет объект(ы) в базе данных. Для обновления объекта нужно принимать его id через параметры пути: PUT /hotels/{hotel_id}

- Метод delete удаляет объект(ы) в базе данных. Для удаления объекта нужно принимать его id через параметры пути: DELETE /hotels/{hotel_id}


*Задание со звездочкой (не рассматривается в решении): перед обновлением или удалением необходимо убедиться, что мы изменяем или удаляем именно один объект. То есть нам не подходят варианты, когда такого объекта нет или объектов с такими фильтрами больше одного. В таких случаях нужно выбрасывать ошибку:

- со статусом 404 в случае, если объект не найден;
- 400 или 422, если объектов больше одного.

*Код со [скриншота](https://github.com/shilyas-ru/FastAPI_AS/blob/main/06-PostgreSQL-SQLAlchemy-Repository-Updating_Deleting_data/Screenshot_at_Aug_28_23-35-20.png):*
```
async def edit(self, data: BaseModel, **filter_by) -> None:
    ...

async def delete(self, **filter_by) -> None:
    ...
```


### Уведомление
Перед запуском проекта требуется:
- Установить пакеты, указанные в файле "[requirements.txt](https://github.com/shilyas-ru/FastAPI_AS/tree/main/06-PostgreSQL-SQLAlchemy-Repository-Updating_Deleting_data/requirements.txt)".
- Создать в корне проекта файл `.env` и заполнить значения, указанные в файле `.env`:
```
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=
```



## Что сделано

К реализации в задании №5 (см. папку "[05-PostgreSQL-SQLAlchemy-Repository-Inserting_data](https://github.com/shilyas-ru/FastAPI_AS/tree/main/05-PostgreSQL-SQLAlchemy-Repository-Inserting_data)") добавлено:


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

- Структура проекта(см. файл "[06-PostgreSQL-SQLAlchemy-Repository-Updating_Deleting_data/project_structure.md](https://github.com/shilyas-ru/FastAPI_AS/tree/main/06-PostgreSQL-SQLAlchemy-Repository-Updating_Deleting_data/project_structure.md)").

- В файле "[ReadMe.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/06-PostgreSQL-SQLAlchemy-Repository-Updating_Deleting_data/src/models/ReadMe.md)" краткая справка по командам alembic

- Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](https://github.com/shilyas-ru/FastAPI_AS/blob/main/06-PostgreSQL-SQLAlchemy-Repository-Updating_Deleting_data/tables_in_database.png)".
