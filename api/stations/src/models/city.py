from pygments.lexers import q
from sqlalchemy import Column, Integer, String
from api.stations.src.database import Base

__all__ = [
    "City"
]


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
