from src.application.api import IUserAPI

__all__ = [
    "UserService",
    "CannotFindUserExistsException"
]


class CannotFindUserExistsException(Exception):
    """
    Raised when cannot find whether user exists or not
    """


class UserService:
    _user_api: IUserAPI

    def __init__(self, user_api: IUserAPI) -> None:
        self._user_api = user_api

    async def find_user_exists(self, user_id: int) -> bool:
        try:
            user_exists = await self._user_api.find_user_exists(user_id)
        except Exception as e:
            raise CannotFindUserExistsException(
                "Cannot find whether user exists or not"
            ) from e

        return user_exists
