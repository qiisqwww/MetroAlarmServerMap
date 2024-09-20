import json
from loguru import logger

from src.application.repositories import (
    IStationRepository,
    ILineRepository,
    ICityRepository
)
from src.application.city_alias import CityAlias
from src.entities import City, Line, Station

__all__ = [
    "DBPrefillService"
]


class DBPrefillService:
    _station_repository: IStationRepository
    _line_repository: ILineRepository
    _city_repository: ICityRepository

    def __init__(
            self,
            station_repository: IStationRepository,
            line_repository: ILineRepository,
            city_repository: ICityRepository
    ) -> None:
        self._station_repository = station_repository
        self._line_repository = line_repository
        self._city_repository = city_repository

    async def prefill_db(self) -> None:
        if await self._database_already_filled():
            logger.info("Database already filled. Skipping process...")
            return
        logger.info("Database is not filled. Setting database base values...")

        await self._insert_cities_into_db()
        await self._insert_lines_into_db()
        await self._insert_stations_into_db()

        logger.info("Database base values was set.")

    async def _database_already_filled(self) -> bool:
        # If amount of stations added to db is bigger than zero, that means that basic values have already been set
        stations = await self._station_repository.get_stations()
        return len(stations) != 0

    async def _insert_cities_into_db(self) -> None:
        logger.info("Inserting cities into database...")

        # Reading & inserting cities
        for city_alias in CityAlias:
            with open(f"maps/{city_alias}_map.json", "r") as file:
                map_data = json.load(file)
                city = City(
                    id=map_data["city"]["id"],
                    name=map_data["city"]["name"],
                    name_eng=map_data["city"]["name_eng"],
                    alias=map_data["city"]["alias"]
                )
                await self._city_repository.insert_city(city)

    async def _insert_lines_into_db(self) -> None:
        logger.info("Inserting lines into database...")

        # Reading lines
        lines = []
        for city_alias in CityAlias:
            with open(f"maps/{city_alias}_map.json", "r") as file:
                map_data = json.load(file)
                for line in map_data["lines"]:
                    lines.append(Line(
                        id=line["id"],
                        city_id=line["city_id"],
                        name=line["name"],
                        alias=line["alias"],
                        logo_path=line["path_logo"]
                    ))

        # Inserting lines
        await self._line_repository.insert_lines(lines)

    async def _insert_stations_into_db(self) -> None:
        logger.info("Inserting stations into database...")

        # Reading stations
        stations = []
        for city_alias in CityAlias:
            with open(f"maps/{city_alias}_map.json", "r") as file:
                map_data = json.load(file)
                for station in map_data["stations"]:
                    stations.append(Station(
                        id=station["id"],
                        name=station["name"],
                        latitude=station["latitude"],
                        longitude=station["longitude"],
                        line_id=station["line_id"],
                        city_id=map_data["city"]["id"],
                        first_neighbour_id=station["id_neighbour1"],
                        second_neighbour_id=station["id_neighbour2"]
                    ))

        # Inserting stations
        await self._station_repository.insert_stations(stations)
