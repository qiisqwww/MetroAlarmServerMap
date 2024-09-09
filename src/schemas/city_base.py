from typing import Self

from pydantic import BaseModel

from src.models import City

__all__ = [
    "CityBase"
]


class CityBase(BaseModel):
    id: int
    name: str
    name_eng: str
    alias: str
