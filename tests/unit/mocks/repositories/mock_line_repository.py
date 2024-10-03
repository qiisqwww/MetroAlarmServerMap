from src.application.repositories import ILineRepository
from src.entities import Line

__all__ = [
    "MockILineRepository"
]


class MockILineRepository(ILineRepository):
    mocked_lines: list[Line]

    def __init__(self) -> None:
        self.mocked_lines = []  # i know

    async def insert_lines(self, lines: list[Line]) -> None:
        self.mocked_lines.extend(lines)

    async def get_lines(self) -> list[Line]:
        return self.mocked_lines

    async def get_lines_by_city_id(self, city_id: int) -> list[Line]:
        lines = []
        for line in self.mocked_lines:
            if line.city_id == city_id:
                lines.append(line)

        return lines
