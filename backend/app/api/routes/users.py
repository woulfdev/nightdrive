import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path

from app.api.deps import SessionDep
from app.models.users import *

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup/{signup_code}")
async def register_user(
    session: SessionDep,
    signup_code: Annotated[int, Path(gt=100000, le=999999)]
):
    """
    Create a new user without the need to be logged in. Requires a signup code.
    """
    return signup_code

@router.get("/profile")
@router.get("/profile/{user_id}", response_model=UserProfile)
async def get_user_profile(
    user_id: uuid.UUID
):
    return

@router.post("/profile/update")
async def update_profile():
    return