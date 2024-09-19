from abc import ABC, abstractmethod

from src.entities.models import Line

__all__ = [
    "ILineRepository"
]


class ILineRepository(ABC):
    @abstractmethod
    async def insert_lines(self, lines: list[Line]) -> None:
        ...

    @abstractmethod
    async def get_lines(self) -> list[Line]:
        ...

    @abstractmethod
    async def get_lines_by_city_id(self, city_id: int) -> list[Line]:
        ...
