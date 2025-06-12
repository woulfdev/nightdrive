from app.core.config import settings
from sqlmodel import Session, create_engine, select

from app.models.users import User

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

def init_db(session: Session) -> None:
    return