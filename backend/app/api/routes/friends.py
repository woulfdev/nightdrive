import uuid

from fastapi import APIRouter, Depends, HTTPException

from app.api.deps import SessionDep, CurrentUser
from app.core.log import logger

router = APIRouter(prefix="/friends", tags=["Friends"])

@router.post("/request/{user_id}")
async def friend_request(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Send a friend request to another user.
    """
    return
