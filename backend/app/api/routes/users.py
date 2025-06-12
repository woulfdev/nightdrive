import uuid

from fastapi import APIRouter, Depends, HTTPException

from app.api.deps import SessionDep

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup/{signup_code}")
async def register_user(
    session: SessionDep,
    signup_code: str
):
    """
    Create a new user without the need to be logged in. Requires a signup code.
    """
    return signup_code

@router.get("/profile")
@router.get("/profile/{user_id}")
async def get_user_profile(
    user_id: uuid.UUID
):
    return

@router.post("/profile/update")
async def update_profile():
    return