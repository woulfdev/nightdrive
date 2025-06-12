from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/oauth")
async def auth_login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    """
    OAuth compatible login, get an access token for future requests.
    """
    return

@router.get("/refresh")
async def refresh_token(
    
):
    """
    Exchange a token for a new one with a new time of life.
    """
    return

@router.post("/logout")
async def logout(

):
    """
    Invalidate a token.
    """
    return

@router.post("/logout/all")
async def full_logout():
    """
    Invalidates all token belonging to the calling user.
    """
    return