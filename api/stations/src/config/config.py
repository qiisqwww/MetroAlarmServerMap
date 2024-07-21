from pathlib import Path

from api.stations.src.config.env import StrEnv, BoolEnv

__all__ = [
    "DEBUG",
    "PROJECT_NAME",
    "LOGGING_PATH",
    "DOCS_URL",
    "OPENAPI_URL",
    "HTTP_HOST",
    "HTTP_PORT"
]


DEBUG: bool = BoolEnv("DEBUG")

PROJECT_NAME: str = StrEnv("PROJECT_NAME")

LOGGING_PATH: Path = Path(StrEnv("LOGGING_PATH"))
DOCS_URL: str = StrEnv("DOCS_URL")
OPENAPI_URL: str = StrEnv("OPENAPI_URL")

HTTP_HOST: str = StrEnv("HTTP_HOST")
HTTP_PORT: int = StrEnv("HTTP_PORT")
