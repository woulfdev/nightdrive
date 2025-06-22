import uuid
from datetime import datetime

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel
from app.core.config import settings

# shared properties
class UserBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_name: str = Field(unique=True, max_length=255)
    name: str = Field(max_length=255)

# properties to be received by API on user creation
class UserCreate(UserBase):
    email: EmailStr = Field(unique=True, max_length=255)
    password: str = Field(min_length=settings.PASSWORD_MIN_LENGTH, max_length=40)

# databse model
class User(UserBase, table=True):
    email: EmailStr = Field(unique=True, max_length=255)
    email_verified: bool
    hashed_password: str = Field()
    last_password_change: datetime = Field()
    is_suspended: bool = False
    is_admin: bool = False

# full user profile
class UserProfile(UserBase):
    distance_driven: int
    time_driven: int
