<img src="https://gas-kvas.com/grafic/uploads/posts/2024-01/gas-kvas-com-p-smailik-chitaet-na-prozrachnom-fone-27.jpg" height="110" align="left" hspace="40">

При изучении FastAPI разрабатывается приложение для отелей. Каждое задание складывается в отдельную папку, а не оформляется коммитами - с точки зрения разработки это не совсем правильно (надо делать коммиты), но мне так удобнее.
<br><br>

## Задание №1: PUT и PATCH ручки отелей
Подробное описание в файле "[01-FirstLaunchOfFastAPI/readme.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/01-FirstLaunchOfFastAPI/readme.md)"

Необходимо реализовать 2 ручки:
- Ручка PUT на изменение отеля
- Ручка PATCH на изменения отеля

Код размещён в папке "[01-FirstLaunchOfFastAPI](https://github.com/shilyas-ru/FastAPI_AS/tree/main/01-FirstLaunchOfFastAPI)"



## Задание №2: Пагинация для отелей
Подробное описание в файле "[02-HotelsPagination/readme.md](https://github.com/shilyas-ru/FastAPI_AS/blob/main/02-HotelsPagination/readme.md)"

Необходимо реализовать пагинацию для отелей.

Для этого необходимо добавить 2 query параметра page и per_page, оба параметра являются необязательными. Если пользователь не передает page, то используется значение по умолчанию 1 (то есть первая страница). Для per_page ситуация аналогичная — если параметр не передается, то используется значение по умолчанию 3 (можете выбрать любое другое). 

Код размещён в папке "[02-HotelsPagination](https://github.com/shilyas-ru/FastAPI_AS/tree/main/02-HotelsPagination)"

