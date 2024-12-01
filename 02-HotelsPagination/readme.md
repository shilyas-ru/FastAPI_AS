## Задание №2: Пагинация для отелей

Необходимо реализовать пагинацию для отелей.

Для этого необходимо добавить 2 query параметра page и per_page, оба параметра являются необязательными. Если пользователь не передает page, то используется значение по умолчанию 1 (то есть первая страница). Для per_page ситуация аналогичная — если параметр не передается, то используется значение по умолчанию 3 (можете выбрать любое другое).



## Структура проекта
- Папка "[_course_helpers](https://github.com/shilyas-ru/FastAPI_AS/tree/main/02-HotelsPagination/_course_helpers)". Содержит код для сравнения времени работы FastAPI в синхронном и асинхронном режиме.
- Папка "[Routers_FastAPI](https://github.com/shilyas-ru/FastAPI_AS/tree/main/02-HotelsPagination/Routers_FastAPI)". Содержит API-роуты - файлы для обработки маршрутов FastAPI.
- В корне находится файл "[main.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02-HotelsPagination/main.py)" для запуска проекта.



## Что сделано

<ul>
<li>К реализации в задании №1 (см. папку "[01-FirstLaunchOfFastAPI](https://github.com/shilyas-ru/FastAPI_AS/tree/main/01-FirstLaunchOfFastAPI)") добавлена пагинация: возможность вывода всего списка отелей сразу или вывод отелей с разбивкой по страницам.</li>
<li>Обработка маршрутов, связанных с отелями, из файла "[main.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/01-FirstLaunchOfFastAPI/main.py)" перенесена в файл "[Routers_FastAPI/hotels.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02-HotelsPagination/Routers_FastAPI/hotels.py)". В результате в итоговом файле "[main.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02-HotelsPagination/main.py)" осталось только обращение к роутеру.</li>
</ul>



Рабочие ссылки (список методов и запрашиваемые параметры приведены в подробном перечне в файле "[hotels.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02-HotelsPagination/Routers_FastAPI/hotels.py)"):
- get("/hotels") - Вывод списка всех отелей с разбивкой по страницам или всего списка полностью
- get("/hotels/{hotel_id}") - Вывод информации об одном отеле
- delete("/hotels/{hotel_id}") - Удаление выбранной записи
- post("/hotels") - Добавить данные
- put("/hotels/{hotel_id}") - Обновление ВСЕХ данные одновременно
- patch("/hotels/{hotel_id}") - Обновление каких-либо данных выборочно или всех данных сразу


**Подробнее в файле "[hotels.py](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02-HotelsPagination/Routers_FastAPI/hotels.py)"**
