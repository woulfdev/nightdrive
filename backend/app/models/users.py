import uuid

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel
from app.core.config import settings

# shared properties
class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, max_length=255)
    
    user_name: str = Field(unique=True, max_length=255)
    is_active: bool = True
    is_admin: bool = False

# properties to be received by API on user creation
class UserCreate(UserBase):
    password: str = Field(min_length=settings.PASSWORD_MIN_LENGTH, max_length=40)

# Databse model
class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
