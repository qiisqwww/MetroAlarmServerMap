from sqlalchemy import Column, Integer, String

from src.entities.declarative_base import Base

__all__ = [
    "City"
]


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    name_eng = Column(String, nullable=False)
    alias = Column(String, nullable=False)
