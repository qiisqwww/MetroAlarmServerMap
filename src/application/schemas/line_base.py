from pydantic import BaseModel

__all__ = [
    "LineBase"
]


class LineBase(BaseModel):
    id: int
    name: str
    city_id: int
    alias: str
    logo_path: str

    class Config:
        from_attributes = True
