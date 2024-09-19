from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.repositories import Repository
from src.application.repositories import ICityRepository
from src.entities.models import City

__all__ = [
    "CityRepository"
]


class CityRepository(Repository, ICityRepository):
    _model: type[City]

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self._model = City

    async def insert_city(self, city: City) -> None:
        self._session.add(city)
        await self._session.commit()
