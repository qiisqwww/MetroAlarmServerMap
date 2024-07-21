from fastapi import APIRouter

__all__ = [
    "version_router"
]


version_router = APIRouter(
    prefix="/version",
)


@version_router.get("/app")
async def get_cities_map() -> "str":
    return "0.0"


@version_router.get("/city/")
async def get_city_version(name: str) -> "str":
    return "0.0"
