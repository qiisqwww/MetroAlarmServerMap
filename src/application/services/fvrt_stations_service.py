from src.application.repositories import IStationRepository, IFvrtStationRepository

__all__ = [
    "FvrtStationsService"
]


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

    async def set_favourite_station(self, station_id: int, user_id: int) -> None:
        fvrt_station = await self._fvrt_station_repository.find_user_fvrt_station(station_id, user_id)
        if fvrt_station:
            return
        await self._fvrt_station_repository.insert_fvrt_station(station_id, user_id)

    async def remove_favourite_station(self, station_id: int, user_id: int) -> None:
        fvrt_station = await self._fvrt_station_repository.find_user_fvrt_station(station_id, user_id)
        if not fvrt_station:
            return
        await self._fvrt_station_repository.delete_fvrt_station(fvrt_station)
