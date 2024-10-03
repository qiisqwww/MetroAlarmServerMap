import pytest

from src.application.services import FvrtStationsService
from src.application.schemas import StationBase


@pytest.mark.asyncio()
@pytest.mark.parametrize(
    "station_id, user_id, expected",
    [
        (10001, 15, StationBase(
            id=10001,
            name="Бульвар Рокоссовского",
            longitude="55.81645",
            latitude="37.738477",
            line_id=1001,
            city_id=1,
            first_neighbour_id=None,
            second_neighbour_id=10002,
            is_favourite=True,
            radius=400
        )),
        (10002, 13, StationBase(
            id=10002,
            name="Черкизовская",
            longitude="55.81645",
            latitude="37.738477",
            line_id=1001,
            city_id=1,
            first_neighbour_id=10001,
            second_neighbour_id=10003,
            is_favourite=True,
            radius=400
        ))
    ]
)
async def test_station_was_set(
        station_id: int,
        user_id: int,
        expected: StationBase,
        fvrt_stations_service: FvrtStationsService,
) -> None:
    updated_station = await fvrt_stations_service.set_favourite_station(station_id, user_id)
    assert expected == updated_station


@pytest.mark.asyncio()
@pytest.mark.parametrize(
    "station_id, user_id, expected",
    [
        (10001, 13, StationBase(
            id=10001,
            name="Бульвар Рокоссовского",
            longitude="55.81645",
            latitude="37.738477",
            line_id=1001,
            city_id=1,
            first_neighbour_id=None,
            second_neighbour_id=10002,
            is_favourite=False,
            radius=400
        )),
        (10002, 15, StationBase(
            id=10002,
            name="Черкизовская",
            longitude="55.81645",
            latitude="37.738477",
            line_id=1001,
            city_id=1,
            first_neighbour_id=10001,
            second_neighbour_id=10003,
            is_favourite=False,
            radius=400
        ))
    ]
)
async def test_station_was_removed(
        station_id: int,
        user_id: int,
        expected: StationBase,
        fvrt_stations_service: FvrtStationsService,
) -> None:
    updated_station = await fvrt_stations_service.remove_favourite_station(station_id, user_id)
    assert expected == updated_station
