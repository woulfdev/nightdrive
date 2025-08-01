import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, UploadFile

from app.api.routes import super, usersettings

from app.api.deps import SessionDep, CurrentUser
from app.models.user import *

router = APIRouter(prefix="/users", tags=["Users"])
router.include_router(super.sub_router)
router.include_router(usersettings.sub_router)

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
    # TODO
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
    # TODO
    return

@router.post("/signup")
async def register_user_no_code():
    """
    Register without a signup code.
    """
    if usersettings.REQUIRE_SIGNUP_CODE:
        raise HTTPException(
            status_code=401,
            detail="Signup without a signup code is not permited on this server."
        )
    
    # TODO: 
    return

@router.get("/profile/me", response_model=UserPrivate)
async def get_my_profile(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Get your own profile
    """
    # TODO
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
    # TODO
    return

@router.patch("/profile/update")
async def update_profile(
    session: SessionDep
):
    """
    Update profile
    """
    # TODO
    return

@router.post("/profile/picture")
async def upload_profile_picture(
    session: SessionDep,
    current_user: CurrentUser,
    file: UploadFile
):
    """
    Upload a new profile picture.
    """
    # TODO
    return

@router.delete("/profile/picture")
async def delete_profile_picture(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Delete your profile picture.
    """
    # TODO
    return

@router.delete("/profile/delete")
async def delete_user(
        session: SessionDep,
        current_user: CurrentUser
):
    """
    Delete your user.
    """
    # TODO
    return