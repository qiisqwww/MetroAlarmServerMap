import pytest

from src.application.services import FvrtStationsService
from tests.unit.mocks import (
    MockStationRepository,
    MockFvrtStationRepository
)


@pytest.fixture()
def fvrt_stations_service() -> FvrtStationsService:
    fvrt_stations_service = FvrtStationsService(
        MockStationRepository(),
        MockFvrtStationRepository()
    )

    return fvrt_stations_service
