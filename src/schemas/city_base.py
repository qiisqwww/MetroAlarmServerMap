from pydantic import BaseModel

__all__ = [
    "CityBase"
]


class CityBase(BaseModel):
    id: int
    name: str
