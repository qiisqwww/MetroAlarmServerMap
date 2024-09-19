from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from src.entities.declarative_base import Base

__all__ = [
    "Station"
]


class Station(Base):
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    longitude = Column(String)
    latitude = Column(String)

    line_id = Column(Integer, ForeignKey("lines.id"), nullable=False)
    line = relationship("Line", backref="stations")
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    city = relationship("City", backref="stations")

    first_neighbour_id = Column(Integer)
    second_neighbour_id = Column(Integer)

    radius = Column(Integer, nullable=False, default=400)
    radius_rate = Column(Float, nullable=False, default=0)
