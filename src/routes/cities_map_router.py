from typing import List, Annotated

from fastapi import APIRouter, Depends, Path

from src.schemas import CityStationsMap
from src.city_stations_map_service import CityStationsMapService, get_city_stations_map_service
from src.city_alias import CityAlias

__all__ = [
    "cities_map_router"
]


cities_map_router = APIRouter()


@cities_map_router.get("/full")
async def get_full_map(
        city_stations_service: CityStationsMapService = Depends(get_city_stations_map_service)
) -> List[CityStationsMap]:
    return await city_stations_service.get_full_map()


@cities_map_router.get("/city/{city_alias}")
async def get_city_map(
        city_alias: Annotated[CityAlias, Path(title="Alias of the city")],
        city_stations_service: CityStationsMapService = Depends(get_city_stations_map_service)
) -> CityStationsMap:
    return await city_stations_service.get_city_stations_map_by_city_alias(city_alias)
