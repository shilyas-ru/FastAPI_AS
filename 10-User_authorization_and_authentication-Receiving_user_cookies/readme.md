## Задание №9: Получение cookie пользователя внутри ручки

Необходимо реализовать получение токена access_token из cookie пользователя, которые отправляет браузер. Внутри cookie может либо находится наш токен, либо будет пусто (если юзер не аутентифицирован).

Цель задания — открыть для себя мир исходного кода библиотек, с которыми вы работаете. Взглянуть на код, который пишут продвинутые Python разработчики (см. [скриншот](https://github.com/shilyas-ru/FastAPI_AS/blob/main/10-User_authorization_and_authentication-Receiving_user_cookies/Screenshot_at_Aug_28_23-55-56.png)), а также переписать ручки PUT и DELETE.

***Скриншот:***<br>
<img src="https://github.com/shilyas-ru/FastAPI_AS/blob/main/10-User_authorization_and_authentication-Receiving_user_cookies/Screenshot_at_Aug_28_23-55-56.png" alt="скриншот" height="135">


*Код со [скриншота](https://github.com/shilyas-ru/FastAPI_AS/blob/main/10-User_authorization_and_authentication-Receiving_user_cookies/Screenshot_at_Aug_28_23-55-56.png):*
```
@router.get("/only_auth")
async def only_auth(
        request: Request,
):
    ...
    access_token = "..." or None
```



### Уведомление
Перед запуском проекта требуется:
- Установить пакеты, указанные в файле "[requirements.txt](https://github.com/shilyas-ru/FastAPI_AS/tree/main/10-User_authorization_and_authentication-Receiving_user_cookies/requirements.txt)".
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

К заданию №8 "Запретить создание нескольких юзеров с одинаковой почтой" (см. папку "[09-User_authorization_and_authentication-User_registration](https://github.com/shilyas-ru/FastAPI_AS/tree/main/09-User_authorization_and_authentication-User_registration)") добавлено:

- Создан роутер для работы с пользователями (см. файл "[src/api/routers/auth.py](https://github.com/shilyas-ru/FastAPI_AS/tree/main/10-User_authorization_and_authentication-Receiving_user_cookies/src/api/routers/auth.py)"), написана обработка:
    - post("/auth/login") - Проверка, что пользователь существует и может 
        авторизоваться.<br>
        Функция: login_user_post
    - post("/auth/register") - Создание записи с новым пользователем.<br>
        Функция: register_user_post
    - post("/auth/only_auth") - Тестовый метод для получения куков по имени 
        (в примере проверяется значение для access_token).<br>
        Функция: only_auth

- Создан файл для работы с токенами, авторизацией, хешированием паролей и т.д. (см. файл "[src/services/auth.py](https://github.com/shilyas-ru/FastAPI_AS/tree/main/10-User_authorization_and_authentication-Receiving_user_cookies/src/services/auth.py)"), используется в "[src/api/routers/auth.py](https://github.com/shilyas-ru/FastAPI_AS/tree/main/10-User_authorization_and_authentication-Receiving_user_cookies/src/api/routers/auth.py)"



Рабочие ссылки (список методов, параметры в подробном перечне):
- post("/auth/login") - Проверка, что пользователь существует и может 
    авторизоваться.<br>
    Функция: login_user_post
- post("/auth/register") - Создание записи с новым пользователем.<br>
    Функция: register_user_post
- post("/auth/only_auth") - Тестовый метод для получения куков по имени 
    (в примере проверяется значение для access_token).<br>
    Функция: only_auth



## Итог

- Обновлена структура проекта(см. файл "[10-User_authorization_and_authentication-Receiving_user_cookies/project_structure.md](https://github.com/shilyas-ru/FastAPI_AS/tree/main/10-User_authorization_and_authentication-Receiving_user_cookies/project_structure.md)").

- Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](https://github.com/shilyas-ru/FastAPI_AS/blob/main/10-User_authorization_and_authentication-Receiving_user_cookies/tables_in_database.png)".

- В файле "[variables_abbreviations_and_naming.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/10-User_authorization_and_authentication-Receiving_user_cookies/src/models/variables_abbreviations_and_naming.md)" описываются используемые сокращения и именования переменных/классов/прочего.

- В файле "[ReadMe.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/10-User_authorization_and_authentication-Receiving_user_cookies/src/models/ReadMe.md)" краткая справка по командам alembic
