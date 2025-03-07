## Структура проекта

```
Project
├── .env        Содержит описание переменных окружения. 
│               Этот файл никому не показывать, на гитхаб не выкладывать.
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
├── http_errors_statuses.txt        Описание http кодов ошибок, которые могут использоваться. 
│                                   Для справки.
├── project_structure.md            Этот файл
├── variables_abbreviations_and_naming.md       Используемые сокращения и  наименования
├── requirements.txt        Пакеты для установки
├── src
│   ├── config.py       Импорт переменных окружения из файла .env и 
│   │                   подготавливает их для использования в программе.
│   ├── database.py     Основной файл для работы с подключением к базе данных.
│   ├── main.py         Файл запуска приложения
│   ├── api: файлы приложения
│   │   ├── dependencies
│   │   │   ├── dependencies.py     Часто используемые классы (в моём 
│   │   │   │                       случае - описание пагинации).
│   │   │   ├── dependencies_consts.py     Константы, используемые в зависимостях 
│   │   ├── routers
│   │   │   ├── auth.py             Обработка конечных точек FastAPI для пользователей
│   │   │   ├── bookings.py         Обработка конечных точек FastAPI для бронирования номеров
│   │   │   ├── facilities.py       Обработка конечных точек FastAPI для удобств в номерах
│   │   │   ├── hotels.py           Обработка конечных точек FastAPI для отелей
│   │   │   ├── rooms.py            Обработка конечных точек FastAPI для номеров
│   ├── migration: файлы для миграций
│   │   ├── env.py          Настройки alembic
│   │   │                   - Добавляем код с новыми моделями (пример для модели RoomsORM)
│   │   │                     (from src.models.rooms import RoomsORM)
│   │   │                   - Изменяем код для обработки метаданных
│   │   │                     (from src.database import Base
│   │   │                     target_metadata = Base.metadata)
│   │   │                   - Устанавливаем параметр для правильной обработки миграций:
│   │   │                     config.set_main_option("sqlalchemy.url", 
│   │   │                                            f"{settings.DB_URL}?async_fallback=True")
│   │   ├── README
│   │   ├── script.py.mako
│   │   ├── versions        файлы со сгенерированным кодом для миграций
│   │   │   ├── 2024_12_16_2358-5142f000848b_001_create_table_hotels.py
│   │   │   ├── 2024_12_17_0004-5711a9787c99_002_create_rooms_hotels.py
│   │   │   ├── 2025_01_09_1440-ed77240b4dbc_003_add_users.py
│   │   │   ├── 2025_01_09_1848-1505718cb7dc_004_make_email_unique.py
│   │   │   ├── 2025_01_21_1915-66aead272fb4_005_add_bookings.py
│   │   │   ├── 2025_02_07_0117-d63318ef9cad_006_add_facilities.py
│   ├── models: файлы с моделями для работы с базой данных
│   │   ├── bookings.py     модель для работы с бронированием номеров 
│   │   │                   (создаваемые таблицы)
│   │   ├── facilities.py   модель для работы с удобствами в номерах 
│   │   │                   (создаваемые таблицы)
│   │   ├── hotels.py       модель для работы с отелями (создаваемые таблицы)
│   │   ├── rooms.py        модель для работы с номерами (создаваемые таблицы)
│   │   ├── users.py        модель для работы с пользователями (создаваемые 
│   │   │                   таблицы)
│   ├── repositories
│   │   ├── base.py         файл с классом базового репозитария (родительским).
│   │   ├── bookings.py     файл с классом репозитария для удобств в номерах, 
│   │   │                   дочернего базовому.
│   │   ├── facilities.py   файл с классом репозитария для бронирования номеров, 
│   │   │                   дочернего базовому.
│   │   ├── hotels.py       файл с классом репозитария для отелей, дочернего 
│   │   │                   базовому.
│   │   ├── rooms.py        файл с классом репозитария для номеров, дочернего 
│   │   │                   базовому.
│   │   ├── users.py        файл с классом репозитария для пользователей, 
│   │   │                   дочернего базовому.
│   │   ├── utils.py        файл с общими для разных репозитариев служебными 
│   │   │                   функциями.
│   ├── services: файлы с сервисным кодом
│   │   ├── auth.py         файл для работы с токенами, авторизацией, 
│   │   │                   хешированием паролей и т.д., которые используются 
│   │   │                   в src/api/routers/auth.py
│   ├── schemas: файлы со схемами данных
│   │   ├── facilities.py   файл со схемами данных для удобств в номерах, схемы 
│   │   │                   используются в src/api/routers/facilities.py
│   │   ├── hotels.py       файл со схемами данных для отелей, схемы 
│   │   │                   используются в src/api/routers/hotels.py
│   │   ├── bookings.py     файл со схемами данных для бронирования номеров, 
│   │   │                   схемы используются в src/api/routers/bookings.py
│   │   ├── rooms.py        файл со схемами данных для номеров, схемы 
│   │   │                   используются в src/api/routers/rooms.py
│   │   ├── users.py        файл со схемами данных для пользователей, схемы 
│   │   │                   используются в src/api/routers/users.py
│   ├── utils: папка для файлов с утилитами
│   │   ├── db_manager.py       файлы с утилитами
```

### Как создавалась структура проекта.

 1. Код проекта находится в папке src.

 2. Сначала написан код для обработки конечных точек FastAPI для работы с отелями:
    - src/main.py - файл запуска приложения.
    - файлы с кодом:
        - src/api/routers/hotels.py: обработка конечных точек FastAPI.
        - src/api/dependencies/dependencies.py: часто используемые классы 
          (в моём случае - описание пагинации).
        - src/schemas/hotels.py: файлы со схемами данных. 
          Используются в src/api/routers/hotels.py.
        - src/models/hotels.py: модель для работы с отелями 
          (создаваемые таблицы).
        - src/models/rooms.py: модель для работы с номерами 
          (создаваемые таблицы).

 3. Сделана обработка переменных окружения:
    - .env: содержит описание переменных окружения. Этот файл никому не 
      показывать, на гитхаб не выкладывать.
    - src/config.py: делает импорт переменных окружения из файла .env и 
      подготавливает их для использования в программе.

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

 7. Сделаны репозитарии в папке src/repositories:
    - src/repositories/base.py: файл с классом базового репозитария 
      (родительским).
    - src/repositories/hotels.py: файл с классом репозитария для отелей, 
      дочернего базовому.
    - src/repositories/rooms.py: файл с заготовкой для класса репозитария 
      для номеров, дочернего базовому.

 8. Реализован DataMapper - сделано преобразование возвращаемых данных к 
      схеме Pydantic.

 9. Написан код для обработки конечных точек FastAPI для работы с 
    пользователями:
    - src/main.py - файл запуска приложения.
    - файлы с кодом:
        - src/api/routers/auth.py: обработка конечных точек FastAPI для работы 
          с пользователем.
        - src/schemas/users.py: файлы со схемами данных. Используются 
          в src/api/routers/auth.py.
        - src/models/users.py: модель для работы с пользователями 
          (создаваемые таблицы).

10. Добавлена работа с JWT-токеном, дополнен список переменных в файле .env.
    - файлы с кодом:
        - src/services/auth.py: файлы с кодом для обработки JWT-токенов, 
          кодировки и декодировки сохраняемых токенов. 
          Используются в src/api/routers/auth.py.
        - src/api/routers/auth.py: Добавлена обработка конечных точек FastAPI 
          для работы с пользователем - вход/выход пользователя, получение 
          информации о теккущем пользователе, работа с куками.

11. Дополнен файл зависимостей кодом для получения идентификатора текущего 
    пользователя:
    - файлы с кодом:
        - src/api/dependencies/dependencies.py: дополнен зависимостью для 
          получения идентификатора текущего пользователя.

12. Написан код для обработки конечных точек FastAPI для работы с 
    пользователями, построены миграции для создания таблицы с пользователями 
    и таблица создана:
    - src/main.py - файл запуска приложения.
    - файлы с кодом:
        - src/api/routers/rooms.py: обработка конечных точек FastAPI для работы 
          с номерами.
        - src/schemas/users.py: файлы со схемами данных. Используются 
          в src/api/routers/auth.py.
        - src/models/users.py: модель для работы с пользователями 
          (создаваемые таблицы).
        - Сделаны миграции, добавлены файлы миграций:
            - src/migration/versions/2025_01_09_1440-ed77240b4dbc_003_add_users.py
            - 2025_01_09_1848-1505718cb7dc_004_make_email_unique.py

13. Делаем асинхронный контекстный менеджер.
    - src/main.py - файл запуска приложения.
    - src/utils - папка с полезностями, небольшие классы/функции, которые 
      используются во многих файлах и модулях.
    - файлы с кодом:
        - src/api/dependencies/dependencies.py: дополнен зависимостью для 
          асинхронного контекстного менеджера.
        - src/utils/db_manager.py: файлы с утилитами.
        - src/api/routers/rooms.py: обработка конечных точек FastAPI для 
          работы с номерами.
    - В репозиториях изменена обработка отсутствующего результата.
      Если раньше выводилось обычным способом, то сейчас возбуждается 
      исключение HTTPException.
    - Сделан контекстный менеджер:
        - Создана папка src/utils, в которой размещён файл 
          src/utils/db_manager.py - в нем код класса DBManager.
        - Файл с зависимостями src/api/dependencies/dependencies.py дополнен 
          зависимостью для контекстного менеджера - DBDep.
        - Весь код в роутерах изменен на работу с контекстным менеджером, 
          то есть, конструкции вида:<br>
              `async with async_session_maker() as session:`<br>
              `    result = await HotelsRepository(session).delete(id=hotel_path.hotel_id)`<br>
              `    await session.commit()  # Подтверждаем изменение`<br>
              `return result`<br>
          заменены на конструкцию:<br>
              `result = await db.hotels.delete(id=hotel_path.hotel_id)`<br>
              `await db.commit()  # Подтверждаем изменение`<br>
              `return result`<br>
    - В репозитарии src/repositories/hotels.py добавлен метод 
      create_stmt_for_selection, параметр которого sql_func принимает функцию 
      для построения SQL-запроса (одна из: sqlalchemy.select, sqlalchemy.delete,
      sqlalchemy.update, sqlalchemy.insert).
    Этот метод подготавливает SQL-запрос, если требуется использовать свободные 
    фильтры where или filter, а не filter_by.
    - В роутере для отелей src/api/routers/hotels.py функции find_hotels_get() 
      и delete_hotel_param_del() исправлены на использование метода 
      db.hotels.create_stmt_for_selection().

14. Добавлено бронирование отелей.
    - Создан файл src\models\bookings.py с моделью для бронирования.
    - Дополнен файл \src\migration\env.py информацией о модели бронирования.
    - Создан файл src\migration\versions\2025_01_21_1915-66aead272fb4_005_add_bookings.py
    - Создана таблица бронирования - см. картинку в файле tables_in_database.png.
    - Создан файл src\repositories\bookings.py с классом репозитария для 
      бронирования номеров, дочернего базовому.
    - Создан файл src\schemas\bookings.py со схемами данных для бронирования 
      номеров, схемы используются в src/api/routers/bookings.py.
    - Создан файл src\api\routers\bookings.py с обработкой конечных точек 
      FastAPI для бронирования номеров.
    - Сделана ручка для добавления бронипрования номера.
    - Дополнен файл \src\utils\db_manager.py информацией о модели бронирования.
    - Дополнен файл \src\main.py информацией о модели бронирования.

15. Добавляем возможность:
    - Выборки отелей, содержащих свободные (не забронированные) номера.
    - Выборки свободных (не забронированных) номеров.<br>
    Для этого:
        - В папке src\api\repositories создан файл utils.py с общими для разных 
          репозитариев служебными функциями,
          добавлена в него функция rooms_ids_for_booking_query для формирования 
          SQL-запроса на поиск свободных 
          номеров по всем отелям или для конкретного отеля.
        - В репозитории HotelsRepository добавлен метод create_stmt_for_selection.
        - В репозитории RoomsRepository добавлен метод create_stmt_for_selection.
        - В репозитории HotelsRepository изменен метод get_limit - добавлена 
          возможность выбирать отели со свободными номерами.
        - В репозитории RoomsRepository изменен метод get_limit - добавлена 
          возможность выбирать свободные номера.
        - Внесены изменения в код, позволяющие искать и удалять отели по 
          критериям, включающим использование критериев для всех отелей/номеров 
          или для отелей/номеров, имеющих свободные номера.
        - Сделана возможность вывода полного списка отелей/номеров и вывод 
          отелей/номеров со свободными номерами.

16. Добавляем удобства (facilities) - это то, что предлагается в номере:
    - Создаём две таблицы в БД: facilities и rooms_facilities 
      (таблица many-to-many).<br>
      Для этого:
        - В папке с моделями (src\models) создаём файл с моделями facilities.py. 
          Создали модели:
            - class FacilitiesORM(Base).
            - class RoomsFacilitiesORM(Base).
        - Заходим в миграции (файл src\migration\env.py), импортируем какой-либо
          класс из файла с новой моделью (src\models\facilities.py).
        - Прогоняем миграции: 
          alembic revision --autogenerate -m "006 Add facilities"
          Создан файл: 2025_02_07_0117-d63318ef9cad_006_add_facilities.py
        - Применяем все не обработанные миграции: alembic upgrade head
    - Реализуем две ручки для работы с удобствами (работаем с сущностью 
      FacilitiesORM из файла src\models\facilities.py): Получать список
      удобств и добавлять новое удобство.
      Для этого:
        - Делаем роутер. Создаём файл src\api\routers\facilities.py для 
          размещения кода для end-point'ов.
            - Делаем переменную с примерами: openapi_examples_dict
            - Делаем метод для создания удобств: create_facility_post
            - Делаем метод для вывода списка удобств: 
              show_facilities_in_rooms_get
        - Делаем Pydantic-схемы. Создаём файл src\schemas\facilities.py для 
          схем. В нём создаём нужные схемы:
            - class FacilityDescriptionRecURL(BaseModel).
            - class FacilityBase(BaseModel).
            - class FacilityPydanticSchema(FacilityBase).
        - Делаем репозиторий. Создаём файл src\repositories\facilities.py, 
          создаём:
            - Создали класс class FacilitiesRepository(BaseRepository) с 
              атрибутами:
                - model = FacilitiesORM.
                - schema = FacilityPydanticSchema.
            - Создали метод класса:
                - get_limit.
        - Добавляем в src\utils\db_manager.py:
            - Добавляем импорт: 
              from src.repositories.facilities import FacilitiesRepository.
            - В методе `async def __aenter__` добавляем: 
              self.facilities = FacilitiesRepository(self.session).
        - Редактируем файл src\main.py:
            - Добавляем импорт: 
              from src.api.routers.facilities import router as router_facilities.
            - Редактируем переменную openapi_tags - определяя параметры и 
              порядок вывода в документации.
            - Добавляем роутер: app.include_router(router_facilities).
    - Косметическая правка. В файле src\api\dependencies\dependencies.py 
      в классе PaginationPagesAllParams заменил наименование атрибута. 
      Обусловлено тем, что объекты для вывода сейчас не только отели.
        - Было: PaginationPagesAllParams.all_hotels.
        - Стало: PaginationPagesAllParams.all_objects.



