import pytest

from src.application.services import MapService
from src.application.schemas import CityStationsMap, CityBase, StationBase, LineBase
from src.application.city_alias import CityAlias

from tests.unit.mocks.data import cities_list, lines_list, stations_list, fvrt_stations_list


fvrt_13_moscow_stations_ids = [station.station_id for station in fvrt_stations_list if station.user_id == 13 and
                               station.station_id < 19999]  # Moscow station ids 10001 <= id < 19999


@pytest.mark.asyncio()
@pytest.mark.parametrize(
    "user_id, city_alias, expected",
    [
        (
            None,
            CityAlias.Moscow,
            CityStationsMap(
                city=cities_list[0],
                lines=[LineBase.model_validate(line) for line in lines_list if line.city_id == cities_list[0].id],
                stations=[StationBase.from_orm_model(station) for station in stations_list
                          if station.city_id == cities_list[0].id],
            )
        ),
        (
            13,
            CityAlias.Saint_Petersburg,
            CityStationsMap(
                city=cities_list[1],
                lines=[LineBase.model_validate(line) for line in lines_list if line.city_id == cities_list[1].id],
                stations=[StationBase.from_orm_model(station, station.id in fvrt_13_moscow_stations_ids)
                          for station in stations_list if station.city_id == cities_list[1].id],
            )
        )
    ]
)
async def test_get_city_map(
        user_id: int | None,
        city_alias: CityAlias,
        expected: CityStationsMap,
        map_service: MapService
) -> None:
    city_map = await map_service.get_map_for_city(city_alias, user_id)
    assert city_map == expected
