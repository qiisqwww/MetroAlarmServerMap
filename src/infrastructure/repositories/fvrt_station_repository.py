from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from src.infrastructure.repositories import Repository
from src.application.repositories import IFvrtStationRepository
from src.entities.models import UserFavouriteStation

__all__ = [
    "FvrtStationRepository"
]


class FvrtStationRepository(Repository, IFvrtStationRepository):
    _model: type[UserFavouriteStation]

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self._model = UserFavouriteStation

    async def insert_fvrt_station(self, station_id: int, user_id: int) -> None:
        self._session.add(UserFavouriteStation(station_id=station_id, user_id=user_id))
        await self._session.commit()

    async def delete_fvrt_station(self, user_fvrt_station: UserFavouriteStation) -> None:
        await self._session.delete(user_fvrt_station)
        await self._session.commit()

    async def get_user_fvrt_stations(self, user_id: int) -> list[UserFavouriteStation]:
        stmt = select(self._model).where(self._model.user_id == user_id)
        return [fvrt_station for fvrt_station in await self._session.scalars(stmt)]

    async def find_user_fvrt_station(self, station_id: int, user_id: int) -> UserFavouriteStation | None:
        stmt = select(self._model).where(
            self._model.user_id == user_id,
            self._model.station_id == station_id
        )
        return await self._session.scalar(stmt)
