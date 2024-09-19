from sqlalchemy.ext.asyncio import AsyncSession

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
