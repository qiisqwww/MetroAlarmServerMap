from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from src.database import get_async_session
from src.schemas import CityStationsMap, CityBase, LineBase, StationBase
from src.models import City, Line, Station
from src.city_alias import CityAlias

__all__ = [
    "CityStationsMapService",
    "get_city_stations_service"
]


class CityStationsMapService:
    session: AsyncSession

    def __init__(self, session: AsyncSession) -> None:
        self.model = CityStationsMap
        self.session = session

    async def get_full_map(self) -> List[CityStationsMap]:
        pass

    async def find_city_by_city_alias(self, city_alias: CityAlias) -> CityBase | None:
        pass

    async def get_city_stations_map_by_city_name(self, city_name: str) -> CityStationsMap:
        pass


def get_city_stations_service(session: AsyncSession = Depends(get_async_session)) -> CityStationsMapService:
    return CityStationsMapService(session=session)
