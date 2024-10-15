__all__ = [
    "UnexpectedRequestException",
    "NonExpectedStatusCodeException"
]


class UnexpectedRequestException(Exception):
    """
    Raised when unexpected exceptions occur during aiohttp request
    """


class NonExpectedStatusCodeException(Exception):
    """
    Raised when an unexpected HTTP status code is received
    """
