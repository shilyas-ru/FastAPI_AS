## Задание № 15: Получение и добавление удобств
Необходимо добавить роутер для удобств и две ручки:

    GET /facilities на получение всех удобств
    POST /facilities для добавления нового удобства

Обратите внимание, что пока мы не используем m2m таблицу. 
Она пригодится нам позже.


### Уведомление
Перед запуском проекта требуется:
- Установить пакеты, указанные в файле "[requirements.txt](requirements.txt)".
- Создать в корне проекта файл `.env` и заполнить значения, указанные в файле `.env`:
```
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=

JWT_SECRET_KEY=
JWT_ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```



## Что сделано

К заданию № 14: Вернуть пагинацию и фильтрацию в получение отелей (см. папку "[15-Database-Rooms_functionality-Raw_SQL_queries](../15-Database-Rooms_functionality-Raw_SQL_queries)"):

- Добавлено:
    - В базовом репозитории BaseRepositoryMyCode добавлен метод delete_id. Метод класса. Выбирает по идентификатору 
      (по первичному ключу) - поле self.model.id один объект в базе, используя метод get, удаляет методом session.delete.<br>
      Используются методы:
        - session.get(RoomsORM, object_id) для получения объекта по ключу
        - session.delete(room_object) для удаления объекта room_object.
        
    - Сделан репозитарий RoomsRepositoryMyCode, дочерний к базовому репозитарию BaseRepositoryMyCode (см. файл "[src/repositories/rooms.py](src/repositories/rooms.py)").

    - Сделана обработка эндпоинтов для номеров (см. файл "[src/api/routers/rooms.py](src/api/routers/rooms.py)").


Рабочие ссылки (список методов, параметры в подробном перечне):
- post("/hotels/room") - Создание записи с новой комнатой в отеле.
- get("/hotels/{hotel_id}/rooms") - Вывод списка номеров для конкретного 
        отеля - весь список полностью.
- get("/hotels/rooms/{room_id}") - Получение из базы данных выбранной 
        записи по идентификатору отеля.
- delete("/hotels/rooms/{room_id}") - Удаление выбранной записи по 
        идентификатору номера.
        Реализовано удаление одного объекта, когда объект для удаления получаем 
        по первичному ключу (метод session.get), удаляем методом session.delete.<br>
        Используются методы:
    - session.get(RoomsORM, id) для получения объекта по ключу
    - session.delete(room_object) для удаления объекта room_object.
- delete("/hotels/rooms/") - Удаление выбранной записи по 
        идентификатору номера.
        При желании можно дополнить удаление по любым условиям, а не только по id.
        Удаление выбранных записей реализовано через метод delete.
- put("/hotels/rooms/{room_id}") - Обновление ВСЕХ данных одновременно 
        для выбранной записи, выборка происходит по идентификатору номера.
- patch("/hotels/rooms/{room_id}") - Обновление каких-либо данных выборочно 
        или всех данных сразу для выбранной записи, выборка происходит по 
        идентификатору номера.



## Итог

- Обновлена структура проекта(см. файл "[project_structure.md](project_structure.md)").

- Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](tables_in_database.png)".

- В файле "[variables_abbreviations_and_naming.md](variables_abbreviations_and_naming.md)" описываются используемые сокращения и именования переменных/классов/прочего.

- В файле "[ReadMe.md](src/models/ReadMe.md)" краткая справка по командам alembic
