import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path

from app.api.routes import super

from app.api.deps import SessionDep, CurrentUser
from app.models.user import *

router = APIRouter(prefix="/users", tags=["Users"])

router.include_router(
    super.sub_router
)

@router.get("/signup/code", response_model=SignupResponse)
async def get_signup_code(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Creates and returns a new signup code
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="The user doesn't have enough privileges."
        )
    
    return

@router.post("/signup/{signup_code}")
async def register_user(
    session: SessionDep,
    signup_code: Annotated[int, Path(gt=100000, le=999999)],
    user: UserRegister
):
    """
    Register using a sign up code.
    """
    return

@router.get("/profile/me", response_model=UserPrivate)
async def get_my_profile(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Get your own profile
    """
    return

@router.get("/profile/{user_id}", response_model=UserPublic)
async def get_user_profile(
    session: SessionDep,
    current_user: CurrentUser,
    user_id: uuid.UUID
):
    """
    Get a users profile.
    """
    return

@router.patch("/profile/update")
async def update_profile(
    session: SessionDep
):
    """
    Update profile
    """
    return

@router.delete("/delete/{user_id}")
async def delete_user(
        session: SessionDep,
        user_id: uuid.UUID
):
    """
    Delete a user, administrator only
    """
    return

@router.get("/settings/privacy", response_model=SettingsPrivacy)
async def get_privacy_settings(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Get your users privacy settings.
    """
    return

@router.patch("/settings/privacy")
async def update_privacy_settings(
    session: SessionDep,
    current_user: CurrentUser,
    privacy_settings: SettingsPrivacyUpdate
):
    """
    Update your users privacy settings.
    """
    return