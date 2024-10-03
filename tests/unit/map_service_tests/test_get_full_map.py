import pytest

from src.application.services import MapService
from src.application.schemas import CitiesStationsMap, CityBase, StationBase, LineBase

from tests.unit.mocks.data import cities_list, lines_list, stations_list, fvrt_stations_list


fvrt_13_stations_ids = [station.station_id for station in fvrt_stations_list if station.user_id == 13]


@pytest.mark.asyncio()
@pytest.mark.parametrize(
    "user_id, expected",
    [
        (
            None,
            CitiesStationsMap(
                cities=[CityBase.model_validate(city) for city in cities_list],
                lines=[LineBase.model_validate(line) for line in lines_list],
                stations=[StationBase.from_orm_model(station) for station in stations_list]
            )
        ),
        (
            13,
            CitiesStationsMap(
                cities=[CityBase.model_validate(city) for city in cities_list],
                lines=[LineBase.model_validate(line) for line in lines_list],
                stations=[StationBase.from_orm_model(station, station.id in fvrt_13_stations_ids)
                          for station in stations_list]
            )
        )
    ]
)
async def test_get_full_map(user_id: int | None, expected: CitiesStationsMap, map_service: MapService) -> None:
    full_map = await map_service.get_full_map(user_id)
    assert full_map == expected
