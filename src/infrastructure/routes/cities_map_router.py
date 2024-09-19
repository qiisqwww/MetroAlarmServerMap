from typing import Annotated

from fastapi import APIRouter, Depends, Path
from src.infrastructure.get_service import get_map_service
from src.application.schemas import CityStationsMap, CitiesStationsMap
from src.application import MapService
from src.application import CityAlias

__all__ = [
    "map_router"
]


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
