import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path

from app.api.deps import SessionDep, CurrentUser
from app.core.log import logger
from app.models.user import *

sub_router = APIRouter(prefix="/settings", tags=["User Settings"])

@sub_router.get("/generic", response_model=SettingsGeneric)
async def get_generic_settings(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Get generic settings.
    """
    # TODO
    return

@sub_router.patch("/generic")
async def update_generic_settings(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Update generic settings.
    """
    # TODO
    return

@sub_router.get("/privacy", response_model=SettingsPrivacy)
async def get_privacy_settings(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Get your users privacy settings.
    """
    # TODO
    return

@sub_router.patch("/privacy")
async def update_privacy_settings(
    session: SessionDep,
    current_user: CurrentUser,
    data: SettingsPrivacyUpdate
):
    """
    Update your users privacy settings.
    """
    # TODO
    return

@sub_router.patch("/security/password/update")
async def update_password(
    session: SessionDep,
    current_user: CurrentUser,
    data: SettingsSecurityPwdUpdate
):
    """
    Upadte your password.
    """
    # TODO
    return

@sub_router.post("/security/password/reset")
async def start_password_reset(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Send yourself an email containing a code allowing you to reset your password.
    """
    # TODO
    return

@sub_router.patch("/security/password/reset")
async def reset_password_with_code(
    session: SessionDep,
    data: SettingsSecurityPwdReset
):
    """
    Reset your password using the code send per email.
    """
    # TODO
    return