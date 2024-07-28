from enum import StrEnum, verify, UNIQUE

__all__ = [
    "CityAlias"
]


@verify(UNIQUE)
class CityAlias(StrEnum):
    Moscow = "msk"
    Saint_Petersburg = "spb"
