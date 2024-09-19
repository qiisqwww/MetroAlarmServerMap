from src.application.schemas import (
    CityStationsMap,
    CitiesStationsMap,
    CityBase,
    LineBase,
    StationBase
)
from src.application.repositories import (
    IStationRepository,
    ILineRepository,
    ICityRepository,
    IFvrtStationRepository
)
from src.application.city_alias import CityAlias


__all__ = [
    "MapService"
]


class MapService:
    _station_repository: IStationRepository
    _line_repository: ILineRepository
    _city_repository: ICityRepository
    _fvrt_station_repository: IFvrtStationRepository

    def __init__(
            self,
            station_repository: IStationRepository,
            line_repository: ILineRepository,
            city_repository: ICityRepository,
            fvrt_station_repository: IFvrtStationRepository
    ) -> None:
        self._station_repository = station_repository
        self._line_repository = line_repository
        self._city_repository = city_repository
        self._fvrt_station_repository = fvrt_station_repository

    # Now we do not search for user's favourite stations cuz auth microservice currently is not working
    async def get_full_map(self) -> CitiesStationsMap:
        raw_cities = await self._city_repository.get_cities()
        raw_lines = await self._line_repository.get_lines()
        raw_stations = await self._station_repository.get_stations()

        return CitiesStationsMap(
            cities=[CityBase.from_orm(raw_city) for raw_city in raw_cities],
            lines=[LineBase.from_orm(raw_line) for raw_line in raw_lines],
            stations=[StationBase.from_orm_model(raw_station) for raw_station in raw_stations]  # TODO: GET FAVOURITE ST
        )

    async def get_map_for_city(self, city_alias: CityAlias) -> CityStationsMap:
        raw_city = await self._city_repository.get_city_by_name(city_alias.translation)
        raw_lines = await self._line_repository.get_lines_by_city_id(raw_city.id)
        raw_stations = await self._station_repository.get_station_by_city_id(raw_city.id)

        return CityStationsMap(
            city=CityBase.from_orm(raw_city),
            lines=[LineBase.from_orm(raw_line) for raw_line in raw_lines],
            stations=[StationBase.from_orm_model(raw_station) for raw_station in raw_stations]
        )