import uuid

from fastapi import APIRouter, Depends, HTTPException

from app.api.deps import SessionDep

router = APIRouter(prefix="/friends", tags=["Friends"])

@router.post("/request/{user_id}")
async def friend_request():
    """
    Send a friend request to another user.
    """
    return
