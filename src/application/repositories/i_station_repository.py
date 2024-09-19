from abc import ABC, abstractmethod

from src.entities.models import Station

__all__ = [
    "IStationRepository"
]


class IStationRepository(ABC):
    @abstractmethod
    async def insert_stations(self, stations: list[Station]) -> None:
        ...
