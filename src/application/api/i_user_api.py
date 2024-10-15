from abc import ABC, abstractmethod

__all__ = [
    "IUserAPI"
]


class IUserAPI(ABC):
    @abstractmethod
    async def find_user_exists(self, user_id: int) -> bool:
        ...
