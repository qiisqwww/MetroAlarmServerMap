from typing import Annotated

from fastapi import APIRouter, Depends, Query

from src.infrastructure.get_service import get_fvrt_stations_service
from src.application.services import FvrtStationsService


__all__ = [
    "fvrt_stations_router"
]


fvrt_stations_router = APIRouter(
    prefix="/favourite"
)


@fvrt_stations_router.patch("/set")
async def set_fvrt_station(
        station_id: Annotated[int, Query()],
        user_id: Annotated[int, Query()],
        fvrt_stations_service: FvrtStationsService = Depends(get_fvrt_stations_service)
) -> None:
    await fvrt_stations_service.set_favourite_station(station_id, user_id)


@fvrt_stations_router.patch("/remove")
async def remove_fvrt_station(
        station_id: Annotated[int, Query()],
        user_id: Annotated[int, Query()],
        fvrt_stations_service: FvrtStationsService = Depends(get_fvrt_stations_service)
) -> None:
    await fvrt_stations_service.remove_favourite_station(station_id, user_id)
