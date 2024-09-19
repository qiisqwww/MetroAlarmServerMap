import json

from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from src.infrastructure import async_session_maker
from src.entities import City, Line, Station
from src.application import CityAlias

__all__ = [
    "set_database_base_values"
]


async def set_database_base_values() -> None:
    async with async_session_maker() as session:
        if await database_already_filled(session):
            logger.info("Database already filled. Skipping process...")
            return
        logger.info("Database is not filled. Setting database base values...")

        cities = await insert_cities_into_database(session)
        lines = await insert_lines_into_database(session)
        stations = await insert_stations_into_database(session)

        logger.info("Database base values set.")


async def database_already_filled(session: AsyncSession) -> bool:
    # If amount of cities added to db is bigger than zero, that means that basic values have already been set
    stmt = select(City)
    cities_to_check = [city for city in await session.scalars(stmt)]

    return len(cities_to_check) != 0


async def insert_cities_into_database(session: AsyncSession) -> list[City]:
    logger.info("Inserting cities into database...")

    # Inserting cities
    for city_alias in CityAlias:
        with open(f"maps/{city_alias}_map.json", "r") as file:
            map_data = json.load(file)
            city = City(
                id=map_data["city"]["id"],
                name=map_data["city"]["name"],
                name_eng=map_data["city"]["name_eng"],
                alias=map_data["city"]["alias"]
            )
            session.add(city)

    # Returning data about cities
    stmt = select(City)
    cities_return = [city for city in await session.scalars(stmt)]

    return cities_return


async def insert_lines_into_database(session: AsyncSession) -> list[Line]:
    logger.info("Inserting lines into database...")

    # Inserting lines
    for city_alias in CityAlias:
        with open(f"maps/{city_alias}_map.json", "r") as file:
            map_data = json.load(file)
            lines = []
            for line in map_data["lines"]:
                lines.append(Line(
                    id=line["id"],
                    city_id=line["city_id"],
                    name=line["name"],
                    alias=line["alias"],
                    logo_path=line["path_logo"]
                ))
            session.add_all(lines)
            await session.commit()

    # Returning data about cities
    stmt = select(Line)
    lines_return = [line for line in await session.scalars(stmt)]

    return lines_return


async def insert_stations_into_database(session: AsyncSession) -> list[Station]:
    logger.info("Inserting stations into database...")

    # Inserting stations
    for city_alias in CityAlias:
        with open(f"maps/{city_alias}_map.json", "r") as file:
            map_data = json.load(file)
            stations = []
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
            session.add_all(stations)
            await session.commit()

    # Returning data about stations
    stmt = select(Station)
    stations_return = [station for station in await session.scalars(stmt)]

    return stations_return