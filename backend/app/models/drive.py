import uuid
import datetime

from decimal import Decimal
from typing import Literal
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel
from app.core.config import settings

### Drive
class DriveBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, unique=True)
    user_id: uuid.UUID = Field(nullable=False)
    description: str = Field()
    distance: int = Field()
    duration: int = Field()
    max_speed: float = Field()
    avg_speed: float = Field()
    avg_speed_moving: float = Field()
    time_moving: float = Field()
    creation: datetime.datetime = Field()

class Drive(DriveBase, table=True):
    public: bool = Field(default=False)
    friends_only: bool = Field(default=False)

class DrivePublic(DriveBase):
    None # type: ignore

class DrivePrivate(Drive):
    None  # type: ignore

class DriveListPrivate(SQLModel):
    drives: list[DrivePrivate]

class DriveListPublic(SQLModel):
    drives: list[DrivePublic]

class DriveUpdate(SQLModel):
    id: uuid.UUID
    description: str | None = None
    public: bool | None = None
    friends_only: bool | None = None

### Drive track points
class TrackPointBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    drive_id: uuid.UUID = Field(nullable=False)
    timestamp: datetime.datetime = Field(nullable=False)
    latitude: Decimal = Field(nullable=False, max_digits=8, decimal_places=6)
    longitude: Decimal = Field(nullable=False, max_digits=9, decimal_places=6)
    elevation: int = Field()
    heading: int = Field()
    speed: float = Field()

class TrackPoint(TrackPointBase, table=True):
    None # type: ignore

class Track(SQLModel):
    points: list[TrackPointBase] = Field()

### Drive Markers
class MarkerBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(max_length=255)
    description: str = Field()
    latitude: Decimal = Field(nullable=False, max_digits=8, decimal_places=6)
    longitude: Decimal = Field(nullable=False, max_digits=9, decimal_places=6)

class Marker(MarkerBase, table=True):
    None # type: ignore

class MarkerUpdate(SQLModel):
    name: str | None = None
    description: str | None = None
    latitude: Decimal | None = Field(nullable=False, max_digits=8, decimal_places=6)
    longitude: Decimal | None = Field(nullable=False, max_digits=9, decimal_places=6)