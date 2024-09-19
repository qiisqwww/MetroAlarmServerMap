from abc import ABC, abstractmethod

from src.entities.models import UserFavouriteStation

__all__ = [
    "IFvrtStationRepository"
]


class IFvrtStationRepository(ABC):
    @abstractmethod
    async def insert_fvrt_station(self, station_id: int, user_id: int) -> None:
        ...

    @abstractmethod
    async def delete_fvrt_station(self, user_fvrt_station: UserFavouriteStation) -> None:
        ...

    @abstractmethod
    async def get_user_fvrt_stations(self, user_id: int) -> list[UserFavouriteStation]:
        ...

    @abstractmethod
    async def find_user_fvrt_station(self, station_id: int, user_id: int) -> UserFavouriteStation | None:
        ...
