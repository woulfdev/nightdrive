import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path

from app.api.deps import SessionDep, CurrentUser
from app.models.generic import *

router = APIRouter(prefix="/dev", tags=["Development"])

@router.get("", response_model=Message)
async def dev_mode_status():
    """
    Allows for easily checking if server is configured for development.
    """
    message = Message(
        message="The server is in development mode! DO NOT USE IN PRODUCTION! Security might be lower or bypassed for testing purposes!"
    )
    return message