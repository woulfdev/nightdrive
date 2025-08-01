import uuid
import datetime

from typing import Literal
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel
from app.core.config import settings

# shared properties
class UserBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(unique=True, max_length=255)
    name: str = Field(max_length=255)

# properties to be received by API on user creation
class UserCreate(UserBase):
    email: EmailStr = Field(unique=True, max_length=255)
    password: str = Field(min_length=settings.PASSWORD_MIN_LENGTH, max_length=40)

class UserRegister(SQLModel):
    email: EmailStr = Field(unique=True, max_length=255)
    username: str = Field(unique=True, max_length=255)
    name: str = Field(default=None)
    password: str = Field(min_length=settings.PASSWORD_MIN_LENGTH, max_length=40)

# databse model
class User(UserBase, table=True):
    email: EmailStr = Field(unique=True, max_length=255)
    email_verified: bool
    hashed_password: str = Field()
    last_password_change: datetime.datetime = Field()
    is_suspended: bool = Field(default=False)
    is_admin: bool = Field(default=False)

# full user profile
class UserPublic(UserBase):
    distance_driven: int
    time_driven: int

class UserPrivate(UserBase):
    no_of_vehicles: int

# Signup

class SignupBase(SQLModel):
    id: int = Field(primary_key=True)
    code: int = Field()
    creation: datetime.datetime = Field()
    expiration: datetime.datetime = Field(nullable=False)
    used: bool = Field(default=False)

class Signup(SignupBase, table=True):
    valid_for_id: uuid.UUID = Field(default=None)

class SignupResponse(SignupBase):
    lifetime: int = settings.SIGNUP_CODE_LIFETIME

"""
Settings
"""

# Generic
class SettingsGeneric(SQLModel):
    color_theme: Literal["light", "dark", "system"] = Field(default="system")

# Privacy
class SettingsPrivacy(SQLModel):
    user_id: uuid.UUID = Field(primary_key=True, unique=True, foreign_key="user.id")
    profile_public: bool = Field(default=True)
    drives_default_public: bool = Field(default=False)
    friend_list_public: bool = Field(default=True)

class SettingsPrivacyUpdate(SQLModel):
    profile_public: bool | None = None
    drives_default_public: bool | None = None
    friend_list_public: bool | None = None

class SettingsSecurityPwdReset(SQLModel):
    username: str | None = Field(max_length=255)
    email: EmailStr | None = Field(max_length=255)
    reset_code: str = Field(min_length=8, max_length=12)
    password: str = Field(min_length=settings.PASSWORD_MIN_LENGTH, max_length=40)

class SettingsSecurityPwdUpdate(SQLModel):
    current_password: str = Field(min_length=settings.PASSWORD_MIN_LENGTH, max_length=40)
    new_password: str = Field(min_length=settings.PASSWORD_MIN_LENGTH, max_length=40)
