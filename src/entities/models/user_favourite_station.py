from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.entities.declarative_base import Base

__all__ = [
    "UserFavouriteStation"
]


class UserFavouriteStation(Base):
    __tablename__ = "user_favourite_stations"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)

    station_id = Column(Integer, ForeignKey("stations.id"), nullable=False)
    station = relationship("Station")

    user_id = Column(Integer, nullable=False)
