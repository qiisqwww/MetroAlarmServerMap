from typing import Self

from pydantic import BaseModel

from src.models import Line

__all__ = [
    "LineBase"
]


class LineBase(BaseModel):
    id: int
    name: str
    line_id: int
    alias: str
    logo_path: str
