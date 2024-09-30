from abc import ABC, abstractmethod

from src.entities.models import City

__all__ = [
    "ICityRepository"
]


class ICityRepository(ABC):
    @abstractmethod
    async def insert_city(self, city: City) -> None:
        ...

    @abstractmethod
    async def get_cities(self) -> list[City]:
        ...

    @abstractmethod
    async def get_city_by_name(self, city_name: str) -> City | None:
        ...
