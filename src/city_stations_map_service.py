from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from fastapi import Depends

from src.database import get_async_session
from src.schemas import CityStationsMap, CitiesStationsMap, CityBase, LineBase, StationBase
from src.models import City, Line, Station, UserFavouriteStation
from src.city_alias import CityAlias

__all__ = [
    "CityStationsMapService",
    "get_city_stations_map_service"
]


class CityStationsMapService:
    session: AsyncSession

    def __init__(self, session: AsyncSession) -> None:
        self.model = CityStationsMap
        self.session = session

    async def get_full_map(self) -> CitiesStationsMap:
        stmt_cities = select(City)
        stmt_lines = select(Line)
        stmt_stations = select(Station)

        cities = [city for city in await self.session.scalars(stmt_cities)]
        lines = [line for line in await self.session.scalars(stmt_lines)]
        raw_stations = [station for station in await self.session.scalars(stmt_stations)]

    async def get_city_stations_map_by_city_alias(self, city_alias: CityAlias) -> CityStationsMap:
        city_name = city_alias.translation


def get_city_stations_map_service(session: AsyncSession = Depends(get_async_session)) -> CityStationsMapService:
    return CityStationsMapService(session=session)
