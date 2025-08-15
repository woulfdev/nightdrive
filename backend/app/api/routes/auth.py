from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.api.deps import SessionDep, CurrentUser
from app.core.log import logger
from app.models.generic import Token
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/oauth")
async def auth_login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """
    OAuth2 compatible login, get an access token for future requests.
    """
    user = User()

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif user.is_suspended:
        raise HTTPException(status_code=400, detail="")
    
    return

@router.get("/refresh")
async def refresh_token(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Exchange a token for a new one with a new time of life.
    """
    return

@router.post("/logout")
async def logout(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Invalidate a token.
    """
    return

@router.post("/logout/all")
async def full_logout(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Invalidates all token belonging to the calling user.
    """
    return