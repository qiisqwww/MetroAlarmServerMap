from typing import Self

from pydantic import BaseModel

from src.entities.models import Station

__all__ = [
    "StationBase"
]


class StationBase(BaseModel):
    id: int
    name: str
    longitude: str | None
    latitude: str | None
    line_id: int
    city_id: int
    first_neighbour_id: int | None
    second_neighbour_id: int | None
    is_favourite: bool
    radius: int

    @classmethod
    def from_orm_model(cls, station: Station, is_favourite: bool = False) -> Self:
        return cls(
            id=station.id,
            name=station.name,
            longitude=station.longitude,
            latitude=station.latitude,
            line_id=station.line_id,
            city_id=station.city_id,
            first_neighbour_id=station.first_neighbour_id,
            second_neighbour_id=station.second_neighbour_id,
            is_favourite=is_favourite,
            radius=station.radius,
        )
