from typing import Annotated

from fastapi import APIRouter, Depends, Query, HTTPException, status

from src.infrastructure.get_service import get_fvrt_stations_service
from src.application.services import (
    FvrtStationsService,
    StationDoesNotExistException,
    FvrtStationAlreadySetException,
    FvrtStationWasNotFoundException
)
from src.application.schemas import StationBase


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
) -> StationBase:
    try:
        updated_station = await fvrt_stations_service.set_favourite_station(station_id, user_id)
    except StationDoesNotExistException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trying to set favourite station which does not exist"
        ) from e
    except FvrtStationAlreadySetException as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Trying to set favourite station which has already been set so"
        ) from e

    return updated_station


@fvrt_stations_router.patch("/remove")
async def remove_fvrt_station(
        station_id: Annotated[int, Query()],
        user_id: Annotated[int, Query()],
        fvrt_stations_service: FvrtStationsService = Depends(get_fvrt_stations_service)
) -> StationBase:
    try:
        updated_station = await fvrt_stations_service.remove_favourite_station(station_id, user_id)
    except FvrtStationWasNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Trying to remove favourite station which was not set favourite (or station with id {station_id} "
                   f"does not exist)"
        ) from e

    return updated_station
