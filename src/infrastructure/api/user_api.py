from aiohttp import ClientSession

from src.application.api.exceptions import UnexpectedRequestException, NonExpectedStatusCodeException
from src.application.api import IUserAPI
from src.config import FIND_USER_EXISTS_URL, SECRET_INSIDE_KEY

__all__ = [
    "UserAPI"
]


class UserAPI(IUserAPI):
    async def find_user_exists(self, user_id: int) -> bool:
        async with ClientSession() as session:
            try:
                response = await session.get(
                    headers={"secret-inside-key": SECRET_INSIDE_KEY},
                    url=FIND_USER_EXISTS_URL+f"?user_id={user_id}"
                )
            except Exception as e:
                raise UnexpectedRequestException(
                    "Occurred an unexpected exception during request"
                ) from e

            if response.status != 200:
                raise NonExpectedStatusCodeException(
                    f"Received unexpected {response.status} status code, 200 expected."
                )

            user_exists = (await response.json(encoding="utf-8")).get("user_exists", False)
            return user_exists
