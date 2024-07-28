from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from src.schemas import CityStationsMap
from src.city_stations_map_service import CityStationsMapService, get_city_stations_service
from src.city_alias import CityAlias

__all__ = [
    "cities_map_router"
]


cities_map_router = APIRouter(
    prefix="map",
)


@cities_map_router.get("/full")
async def get_full_map(
        city_stations_service: CityStationsMapService = Depends(get_city_stations_service)
) -> List[CityStationsMap]:
    return await city_stations_service.get_full_map()


#  city_name must be a query parameter.
@cities_map_router.get("/city/")
async def get_city_map(
        city_alias: CityAlias,
        city_stations_service: CityStationsMapService = Depends(get_city_stations_service)
) -> CityStationsMap:
    city = await city_stations_service.find_city_by_city_alias(city_alias)
    if not city:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"City with alias {city_alias} does not exist."
        )

    return await city_stations_service.get_city_stations_map_by_city_name(city_alias)
