from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
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
    """ Gets the user from a JWT. """
    # TODO: implement
    return

CurrentUser = Annotated[User, Depends(get_current_user)]
""" Get the request sending user. """