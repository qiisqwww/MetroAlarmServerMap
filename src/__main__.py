import asyncio

import uvicorn

from src.infrastructure import app
from src.infrastructure.config import HTTP_HOST, HTTP_PORT, configurate_logger
from src.infrastructure.get_service import get_db_prefil_service


async def main() -> None:
    configurate_logger()
    await get_db_prefil_service().prefil_db()

    server_config = uvicorn.Config(app, host=HTTP_HOST, port=HTTP_PORT)
    server = uvicorn.Server(server_config)

    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
