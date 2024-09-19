from sqlalchemy.ext.asyncio import AsyncSession

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
