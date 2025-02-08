    location_type = '' if starts_with else '%'
    get_hotels_query = select(HotelsORM)

    if not (hotel_location or hotel_title):
        return "Не заданы параметры для выбора отеля"

    if hotel_location:
        if case_sensitivity:
            get_hotels_query = (get_hotels_query
                                .where(HotelsORM.location.like(location_type + hotel_location + "%"))
                                )
        else:
            get_hotels_query = (get_hotels_query
                                .where(HotelsORM.location.ilike(location_type + hotel_location + "%"))
                                )

    if hotel_title:
        if case_sensitivity:
            get_hotels_query = (get_hotels_query
                                .filter(HotelsORM.title.like(location_type + hotel_title + "%"))
                                )
        else:
            get_hotels_query = (get_hotels_query
                                .filter(HotelsORM.title.ilike(location_type + hotel_title + "%"))
                                )

    get_hotels_query = get_hotels_query.order_by(HotelsORM.id)

    skip = (pagination.page - 1) * pagination.per_page
    get_hotels_query = (get_hotels_query.limit(pagination.per_page).offset(skip))

    async with async_session_maker() as session:
        return await HotelsRepository(session).get_limit(query=get_hotels_query,
                                                         per_page=pagination.per_page,
                                                         page=pagination.page)
