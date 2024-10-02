from pydantic import BaseModel, ConfigDict

__all__ = [
    "CityBase"
]


class CityBase(BaseModel):
    id: int
    name: str
    name_eng: str
    alias: str

    model_config = ConfigDict(from_attributes=True)
