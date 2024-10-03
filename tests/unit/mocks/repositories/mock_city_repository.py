from src.application.repositories import ICityRepository
from src.entities import City

from tests.unit.mocks.data import cities_list

__all__ = [
    "MockCityRepository",
]


class MockCityRepository(ICityRepository):
    mocked_cities: list[City]

    def __init__(self) -> None:
        self.mocked_cities = cities_list.copy()

    async def insert_city(self, city: City) -> None:
        self.mocked_cities.append(city)

    async def get_city_by_name(self, city_name: str) -> City | None:
        for city in self.mocked_cities:
            if city.name == city_name:
                return city

        return None

    async def get_cities(self) -> list[City]:
        return self.mocked_cities
