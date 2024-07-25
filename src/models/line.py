from sqlalchemy import Column, Integer, String

from src.database import Base

__all__ = [
    "Line"
]


class Line(Base):
    __tablename__ = "lines"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
