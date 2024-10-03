from src.application.repositories import IFvrtStationRepository
from src.entities import UserFavouriteStation

from tests.unit.mocks.data import fvrt_stations_list

__all__ = [
    "MockFvrtStationRepository"
]


class MockFvrtStationRepository(IFvrtStationRepository):
    mocked_fvrt_stations: list[UserFavouriteStation]

    def __init__(self) -> None:
        self.mocked_fvrt_stations = fvrt_stations_list.copy()

    async def insert_fvrt_station(self, station_id: int, user_id: int) -> None:
        self.mocked_fvrt_stations.append(
            UserFavouriteStation(
                id=self.mocked_fvrt_stations[-1].id + 1,
                station_id=station_id,
                user_id=user_id
            )
        )

    async def find_user_fvrt_station(self, station_id: int, user_id: int) -> UserFavouriteStation | None:
        for fvrt_station in self.mocked_fvrt_stations:
            if fvrt_station.station_id == station_id and fvrt_station.user_id == user_id:
                return fvrt_station

        return None

    async def get_user_fvrt_stations(self, user_id: int) -> list[UserFavouriteStation]:
        fvrt_stations = []
        for fvrt_station in self.mocked_fvrt_stations:
            if fvrt_station.user_id == user_id:
                fvrt_stations.append(fvrt_station)

        return fvrt_stations

    async def delete_fvrt_station(self, user_fvrt_station: UserFavouriteStation) -> None:
        index = None
        for i in range(len(self.mocked_fvrt_stations)):
            if (self.mocked_fvrt_stations[i].user_id == user_fvrt_station.user_id
                    and self.mocked_fvrt_stations[i].id == user_fvrt_station.id):
                index = i
        self.mocked_fvrt_stations.pop(index)
