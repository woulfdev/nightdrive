from fastapi import FastAPI, HTTPException
from fastapi.routing import APIRoute

from app.api.router import api_router
from app.core.config import settings
from app.models.generic import *

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    version="0.0.0"
)

# If the environemt variable ENVIRONMENT is set to "dev" load development route.
if settings.ENVIRONMENT == "dev":
    from app.api.routes import dev
    app.include_router(
        dev.dev_router,
        prefix=settings.API_V1_STR
    )

app.include_router(
    api_router,
    prefix=settings.API_V1_STR
)

@app.get("/", response_model=Message)
async def root():
    raise HTTPException(
        status_code=418,
        detail="I'm a teapot"
    )

@app.get("/info", response_model=APIInfo)
async def info():
    """
    Get basic API info.
    """
    message = APIInfo(
        version = app.version
    )
    return message