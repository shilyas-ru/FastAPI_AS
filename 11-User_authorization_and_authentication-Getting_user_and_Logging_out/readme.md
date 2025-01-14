## Задание №10: Ручка на выход из системы

Необходимо реализовать ручку для выхода из системы. Ручку 
можно назвать /logout. После вызова ручки пользователя должно 
"разлогинить" — подумайте, как это можно реализовать, зная, 
как "залогинить" пользователя

Вам необходимо провести небольшое исследование и понять, 
какой HTTP метод стоит использовать для этой операции — GET, 
POST, PUT, PATCH или DELETE.



### Уведомление
Перед запуском проекта требуется:
- Установить пакеты, указанные в файле "[requirements.txt](https://github.com/shilyas-ru/FastAPI_AS/tree/main/11-User_authorization_and_authentication-Getting_user_and_Logging_out/requirements.txt)".
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

К заданию №9 "Получение cookie пользователя внутри ручки" (см. папку "[10-User_authorization_and_authentication-Receiving_user_cookies](https://github.com/shilyas-ru/FastAPI_AS/tree/main/10-User_authorization_and_authentication-Receiving_user_cookies)")

- Изменено:
    - get("/auth/only_auth"). Адрес для обращения изменён на "/auth/get_me", функция переименована в get_me_get, добавлено получение пользователя.

- Добавлено:
    - В классе AuthService добавлены методы для кодирования/декодирования JWT-токенов. Сделано для того, чтобы токен нельзя было расшифровать штатными инструментами.
    - В файле "[src/api/dependencies/dependencies.py](https://github.com/shilyas-ru/FastAPI_AS/tree/main/11-User_authorization_and_authentication-Getting_user_and_Logging_out/src/api/dependencies/dependencies.py)" добавлены функции: get_token и get_current_user_id.
    - delete("/auth/logout"). Выход авторизованного пользователя.
    Функция: get_me_delete.



Рабочие ссылки (список методов, параметры в подробном перечне):
- post("/auth/login") - Проверка, что пользователь существует и может 
    авторизоваться.<br>
    Функция: login_user_post
- post("/auth/register") - Создание записи с новым пользователем.<br>
    Функция: register_user_post
- get("/auth/get_me") - Тестовый метод для получения куков по имени 
    (в примере проверяется значение для access_token).<br>
    Функция: get_me_get
- delete("/auth/logout"). Выход авторизованного пользователя.
    Функция: get_me_delete.



## Итог

- Структура проекта(см. файл "[11-User_authorization_and_authentication-Getting_user_and_Logging_out/project_structure.md](https://github.com/shilyas-ru/FastAPI_AS/tree/main/11-User_authorization_and_authentication-Getting_user_and_Logging_out/project_structure.md)").

- Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](https://github.com/shilyas-ru/FastAPI_AS/blob/main/11-User_authorization_and_authentication-Getting_user_and_Logging_out/tables_in_database.png)".

- В файле "[variables_abbreviations_and_naming.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/11-User_authorization_and_authentication-Getting_user_and_Logging_out/src/models/variables_abbreviations_and_naming.md)" описываются используемые сокращения и именования переменных/классов/прочего.

- В файле "[ReadMe.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/11-User_authorization_and_authentication-Getting_user_and_Logging_out/src/models/ReadMe.md)" краткая справка по командам alembic
