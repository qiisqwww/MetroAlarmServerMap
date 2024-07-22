from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from api.stations.src.database import Base

__all__ = [
    "Station"
]


class Station(Base):
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    latitude = Column(String, nullable=False)

    line_id = Column(Integer, ForeignKey("lines.id"), nullable=False)
    line = relationship("Line", backref="stations")
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    city = relationship("City", backref="stations")

    first_neighbour_id = Column(Integer, ForeignKey("stations.id"), nullable=False)
    second_neighbour_id = Column(Integer, ForeignKey("stations.id"), nullable=False)
    neighbours = relationship("Station", backref="neighbours")

    radius = Column(Integer, nullable=False)
    radius_rate = Column(Float, nullable=False)
