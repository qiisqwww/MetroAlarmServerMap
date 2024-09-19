from typing import Annotated

from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database import get_async_session
from src.infrastructure.repositories import (
    StationRepository,
    LineRepository,
    CityRepository,
    FvrtStationRepository
)
from src.application.schemas import CityStationsMap, CitiesStationsMap
from src.application import MapService
from src.application import CityAlias

__all__ = [
    "map_router"
]


def get_map_service(session: AsyncSession = Depends(get_async_session)) -> MapService:
    return MapService(
        StationRepository(session),
        LineRepository(session),
        CityRepository(session),
        FvrtStationRepository(session)
    )


map_router = APIRouter()


@map_router.get("/full")
async def get_full_map(
        map_service: MapService = Depends(get_map_service)
) -> CitiesStationsMap:
    return await map_service.get_full_map()


@map_router.get("/city/{city_alias}")
async def get_city_map(
        city_alias: Annotated[CityAlias, Path(title="Alias of the city")],
        map_service: MapService = Depends(get_map_service)
) -> CityStationsMap:
    return await map_service.get_map_for_city(city_alias)
