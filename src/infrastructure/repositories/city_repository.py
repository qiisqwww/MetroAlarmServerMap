from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

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

    async def get_cities(self) -> list[City]:
        stmt = select(self._model)
        return [city for city in await self._session.scalars(stmt)]

    async def get_city_by_name(self, city_name: str) -> City | None:
        stmt = select(City).where(City.name == city_name)
        return await self._session.scalar(stmt)
