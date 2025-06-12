import secrets
import warnings
from typing import Annotated, Any, Literal

from pydantic import (
    AnyUrl,
    EmailStr,
    PostgresDsn,
    HttpUrl,
    BeforeValidator,
    computed_field
)

from pydantic_core import MultiHostUrl

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_ignore_empty=True,
        extra="ignore"
    )

    PROJECT_NAME: str = "NightDrive"

    API_V1_STR: str = "/api/v1"

    SECRET_KEY: str

    # 8 days
    ACCESS_TOKEN_EXPIRATION_MINUTES: int = 60*24*8

    PASSWORD_MIN_LENGTH: int = 8
    
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB
        )

settings = Settings()