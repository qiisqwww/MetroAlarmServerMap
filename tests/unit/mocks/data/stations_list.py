from src.entities import Station

__all__ = [
    "stations_list",
]


stations_list = [
        Station(
            id=10001,
            name="Бульвар Рокоссовского",
            longitude="55.81645",
            latitude="37.738477",
            line_id=1001,
            city_id=1,
            first_neighbour_id=None,
            second_neighbour_id=10002,
            radius=400
        ),
        Station(
            id=10002,
            name="Черкизовская",
            longitude="55.81645",
            latitude="37.738477",
            line_id=1001,
            city_id=1,
            first_neighbour_id=10001,
            second_neighbour_id=10003,
            radius=400
        ),
        Station(
            id=10003,
            name="Преображенская площадь",
            longitude="55.81645",
            latitude="37.738477",
            line_id=1001,
            city_id=1,
            first_neighbour_id=10002,
            second_neighbour_id=10004,
            radius=400
        )
    ]