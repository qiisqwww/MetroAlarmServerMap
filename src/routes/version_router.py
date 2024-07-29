from fastapi import APIRouter

from src.city_alias import CityAlias
from src.config import (
    APP_VERSION,
    MSC_MAP_VERSION,
    SPB_MAP_VERSION
)

__all__ = [
    "version_router"
]


version_router = APIRouter(
    prefix="/version",
)


@version_router.get("/app")
async def get_app_version() -> dict:
    return {"app_version": APP_VERSION}


#  city_alias must be a query parameter.
@version_router.get("/city/")
async def get_city_version(city_alias: CityAlias) -> dict:
    match city_alias:
        case CityAlias.Moscow:
            return {"msc_map_version": MSC_MAP_VERSION}

        case CityAlias.Saint_Petersburg:
            return {"spb_map_version": SPB_MAP_VERSION}
