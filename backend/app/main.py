from fastapi import FastAPI, HTTPException
from fastapi.routing import APIRoute

from contextlib import asynccontextmanager
import logging

from app.api.router import api_router
from app.core.config import settings
from app.core.log import logger
from app.models.generic import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("NightDrive started")
    logger.debug("NightDrive started")
    yield

app = FastAPI(
    lifespan=lifespan,
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    version="0.0.0"
)

app.include_router(
    api_router,
    prefix=settings.API_V1_STR
)

@app.get("/", response_model=Message)
async def root():
    """
    I'm a teapot
    """
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

@app.get("/motd", response_model=Message)
async def message_of_the_day():
    """
    Get the Message of the Day / Disclaimer.
    """
    message = Message(
        message=settings.MESSAGE_OF_THE_DAY
    )
    return message