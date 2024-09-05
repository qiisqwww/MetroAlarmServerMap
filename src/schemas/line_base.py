from pydantic import BaseModel

__all__ = [
    "LineBase"
]


class LineBase(BaseModel):
    id: int
    name: str
    alias: str
    logo_path: str
