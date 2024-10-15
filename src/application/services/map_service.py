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
    "CityWasNotFoundException",
    "MapService"
]


class CityWasNotFoundException(Exception):
    """
    Raised when cannot find a city with given city_alias
    """


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

    async def get_full_map(self, user_id: int = None) -> CitiesStationsMap:
        raw_cities = await self._city_repository.get_cities()
        raw_lines = await self._line_repository.get_lines()
        raw_stations = await self._station_repository.get_stations()

        if not user_id:
            return CitiesStationsMap(
                cities=[CityBase.model_validate(raw_city) for raw_city in raw_cities],
                lines=[LineBase.model_validate(raw_line) for raw_line in raw_lines],
                stations=[StationBase.from_orm_model(raw_station) for raw_station in raw_stations]
            )

        fvrt_stations = await self._fvrt_station_repository.get_user_fvrt_stations(user_id)
        fvrt_stations_ids = [fvrt_station.station_id for fvrt_station in fvrt_stations]

        return CitiesStationsMap(
            cities=[CityBase.model_validate(raw_city) for raw_city in raw_cities],
            lines=[LineBase.model_validate(raw_line) for raw_line in raw_lines],
            stations=[StationBase.from_orm_model(
                raw_station,
                raw_station.id in fvrt_stations_ids
            ) for raw_station in raw_stations]
        )

    async def get_map_for_city(self, city_alias: CityAlias, user_id: int = None) -> CityStationsMap:
        raw_city = await self._city_repository.get_city_by_name(city_alias.translation)
        if raw_city is None:
            raise CityWasNotFoundException
        raw_lines = await self._line_repository.get_lines_by_city_id(raw_city.id)
        raw_stations = await self._station_repository.get_stations_by_city_id(raw_city.id)

        if not user_id:
            return CityStationsMap(
                city=CityBase.model_validate(raw_city),
                lines=[LineBase.model_validate(raw_line) for raw_line in raw_lines],
                stations=[StationBase.from_orm_model(raw_station) for raw_station in raw_stations]
            )

        fvrt_stations = await self._fvrt_station_repository.get_user_fvrt_stations(user_id)
        fvrt_stations_ids = [fvrt_station.station_id for fvrt_station in fvrt_stations]

        return CityStationsMap(
            city=CityBase.model_validate(raw_city),
            lines=[LineBase.model_validate(raw_line) for raw_line in raw_lines],
            stations=[StationBase.from_orm_model(
                raw_station,
                raw_station.id in fvrt_stations_ids
            ) for raw_station in raw_stations]
        )
