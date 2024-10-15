import pytest

from src.application.services import FvrtStationsService, MapService

from tests.unit.mocks import (
    MockStationRepository,
    MockFvrtStationRepository,
    MockLineRepository,
    MockCityRepository
)


@pytest.fixture()
def fvrt_stations_service() -> FvrtStationsService:
    fvrt_stations_service = FvrtStationsService(
        MockStationRepository(),
        MockFvrtStationRepository()
    )

    return fvrt_stations_service


@pytest.fixture()
def map_service() -> MapService:
    map_service = MapService(
        MockStationRepository(),
        MockLineRepository(),
        MockCityRepository(),
        MockFvrtStationRepository()
    )

    return map_service
