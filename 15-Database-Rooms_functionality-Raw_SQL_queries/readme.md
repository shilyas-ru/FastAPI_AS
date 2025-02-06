## Задание № 14: Вернуть пагинацию и фильтрацию в получение отелей
Необходимо добавить фильтрацию и пагинацию в метод get_filtered_by_time 
в HotelsRepository и в API ручку /hotels. 

Метод get_all в HotelsRepository необходимо удалить.



### Уведомление
Перед запуском проекта требуется:
- Установить пакеты, указанные в файле "[requirements.txt](https://github.com/shilyas-ru/FastAPI_AS/tree/main/15-Database-Rooms_functionality-Raw_SQL_queries/requirements.txt)".
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

К заданию №13: "Ручки на получение бронирований" (см. папку "[14-Database-Rooms_functionality-Getting_booking_room](https://github.com/shilyas-ru/FastAPI_AS/tree/main/14-Database-Rooms_functionality-Getting_booking_room)")

- Добавлено:
    - В репозитории BaseRepository добавлен метод get_filtered. Метод класса. 
      Выбирает строки по указанным фильтрам из таблицы. Сделано для применения метода get_filtered_by_time из репозитариев RoomsRepository и HotelsRepository.
    - В папке src\api\repositories создан файл utils.py с общими для разных репозитариев служебными функциями,
      добавлена в него функция rooms_ids_for_booking_query для формирования SQL-запроса на поиск свободных 
      номеров по всем отелям или для конкретного отеля.
    - В репозитории RoomsRepository добавлен метод get_filtered_by_time. Метод класса. 
      Выбирает все свободные номера в указанный промежуток времени (от date_from до date_to) 
      для указанного отеля. Сделано, чтобы понять работу выборки свободных (не забронированных) номеров.
    - В репозитории HotelsRepository добавлен метод get_filtered_by_time. Метод класса. 
      Выбирает все свободные номера в указанный промежуток времени (от date_from до date_to) 
      для указанного отеля. Сделано, чтобы понять работу выборки отелей, содержащих свободные (не забронированные) номера.
    - В репозитории HotelsRepository добавлен метод create_stmt_for_selection.
    - В репозитории RoomsRepository добавлен метод create_stmt_for_selection.

- Изменено:
    - В репозитории HotelsRepository изменен метод get_limit.
    - В репозитории HotelsRepository оставлен метод get_all, но по факту этот метод перестал использоваться, так как заменён методом get_limit.
    - В репозитории RoomsRepository изменен метод get_limit.
    - В репозитории RoomsRepository оставлен метод get_all, но по факту этот метод перестал использоваться, так как заменён методом get_limit.
    - В обработке эндпоинтов для номеров (rooms) заменен адрес get("/hotels/{hotel_id}/rooms") - вывод списка номеров для конкретного 
      отеля, весь список полностью, функция: show_rooms_in_hotel_all_get на два других:
        - get("/hotels/{hotel_id}/rooms/all") - Вывод для конкретного отеля списка ВСЕХ номеров, весь список полностью.
          Функция: show_rooms_in_hotel_all_get.
        -get("/hotels/{hotel_id}/rooms/free") - Вывод для конкретного отеля списка СВОБОДНЫХ номеров, весь список полностью.
        Функция: show_rooms_in_hotel_free_get.

- Для номеров сделано:
    - Поиск номера по параметрам (по наименованию/описанию номера) среди всех номеров или среди свободных в указанном диапазоне дат.
    - Удаление номера по параметрам (по наименованию/описанию номера).
    - Вывод всех номеров (адрес: /hotels/{hotel_id}/rooms/all).
    - Вывод только свободных в указанном диапазоне дат номеров (адрес: /hotels/{hotel_id}/rooms/free).

- Для отелей сделано:
    - Поиск отелей по параметрам (по наименованию/адресу отеля) среди всех отелей или среди отелей, имеющих свободные номера в указанном диапазоне дат.
    - Удаление отеля по параметрам (по наименованию/адресу отеля).
    - Вывод всех отелей (адрес: /hotels/all).
    - Вывод только отелей, имеющих свободные номера в указанном диапазоне дат (адрес: /hotels/free).




## Итог

- Обновлена структура проекта(см. файл "[project_structure.md](project_structure.md)").

- Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](tables_in_database.png)".

- В файле "[variables_abbreviations_and_naming.md](variables_abbreviations_and_naming.md)" описываются используемые сокращения и именования переменных/классов/прочего.

- В файле "[ReadMe.md](src/models/ReadMe.md)" краткая справка по командам alembic
