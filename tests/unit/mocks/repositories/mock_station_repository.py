from src.application.repositories.i_station_repository import IStationRepository
from src.entities import Station

from tests.unit.mocks.data import stations_list

__all__ = [
    "MockStationRepository",
]


class MockStationRepository(IStationRepository):
    mocked_stations: list[Station]

    def __init__(self) -> None:
        self.mocked_stations = stations_list.copy()

    async def find_station_by_id(self, station_id: int) -> Station | None:
        for station in self.mocked_stations:
            if station.id == station_id:
                return station

        return None

    async def get_stations_by_city_id(self, city_id: int) -> list[Station]:
        stations = []
        for station in self.mocked_stations:
            if station.city_id == city_id:
                stations.append(station)

        return stations

    async def get_stations(self) -> list[Station]:
        return self.mocked_stations

    async def insert_stations(self, stations: list[Station]) -> None:
        pass
