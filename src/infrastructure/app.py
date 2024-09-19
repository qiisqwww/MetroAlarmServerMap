from fastapi import FastAPI

from src.infrastructure.config import DEBUG, PROJECT_NAME, DOCS_URL, OPENAPI_URL
from src.infrastructure import catch_exception_middleware
from src.infrastructure.routes import root_router

__all__ = [
    "app"
]


openapi_url = OPENAPI_URL if DEBUG else None

app = FastAPI(
    title=PROJECT_NAME,
    debug=DEBUG,
    docs_url=DOCS_URL,
    openapi_url=openapi_url
)

app.middleware("http")(catch_exception_middleware)
app.include_router(root_router)
