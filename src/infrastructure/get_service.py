from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from src.infrastructure.database import get_async_session, async_session_maker
from src.infrastructure.repositories import (
    StationRepository,
    LineRepository,
    CityRepository,
    FvrtStationRepository
)
from src.application.services import MapService, DBPrefillService

__all__ = [
    "get_map_service",
    "get_db_prefil_service"
]


def get_map_service(session: AsyncSession = Depends(get_async_session)) -> MapService:
    return MapService(
        StationRepository(session),
        LineRepository(session),
        CityRepository(session),
        FvrtStationRepository(session)
    )


def get_db_prefil_service() -> DBPrefillService:
    async with async_session_maker() as session:
        return DBPrefillService(
            StationRepository(session),
            LineRepository(session),
            CityRepository(session),
        )
