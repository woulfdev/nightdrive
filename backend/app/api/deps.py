from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.core.db import engine
from app.models.user import User

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_db)]
""" Used to get a database session. """

def get_current_user(session: SessionDep, token) -> User:
    """ Gets the user from a JWT. """
    # TODO: implement
    return

CurrentUser = Annotated[User, Depends(get_current_user)]
""" Get the request sending user. """