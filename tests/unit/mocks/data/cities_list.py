from src.entities import City

__all__ = [
    "cities_list",
]


cities_list = [
    City(
        id=1,
        name="Москва",
        name_eng="Moscow",
        alias="msc"
    ),
    City(
        id=2,
        name="Санкт-Петербург",
        name_eng="Saint-Petersburg",
        alias="spb"
    )
]
