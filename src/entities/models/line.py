from sqlalchemy import Column, Integer, String, ForeignKey

from src.entities.declarative_base import Base

__all__ = [
    "Line"
]


class Line(Base):
    __tablename__ = "lines"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    alias = Column(String, nullable=False)
    logo_path = Column(String)
