from loguru import logger

from src.config import LOGGING_PATH

__all__ = [
    "configurate_logger",
]


def configurate_logger() -> None:
    logger.add(
        LOGGING_PATH,
        level="INFO",
        compression="zip",
        rotation="500 MB",
        enqueue=True,
        backtrace=True,
        diagnose=True,
    )
