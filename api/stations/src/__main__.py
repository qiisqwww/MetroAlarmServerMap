from fastapi import FastAPI

from api.stations.src.config import DEBUG, PROJECT_NAME, DOCS_URL, OPENAPI_URL


openapi_url = OPENAPI_URL if DEBUG else None

app = FastAPI(
    title=PROJECT_NAME,
    debug=DEBUG,
    docs_url=DOCS_URL,
    openapi_url=openapi_url
)

"""NEED TO INCLUDE MIDDLEWARES & ROUTERS TO app OBJECT"""
