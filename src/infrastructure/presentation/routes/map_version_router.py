from typing import Annotated

from fastapi import APIRouter, Path

from src.application.city_alias import CityAlias
from src.config import (
    MAP_VERSION,
    MSC_MAP_VERSION,
    SPB_MAP_VERSION
)

__all__ = [
    "map_version_router"
]


map_version_router = APIRouter(
    prefix="/version",
)


@map_version_router.get("/full")
async def get_data_version() -> dict:
    return {"map_version": MAP_VERSION}


@map_version_router.get("/city/{city_alias}")
async def get_city_version(city_alias: Annotated[CityAlias, Path(title="Alias of the city")]) -> dict:
    match city_alias:
        case CityAlias.Moscow:
            return {"msc_map_version": MSC_MAP_VERSION}

        case CityAlias.Saint_Petersburg:
            return {"spb_map_version": SPB_MAP_VERSION}
