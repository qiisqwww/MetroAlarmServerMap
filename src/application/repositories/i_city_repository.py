from abc import ABC, abstractmethod

from src.entities.models import City

__all__ = [
    "ICityRepository"
]


class ICityRepository(ABC):
    @abstractmethod
    async def insert_city(self, city: City) -> None:
        ...

