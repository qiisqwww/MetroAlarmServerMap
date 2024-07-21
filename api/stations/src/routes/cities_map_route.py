from fastapi import APIRouter

__all__ = [
    "cities_map_router"
]


cities_map_router = APIRouter(
    prefix="map",
)


@cities_map_router.get("/full")
async def get_full_map() -> None:
    return None


@cities_map_router.get("/city/")
async def get_city_map(name: str) -> None:
    return None

