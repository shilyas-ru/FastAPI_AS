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

- Добавляем удобства (facilities) - это то, что предлагается в номере:
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



## Итог

- Обновлена структура проекта(см. файл "[project_structure.md](project_structure.md)").

- Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](tables_in_database.png)".

- В файле "[variables_abbreviations_and_naming.md](variables_abbreviations_and_naming.md)" описываются используемые сокращения и именования переменных/классов/прочего.

- В файле "[ReadMe.md](src/models/ReadMe.md)" краткая справка по командам alembic
