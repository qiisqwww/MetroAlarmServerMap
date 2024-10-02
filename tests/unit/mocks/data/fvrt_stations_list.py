from src.entities import UserFavouriteStation

__all__ = [
    "fvrt_stations_list",
]


fvrt_stations_list = [
    UserFavouriteStation(
        id=1,
        station_id=10001,
        user_id=13
    ),
    UserFavouriteStation(
        id=2,
        station_id=10002,
        user_id=15
    ),
    UserFavouriteStation(
        id=3,
        station_id=10003,
        user_id=13
    )
    ]
