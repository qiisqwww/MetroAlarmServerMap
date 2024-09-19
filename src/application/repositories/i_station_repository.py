from abc import ABC, abstractmethod

from src.entities.models import Station

__all__ = [
    "IStationRepository"
]


class IStationRepository(ABC):
    @abstractmethod
    async def insert_stations(self, stations: list[Station]) -> None:
        ...

    @abstractmethod
    async def get_stations(self) -> list[Station]:
        ...

    @abstractmethod
    async def get_station_by_city_id(self, city_id: int) -> list[Station]:
        ...
