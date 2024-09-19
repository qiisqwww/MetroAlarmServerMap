from fastapi import APIRouter

from .cities_map_router import map_router
from .map_version_router import map_version_router

__all__ = [
    "root_router"
]


root_router = APIRouter(prefix="/map")
root_router.include_router(map_router)
root_router.include_router(map_version_router)
