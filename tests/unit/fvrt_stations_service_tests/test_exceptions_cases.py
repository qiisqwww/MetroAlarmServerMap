import pytest

from src.application.services import (
    FvrtStationsService,
    StationDoesNotExistException
)

from tests.unit.mocks import (
    MockStationRepository,
    MockFvrtStationRepository
)


@pytest.mark.asyncio()
@pytest.mark.parametrize(
    "station_id, user_id",
    [
        ("228", 13),
        ("131", 12)
    ]
)
async def test_set_fvrt_station_does_not_exist(station_id: int, user_id: int) -> None:
    fvrt_stations_service = FvrtStationsService(
        MockStationRepository(),
        MockFvrtStationRepository()
    )

    with pytest.raises(StationDoesNotExistException):
        await fvrt_stations_service.set_favourite_station(station_id, user_id)


@pytest.mark.asyncio()
@pytest.mark.parametrize(
    "station_id, user_id",
    [
        ("228", 13),
        ("131", 12)
    ]
)
async def test_remove_fvrt_station_does_not_exist(station_id: int, user_id: int) -> None:
    fvrt_stations_service = FvrtStationsService(
        MockStationRepository(),
        MockFvrtStationRepository()
    )

    with pytest.raises(StationDoesNotExistException):
        await fvrt_stations_service.remove_favourite_station(station_id, user_id)
