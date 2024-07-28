from pydantic import BaseModel

__all__ = [
    "StationBase"
]


class StationBase(BaseModel):
    id: int
    name: str
    longitude: str
    latitude: str
    line_id: int
    city_id: int
    first_neighbour_id: int
    second_neighbour_id: int
    alarm_set: int
    is_favourite: bool
    radius: int
