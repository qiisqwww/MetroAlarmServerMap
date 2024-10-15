from src.application.api import IUserAPI

__all__ = [
    "UserService"
]


class UserService:
    _user_api: IUserAPI

    def __init__(self, user_api: IUserAPI) -> None:
        self._user_api = user_api

    async def find_user_exists(self, user_id: int) -> bool:
        return await self._user_api.find_user_exists(user_id)
