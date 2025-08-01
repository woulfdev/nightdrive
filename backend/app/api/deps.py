from collections.abc import Generator
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from app.core.db import engine
from app.core.config import settings
from app.models.user import User

reusable_oauth2 = OAuth2PasswordBearer(
    # tokenUrl=f"{settings.API_V1_STR}/login/access-token"
    tokenUrl="token"
)

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_db)]
""" Used to get a database session. """
TokenDep = Annotated[str, Depends(reusable_oauth2)]

def get_current_user(session: SessionDep, token) -> User:
    """ 
    Gets the user from a JWT. 

    Also used for verifying if a valid token is used.

    :return: current user
    :rtype: User
    :raises:
        Raises a 403 HTTP Exception if token not valid or hashed_password = Null.
    """
    user = User()
    if user.hashed_password == None:
        raise HTTPException(
            status_code=403,
            detail="Password reset required."
        )
    # TODO: implement
    return

CurrentUser = Annotated[User, Depends(get_current_user)]
""" Get the request sending user. """