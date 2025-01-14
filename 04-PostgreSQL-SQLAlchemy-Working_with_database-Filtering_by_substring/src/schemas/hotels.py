from pydantic import BaseModel, Field

# Pydantic 2: Полное руководство для Python-разработчиков — от основ до продвинутых техник
# https://fastapi.qubitpi.org/reference/fastapi/?h=tags_metadata#fastapi.FastAPI--example

# См. документацию про примеры:
# https://fastapi.tiangolo.com/ru/tutorial/schema-extra-example/?h=#body-with-multiple-examples
# https://fastapi.qubitpi.org/tutorial/schema-extra-example/?h=#body-with-multiple-examples


# class HotelPath(BaseModel):
#     hotel_id: int = Field(description="Идентификатор отеля",
#                           ge=1,
#                           examples=[1],
#                           )
#     # model_config = {
#     #     "json_schema_extra": {
#     #         # порядок вывод полей - алфавитный, а не как указано в коде.
#     #         "examples": [
#     #             {
#     #                 "hotel_id": 1,
#     #             }
#     #         ]
#     #     }
#     # }


hotel = {"title": "Название отеля",
         "location": "Местонахождение отеля",
         }

hotel_examples = {"title": "Название отеля",
                  "location": "Местонахождение отеля",
                  }

"""
Можно было бы описать один класс так:
class HotelCaption(BaseModel):
    hotel_title: str | None = Field(description=hotel["title"],
                                    min_length=3,
                                    )
    hotel_name: str | None = Field(description=hotel["name"],
                                   max_length=50,
                                   )
В этом случае параметры не имеют значения, присвоенного по умолчанию,
и должны считаться обязательными.
Чтобы сделать присвоение значений по умолчанию, можно в описании ручки сделать так:
@router.patch("/{hotel_id}",
              tags=["Отели"],
              summary="Обновление каких-либо данных выборочно или всех данных сразу",
              )
def hotel_patch(hotel_path: Annotated[HotelPath, Path()],
                hotel_caption: Annotated[HotelCaption, Body()] = HotelCaption(hotel_title=None,
                                                                              hotel_name=None),
                ):

Но этот метод плох тем, что через метод Body() можно передать с json значение None 
и pydantic его пропустит, например, так:
{
  "hotel_title": null,
  "hotel_name": "string"
}
"""


class HotelPath(BaseModel):
    # Поля указываем такие же, как в дальнейшем будем указывать в ссылках:
    # @router.delete("/{hotel_id}",...
    # Если поле в классе и имя переменной в ссылке будут различными, то возникнет
    # ошибка "422 unprocessable entity"
    hotel_id: int = Field(description="Идентификатор отеля",
                          ge=1,
                          examples=[1],
                          )


class HotelCaptionRec(BaseModel):
    # Поля указываем такие же, как именованы колонки в таблице
    # hotels (класс HotelsORM в файле src\models\hotels.py).
    title: str = Field(description=hotel["title"],
                       min_length=3,
                       examples=[hotel_examples["title"]],
                       )
    location: str = Field(description=hotel["location"],
                          max_length=50,
                          examples=[hotel_examples["location"]],
                          )


class HotelCaptionOpt(BaseModel):
    # Поля указываем такие же, как именованы колонки в таблице
    # hotels (класс HotelsORM в файле src\models\hotels.py).
    title: str | None = Field(default=None,
                              description=hotel["title"],
                              min_length=3,
                              examples=[hotel_examples["title"]],
                              )
    location: str | None = Field(default=None,
                                 description=hotel["location"],
                                 max_length=50,
                                 examples=[hotel_examples["location"]],
                                 )
