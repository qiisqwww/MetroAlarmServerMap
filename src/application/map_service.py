from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from fastapi import Depends

from src.infrastructure.database import get_async_session
from src.infrastructure.schemas import CityStationsMap, CitiesStationsMap, CityBase, LineBase, StationBase
from src.entities.models import City, Line, Station
from src.application.city_alias import CityAlias

__all__ = [
    "MapService",
    "get_map_service"
]


class MapService:
    session: AsyncSession

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    # Now we do not search for user's favourite stations cuz auth microservice currently is not working
    async def get_full_map(self) -> CitiesStationsMap:
        stmt_cities = select(City)
        stmt_lines = select(Line)
        stmt_stations = select(Station)

        raw_cities = [city for city in await self.session.scalars(stmt_cities)]
        raw_lines = [line for line in await self.session.scalars(stmt_lines)]
        raw_stations = [station for station in await self.session.scalars(stmt_stations)]

        return CitiesStationsMap(
            cities=[CityBase.from_orm(raw_city) for raw_city in raw_cities],
            lines=[LineBase.from_orm(raw_line) for raw_line in raw_lines],
            stations=[StationBase.from_orm_model(raw_station) for raw_station in raw_stations]  # TODO: GET FAVOURITE ST
        )

    async def get_city_stations_map_by_city_alias(self, city_alias: CityAlias) -> CityStationsMap:
        city_name = city_alias.translation

        stmt_city = select(City).where(City.name == city_name)
        raw_city = await self.session.scalar(stmt_city)

        stmt_lines = select(Line).where(Line.city_id == raw_city.id)
        stmt_stations = select(Station).where(Station.city_id == raw_city.id)

        raw_lines = [line for line in await self.session.scalars(stmt_lines)]
        raw_stations = [station for station in await self.session.scalars(stmt_stations)]

        return CityStationsMap(
            city=CityBase.from_orm(raw_city),
            lines=[LineBase.from_orm(raw_line) for raw_line in raw_lines],
            stations=[StationBase.from_orm_model(raw_station) for raw_station in raw_stations]
        )


def get_map_service(session: AsyncSession = Depends(get_async_session)) -> MapService:
    return MapService(session=session)
