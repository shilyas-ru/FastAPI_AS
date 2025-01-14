## Задание №2: Пагинация для отелей

Необходимо реализовать пагинацию для отелей.

Для этого необходимо добавить 2 query параметра page и per_page, оба параметра являются необязательными. Если пользователь не передает page, то используется значение по умолчанию 1 (то есть первая страница). Для per_page ситуация аналогичная — если параметр не передается, то используется значение по умолчанию 3 (можете выбрать любое другое).



## Структура проекта
- Папка "[_course_helpers](https://github.com/shilyas-ru/FastAPI_AS/tree/main/02_1-HotelsPagination/_course_helpers)". Содержит код для сравнения времени работы FastAPI в синхронном и асинхронном режиме.
- Папка "[Routers_FastAPI](https://github.com/shilyas-ru/FastAPI_AS/tree/main/02_1-HotelsPagination/Routers_FastAPI)". Содержит API-роуты - файлы для обработки маршрутов FastAPI.
- Папка "[schemas](https://github.com/shilyas-ru/FastAPI_AS/tree/main/02_1-HotelsPagination/schemas)". Содержит схему данных, созданную с использованием Pydantic.
- В корне находится файл "[main.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02_1-HotelsPagination/main.py)" для запуска проекта.



## Что сделано

- К реализации в задании №1 (см. папку "[01-FirstLaunchOfFastAPI](https://github.com/shilyas-ru/FastAPI_AS/tree/main/01-FirstLaunchOfFastAPI)") добавлена пагинация: возможность вывода всего списка отелей сразу или вывод отелей с разбивкой по страницам.
- Обработка маршрутов, связанных с отелями, из файла "[main.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/01-FirstLaunchOfFastAPI/main.py)" перенесена в файл "[Routers_FastAPI/hotels_full_file.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02_1-HotelsPagination/Routers_FastAPI/hotels_full_file.py)".
- Создана схема данных, используя Pydantic. Файл со схемой данных "[schemas/hotels.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02_1-HotelsPagination/schemas/hotels.py)" и файл с обработкой маршрутов, преобразованный для работы с созданной схемой данных, "[Routers_FastAPI/hotels_schemas.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02_1-HotelsPagination/Routers_FastAPI/hotels_schemas.py)" .
- Сделаны несколько тестовых ручек для проверки, как оно работает. Для них в пути используется слово "/test" и в наименовании функции присутствует слово "_test".
- Добавлены примеры для входных данных для тестовых ручек - см. файлы "[Routers_FastAPI/hotels_schemas_examples.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02_1-HotelsPagination/Routers_FastAPI/hotels_schemas_examples.py)" и "[schemas/hotels_examples.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02_1-HotelsPagination/schemas/hotels_examples.py)".

В результате в итоговом файле "[main.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02_1-HotelsPagination/main.py)" осталось обращение к роутеру и добавлены разные метаданные.



Рабочие ссылки (список методов и запрашиваемые параметры приведены в подробном перечне в файле "[hotels.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02_1-HotelsPagination/Routers_FastAPI/hotels.py)"):
- get("/hotels") - Вывод списка всех отелей с разбивкой по страницам или всего списка полностью
- get("/hotels/{hotel_id}") - Вывод информации об одном отеле
- delete("/hotels/{hotel_id}") - Удаление выбранной записи
- post("/hotels") - Добавить данные
- put("/hotels/{hotel_id}") - Обновление ВСЕХ данные одновременно
- patch("/hotels/{hotel_id}") - Обновление каких-либо данных выборочно или всех данных сразу


**Подробнее** в файле "[hotels_schemas.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02_1-HotelsPagination/Routers_FastAPI/hotels_schemas.py)" или в файле "[hotels_full_file.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02_1-HotelsPagination/Routers_FastAPI/hotels_full_file.py)".
