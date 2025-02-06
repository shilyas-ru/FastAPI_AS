## Задание № 12: Ручка для добавления бронирования
Необходимо создать API ручку POST /bookings для добавления бронирования.

Принимаемые данные:
- date_from — дата заезда (только дата, без времени)
- date_to — дата выезда (только дата, без времени)
- room_id — id номера


Перед добавлением бронирования необходимо взять актуальную цену 
номера из таблицы rooms (поле price).

Напомню, что это задание предполагает создание новых:
- роутера и ручки
- pydantic схем
- репозитория
    
Конкретизировано в видео:

Не принимаем цену, потому что будем считать её на 
бэкэнде (получаем на уровне базы данных).
Не принимаем user_id, потому что будем получать его из 
авторизационных данных, из токена из куки.

И затем уже перегонять данные в другую pydantic-схему.


Подробное описание в файле "[13-Database-Rooms_functionality-Adding_booking_room/readme.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/13-Database-Rooms_functionality-Adding_booking_room/readme.md)"


Код размещён в папке "[13-Database-Rooms_functionality-Adding_booking_room](https://github.com/shilyas-ru/FastAPI_AS/tree/main/13-Database-Rooms_functionality-Adding_booking_room)"





### Уведомление
Перед запуском проекта требуется:
- Установить пакеты, указанные в файле "[requirements.txt](https://github.com/shilyas-ru/FastAPI_AS/tree/main/13-Database-Rooms_functionality-Adding_booking_room/requirements.txt)".
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

- Сделан асинхронный контекстный менеджер.
    - src/main.py - файл запуска приложения.
    - src/utils - папка с полезностями, небольшие классы/функции, которые используются во многих файлах и модулях.
    - файлы с кодом:
        - src/api/dependencies/dependencies.py: дополнен зависимостью для асинхронного контекстного менеджера.
        - src/utils/db_manager.py: файлы с утилитами.
        - src/api/routers/rooms.py: обработка конечных точек FastAPI для работы с номерами.
    - В репозиториях изменена обработка отсутствующего результата.
      Если раньше выводилось обычным способом, то сейчас возбуждается исключение HTTPException.
    - Сделан контекстный менеджер:
        - Создана папка src/utils, в которой размещён файл src/utils/db_manager.py - в нем код класса DBManager.
        - Файл с зависимостями src/api/dependencies/dependencies.py дополнен зависимостью для контекстного менеджера - DBDep
        - Весь код в роутерах изменен на работу с контекстным менеджером, то есть, конструкции вида:<br>
              `async with async_session_maker() as session:`<br>
              `    result = await HotelsRepository(session).delete(id=hotel_path.hotel_id)`<br>
              `    await session.commit()  # Подтверждаем изменение`<br>
              `return result`<br>
          заменены на конструкцию:<br>
              `result = await db.hotels.delete(id=hotel_path.hotel_id)`<br>
              `await db.commit()  # Подтверждаем изменение`<br>
              `return result`<br>
    - В репозитарии src/repositories/hotels.py добавлен метод create_stmt_for_selection, параметр которого sql_func принимает функцию для построения SQL-запроса (одна из: sqlalchemy.select, sqlalchemy.delete, sqlalchemy.update, sqlalchemy.insert).
    Этот метод подготавливает SQL-запрос, если требуется использовать свободные фильтры where или filter, а не filter_by.
    - В роутере для отелей src/api/routers/hotels.py функции find_hotels_get() и delete_hotel_param_del() исправлены на использование метода db.hotels.create_stmt_for_selection().
- Добавлено бронирование отелей.
    - Создан файл src\models\bookings.py с моделью для бронирования.
    - Дополнен файл \src\migration\env.py информацией о модели бронирования.
    - Создан файл src\migration\versions\2025_01_21_1915-66aead272fb4_005_add_bookings.py
    - Создана таблица бронирования - см. картинку в файле tables_in_database.png.
    - Создан файл src\repositories\bookings.py с классом репозитария для бронирования номеров, дочернего базовому.
    - Создан файл src\schemas\bookings.py со схемами данных для бронирования номеров, схемы используются в src/api/routers/bookings.py.
    - Создан файл src\api\routers\bookings.py с обработкой конечных точек FastAPI для бронирования номеров.
    - Сделана ручка для добавления бронипрования номера.
    - Дополнен файл \src\utils\db_manager.py информацией о модели бронирования.
    - Дополнен файл \src\main.py информацией о модели бронирования.



## Итог

- Обновлена структура проекта(см. файл "[project_structure.md](project_structure.md)").

- Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](tables_in_database.png)".

- В файле "[variables_abbreviations_and_naming.md](variables_abbreviations_and_naming.md)" описываются используемые сокращения и именования переменных/классов/прочего.

- В файле "[ReadMe.md](src/models/ReadMe.md)" краткая справка по командам alembic
