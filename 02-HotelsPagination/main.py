"""
## Задание №2: Пагинация для отелей

Необходимо реализовать пагинацию для отелей.

Для этого необходимо добавить 2 query параметра page и per_page,
оба параметра являются необязательными. Если пользователь не передает
page, то используется значение по умолчанию 1 (то есть первая страница).
Для per_page ситуация аналогичная — если параметр не передается,
то используется значение по умолчанию 3 (можете выбрать любое другое).
"""

"""
Импорт роутеров в справке.
    Учебник - Руководство пользователя -> Bigger Applications - Multiple Files
    https://fastapi.tiangolo.com/tutorial/bigger-applications/

An example file structure¶
Let's say you have a file structure like this:
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py

    Раздел "Import the APIRouter"
    https://fastapi.tiangolo.com/ru/tutorial/bigger-applications/#import-the-apirouter
Файл: app/main.py

from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

"""



import uvicorn
from fastapi import FastAPI

from Routers_FastAPI.hotels import router as router_hotels

tags_metadata = [
    {
        "name": "Отели",
        "description": "Операции с отелями.",
        "externalDocs":
            {
                "description": "Подробнее во внешней документации (сайт: https://example.com/)",
                "url": "https://example.com/",
            }
    },
]


app = FastAPI(openapi_tags=tags_metadata)
app.include_router(router_hotels)


if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=8000,
                reload=True)
