from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from src.infrastructure.repositories import Repository
from src.application.repositories import ILineRepository
from src.entities.models import Line

__all__ = [
    "LineRepository"
]


class LineRepository(Repository, ILineRepository):
    _model: type[Line]

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self._model = Line

    async def insert_lines(self, lines: list[Line]) -> None:
        self._session.add_all(lines)
        await self._session.commit()

    async def get_lines(self) -> list[Line]:
        stmt = select(self._model)
        return [line for line in await self._session.scalars(stmt)]

    async def get_lines_by_city_id(self, city_id: int) -> list[Line]:
        stmt = select(self._model).where(self._model.city_id == city_id)
        return [line for line in await self._session.scalars(stmt)]
