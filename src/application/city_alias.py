from enum import StrEnum, verify, UNIQUE

__all__ = [
    "CityAlias"
]


@verify(UNIQUE)
class CityAlias(StrEnum):
    Moscow = "msk"
    Saint_Petersburg = "spb"

    @property
    def translation(self) -> str:
        translations = {
            CityAlias.Moscow: "Москва",
            CityAlias.Saint_Petersburg: "Санкт-Петербург"
        }

        return translations[self]
