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

    # in days (default: 8)
    ACCESS_TOKEN_EXPIRATION_MINUTES: int = 60*24*8

    # in hours (default: 24)
    SIGNUP_CODE_LIFETIME: int = 24

    PASSWORD_MIN_LENGTH: int = 8

    '''
    PostgreSQL database settings
    '''    
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

    '''
    E-Mail settings
    '''    
    REQUIRE_EMAIL_VERIFICATION: bool = False

    SMTP_TLS: bool = True
    SMTP_SSL: bool = False
    SMTP_PORT: int = 587
    SMTP_HOST: str | None = None
    SMTP_USER: str | None = None
    SMTP_PASSWORD: str | None = None
    EMAIL_FROM_EMAIL: EmailStr | None = None
    EMAIL_FROM_NAME: EmailStr | None = None

    @computed_field
    @property
    def EMAIL_CONFIGURED(self) -> bool:
        return bool(self.SMTP_HOST and self.EMAIL_FROM_EMAIL)
    
    '''
    Live group settings
    '''
    # 
    LIVE_GROUP_MAX_DURATION: int = 24*60

settings = Settings()