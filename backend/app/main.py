from fastapi import FastAPI, HTTPException
from fastapi.routing import APIRoute

from app.api.main import api_router
from app.core.config import settings
from app.models.generic import Message

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
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