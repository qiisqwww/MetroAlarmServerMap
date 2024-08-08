import json

from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from src.database import async_session_maker
from src.models import City, Line, Station
from src.city_alias import CityAlias

__all__ = [
    "set_database_base_values"
]


async def set_database_base_values() -> None:
    async with async_session_maker() as session:
        if await database_already_filled(session):
            logger.info("Database already filled. Skipping...")
            return
        logger.info("Database is not filled. Setting database base values...")

        cities = await insert_cities_into_database(session)
        lines = await insert_lines_into_database(session)
        stations = await insert_stations_into_database(session)

        logger.info("Database base values set.")


async def database_already_filled(session: AsyncSession) -> bool:
    stmt = select(City)
    cities_to_check = [city for city in await session.scalars(stmt)]

    return len(cities_to_check) != 0


async def insert_cities_into_database(session: AsyncSession) -> list[City]:
    logger.info("Inserting cities into database...")

    # Inserting cities
    for city_alias in CityAlias:
        with open(f"{city_alias}_map.json", "r") as file:
            map_data = json.load(file)
            city = City(id=map_data["city"]["id"], name=map_data["city"]["name"])
            session.add(city)

    # Returning data about cities
    stmt = select(City)
    cities_return = [city for city in await session.scalars(stmt)]

    return cities_return


async def insert_lines_into_database(session: AsyncSession) -> list[Line]:
    logger.info("Inserting lines into database...")

    # Inserting lines
    for city_alias in CityAlias:
        with open(f"{city_alias}_map.json", "r") as file:
            map_data = json.load(file)
            lines = []
            for line in map_data["lines"]:
                lines.append(Line(id=line["id"], name=line["name"]))
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
        with open(f"{city_alias}_map.json", "r") as file:
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
                    first_neighbour_id=station["first_neighbour_id"],
                    second_neighbour_id=station["second_neighbour_id"],
                    radius=400,
                    radius_rate=0
                ))
            session.add(stations)
            await session.commit()

    stmt = select(Station)
    stations_return = [station for station in await session.scalars(stmt)]

    return stations_return
