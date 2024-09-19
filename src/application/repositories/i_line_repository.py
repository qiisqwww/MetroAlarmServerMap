from abc import ABC, abstractmethod

from src.entities.models import Line

__all__ = [
    "ILineRepository"
]


class ILineRepository(ABC):
    @abstractmethod
    async def insert_lines(self, lines: list[Line]) -> None:
        ...
