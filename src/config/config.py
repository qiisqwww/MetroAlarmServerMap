from pathlib import Path

from src.config.env import StrEnv, BoolEnv, IntEnv

__all__ = [
    "DEBUG",
    "PROJECT_NAME",
    "LOGGING_PATH",
    "DOCS_URL",
    "OPENAPI_URL",
    "HTTP_HOST",
    "HTTP_PORT",
    "DB_HOST",
    "DB_NAME",
    "DB_PORT",
    "DB_PASS",
    "DB_USER",
    "MAP_VERSION",
    "MSC_MAP_VERSION",
    "SPB_MAP_VERSION",
    "FIND_USER_EXISTS_URL"
]


DEBUG: bool = BoolEnv("DEBUG")

PROJECT_NAME: str = StrEnv("PROJECT_NAME")

LOGGING_PATH: Path = Path(StrEnv("LOGGING_PATH"))
DOCS_URL: str = StrEnv("DOCS_URL")
OPENAPI_URL: str = StrEnv("OPENAPI_URL")

HTTP_HOST: str = StrEnv("HTTP_HOST")
HTTP_PORT: int = IntEnv("HTTP_PORT")

DB_USER: str = StrEnv("DB_USER")
DB_PASS: str = StrEnv("DB_PASS")
DB_NAME: str = StrEnv("DB_NAME")
DB_PORT: int = IntEnv("DB_PORT")
DB_HOST: str = StrEnv("DB_HOST")

MAP_VERSION: str = StrEnv("MAP_VERSION")
MSC_MAP_VERSION: str = StrEnv("MSC_MAP_VERSION")
SPB_MAP_VERSION: str = StrEnv("SPB_MAP_VERSION")

FIND_USER_EXISTS_URL: str = StrEnv("FIND_USER_EXISTS")
