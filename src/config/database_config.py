from sqlalchemy import insert

from src.database import get_async_session
from src.models import City, Line, Station

__all__ = [
    "set_database_base_values"
]


async def set_database_base_values() -> None:
    ...
