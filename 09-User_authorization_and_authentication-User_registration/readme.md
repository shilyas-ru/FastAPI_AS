## Задание №8: Запретить создание нескольких юзеров с одинаковой почтой
Необходимо запретить регистрацию пользователей с одинаковой почтой.

Например, если в базе данных уже есть пользователь с почтой kot@pes.ru, 
то второго пользователя с такой же почтой мы создать не можем.

Подумайте, как можно реализовать это на уровне модели/таблицы/базы данных, 
чтобы не пришлось дописывать дополнительную бизнес-логику внутри ручки 
или репозитория.



### Уведомление
Перед запуском проекта требуется:
- Установить пакеты, указанные в файле "[requirements.txt](https://github.com/shilyas-ru/FastAPI_AS/tree/main/09-User_authorization_and_authentication-User_registration/requirements.txt)".
- Создать в корне проекта файл `.env` и заполнить значения, указанные в файле `.env`:
```
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=
```



## Что сделано

К применению паттерна DataMapper (см. папку "[09-User_authorization_and_authentication-User_registration](https://github.com/shilyas-ru/FastAPI_AS/tree/main/09-User_authorization_and_authentication-User_registration)") добавлено:

Создана модель данных SQLAlchemy (см. файл "[src/models/users.py](https://github.com/shilyas-ru/FastAPI_AS/tree/main/09-User_authorization_and_authentication-User_registration/src/models/users.py)") на основании которой сгенерирована таблица для пользователей.

Созданы схемы Pydantic (см. файл "[src/schemas/users.py](https://github.com/shilyas-ru/FastAPI_AS/tree/main/09-User_authorization_and_authentication-User_registration/src/schemas/users.py)"), которая используется для преобразования полученных объектов SQLAlchemy к "понятному" виду.

Создан роутер для работы с пользователями (см. файл "[src/api/routers/auth.py](https://github.com/shilyas-ru/FastAPI_AS/tree/main/09-User_authorization_and_authentication-User_registration/src/api/routers/auth.py)"), которая используется для преобразования полученных объектов SQLAlchemy к "понятному" виду.

Рабочие ссылки (список методов, параметры в подробном перечне):
get("/auth/register") - Создание записи с новым пользователем.
        Функция: register_user_post
        В будущем надо добавить обработку ошибки, если 
        создаётся пользователь с уже существующим email.



## Итог

- Обновлена структура проекта(см. файл "[09-User_authorization_and_authentication-User_registration/project_structure.md](https://github.com/shilyas-ru/FastAPI_AS/tree/main/09-User_authorization_and_authentication-User_registration/project_structure.md)").

- Созданные таблицы в базе данных можно посмотреть на картинке "[tables_in_database.png](https://github.com/shilyas-ru/FastAPI_AS/blob/main/09-User_authorization_and_authentication-User_registration/tables_in_database.png)".

- В файле "[variables_abbreviations_and_naming.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/09-User_authorization_and_authentication-User_registration/src/models/variables_abbreviations_and_naming.md)" описываются используемые сокращения и именования переменных/классов/прочего.

- В файле "[ReadMe.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/09-User_authorization_and_authentication-User_registration/src/models/ReadMe.md)" краткая справка по командам alembic
