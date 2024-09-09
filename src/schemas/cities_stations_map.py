from pydantic import BaseModel

from .station_base import StationBase
from .city_base import CityBase
from .line_base import LineBase

__all__ = [
    "CitiesStationsMap"
]


class CitiesStationsMap(BaseModel):
    cities: list[CityBase]
    lines: list[LineBase]
    stations: list[StationBase]
