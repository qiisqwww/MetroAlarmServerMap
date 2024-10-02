from pydantic import BaseModel, ConfigDict

__all__ = [
    "LineBase"
]


class LineBase(BaseModel):
    id: int
    name: str
    city_id: int
    alias: str
    logo_path: str

    model_config = ConfigDict(from_attributes=True)
