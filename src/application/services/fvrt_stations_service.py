from src.application.repositories import IStationRepository, IFvrtStationRepository
from src.application.schemas import StationBase

__all__ = [
    "StationDoesNotExistException",
    "FvrtStationAlreadySetException",
    "FvrtStationWasNotFoundException",
    "FvrtStationsService"
]


class StationDoesNotExistException(Exception):
    """
    Raised when trying to make station favourite, but it does not exist.
    """


class FvrtStationAlreadySetException(Exception):
    """
    Raised when user is trying to make station favourite, but it has already been
    set to favourite before.
    """


class FvrtStationWasNotFoundException(Exception):
    """
    Raised when user is trying to remove favourite station which does not exist,
    or it wasn't set as favourite before.
    """


class FvrtStationsService:
    _station_repository: IStationRepository
    _fvrt_station_repository: IFvrtStationRepository

    def __init__(
            self,
            station_repository: IStationRepository,
            fvrt_station_repository: IFvrtStationRepository
    ) -> None:
        self._station_repository = station_repository
        self._fvrt_station_repository = fvrt_station_repository

    async def set_favourite_station(self, station_id: int, user_id: int) -> StationBase:
        station = await self._station_repository.find_station_by_id(station_id)
        if station is None:
            raise StationDoesNotExistException

        fvrt_station = await self._fvrt_station_repository.find_user_fvrt_station(station_id, user_id)
        if fvrt_station:
            raise FvrtStationAlreadySetException
        await self._fvrt_station_repository.insert_fvrt_station(station_id, user_id)

        return StationBase.from_orm_model(station, True)

    async def remove_favourite_station(self, station_id: int, user_id: int) -> StationBase:
        station = await self._station_repository.find_station_by_id(station_id)
        if station is None:
            raise StationDoesNotExistException

        fvrt_station = await self._fvrt_station_repository.find_user_fvrt_station(station_id, user_id)
        if not fvrt_station:
            raise FvrtStationWasNotFoundException
        await self._fvrt_station_repository.delete_fvrt_station(fvrt_station)

        return StationBase.from_orm_model(station, False)
