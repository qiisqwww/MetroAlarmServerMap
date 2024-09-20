import asyncio

import uvicorn

from src.infrastructure import app_object
from src.config import HTTP_HOST, HTTP_PORT, configurate_logger
from src.infrastructure.get_service import get_db_prefil_service


async def main() -> None:
    configurate_logger()

    prefill_db_service = await get_db_prefil_service()
    await prefill_db_service.prefill_db()

    server_config = uvicorn.Config(app_object, host=HTTP_HOST, port=HTTP_PORT)
    server = uvicorn.Server(server_config)

    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
