import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path

from app.api.deps import SessionDep, CurrentUser
from app.models.user import *

sub_router = APIRouter(prefix="/super", tags=["Superuser"])

@sub_router.post("/password/reset")
async def reset_user_password():
    """
    Allows administrators to reset a users password.
    """
    return

@sub_router.delete("/delete/{user_id}")
async def delete_user(
        session: SessionDep,
        current_user: CurrentUser,
        user_id: uuid.UUID
):
    """
    Delete a user.
    """
    # if requesting user isn't the user to be deleted check if he is admin
    if not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="User is not permitted to delete other users."
        )
    # TODO
    return