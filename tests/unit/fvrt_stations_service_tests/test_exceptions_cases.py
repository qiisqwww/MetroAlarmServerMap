import pytest

from src.application.services import (
    FvrtStationsService,
    StationDoesNotExistException,
    FvrtStationAlreadySetException,
    FvrtStationWasNotFoundException
)


@pytest.mark.asyncio()
@pytest.mark.parametrize(
    "station_id, user_id",
    [
        (228, 13),
        (131, 12)
    ]
)
async def test_set_fvrt_station_does_not_exist(
        station_id: int,
        user_id: int,
        fvrt_stations_service: FvrtStationsService
) -> None:
    with pytest.raises(StationDoesNotExistException):
        await fvrt_stations_service.set_favourite_station(station_id, user_id)


@pytest.mark.asyncio()
@pytest.mark.parametrize(
    "station_id, user_id",
    [
        (228, 13),
        (131, 12)
    ]
)
async def test_remove_fvrt_station_does_not_exist(
        station_id: int,
        user_id: int,
        fvrt_stations_service: FvrtStationsService
) -> None:
    with pytest.raises(StationDoesNotExistException):
        await fvrt_stations_service.remove_favourite_station(station_id, user_id)


@pytest.mark.asyncio()
@pytest.mark.parametrize(
    "station_id, user_id",
    [
        (10001, 13),
        (10002, 15)
    ]
)
async def test_set_fvrt_station_already_set(
        station_id: int,
        user_id: int,
        fvrt_stations_service: FvrtStationsService
) -> None:
    with pytest.raises(FvrtStationAlreadySetException):
        await fvrt_stations_service.set_favourite_station(station_id, user_id)


@pytest.mark.asyncio()
@pytest.mark.parametrize(
    "station_id, user_id",
    [
        (10001, 14),
        (10002, 13)
    ]
)
async def test_remove_fvrt_station_was_not_found(
        station_id: int,
        user_id: int,
        fvrt_stations_service: FvrtStationsService
) -> None:
    with pytest.raises(FvrtStationWasNotFoundException):
        await fvrt_stations_service.remove_favourite_station(station_id, user_id)
