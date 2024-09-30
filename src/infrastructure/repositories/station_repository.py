from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from src.infrastructure.repositories import Repository
from src.application.repositories import IStationRepository
from src.entities.models import Station

__all__ = [
    "StationRepository"
]


class StationRepository(Repository, IStationRepository):
    _model: type[Station]

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self._model = Station

    async def insert_stations(self, stations: list[Station]) -> None:
        self._session.add_all(stations)
        await self._session.commit()

    async def get_stations(self) -> list[Station]:
        stmt = select(self._model)
        return [station for station in await self._session.scalars(stmt)]

    async def get_stations_by_city_id(self, city_id: int) -> list[Station]:
        stmt = select(self._model).where(self._model.city_id == city_id)
        return [station for station in await self._session.scalars(stmt)]

    async def find_station_by_id(self, station_id: int) -> Station | None:
        stmt = select(self._model).where(self._model.id == station_id)
        return await self._session.scalar(stmt)
