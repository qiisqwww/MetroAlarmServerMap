from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query, HTTPException, status
from src.infrastructure.get_service import get_map_service, get_user_service
from src.application.schemas import CityStationsMap, CitiesStationsMap
from src.application.services import (
    MapService,
    CityWasNotFoundException,
    UserService,
    CannotFindUserExistsException
)
from src.application.city_alias import CityAlias

__all__ = [
    "map_router"
]


map_router = APIRouter()


@map_router.get("/full")
async def get_full_map(
        user_id: Annotated[int, Query()] = None,
        map_service: MapService = Depends(get_map_service),
        user_service: UserService = Depends(get_user_service)
) -> CitiesStationsMap:
    if user_id:
        try:
            user_exists = await user_service.find_user_exists(user_id)
        except CannotFindUserExistsException:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Cannot find whether user with id {user_id} exists or not. Try again later"
            )

        if not user_exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} was not registered"
            )

    return await map_service.get_full_map(user_id)


@map_router.get("/city/{city_alias}")
async def get_city_map(
        city_alias: Annotated[CityAlias, Path(title="Alias of the city")],
        user_id: Annotated[int, Query()] = None,
        map_service: MapService = Depends(get_map_service),
        user_service: UserService = Depends(get_user_service)
) -> CityStationsMap:
    if user_id:
        try:
            user_exists = await user_service.find_user_exists(user_id)
        except CannotFindUserExistsException:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Cannot find whether user with id {user_id} exists or not. Try again later"
            )

        if not user_exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} was not registered"
            )

    try:
        city_map = await map_service.get_map_for_city(city_alias, user_id)
    except CityWasNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"City with city_alias {city_alias} does not exist"
        ) from e

    return city_map
