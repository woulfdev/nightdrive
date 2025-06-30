import uuid
import datetime
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel
from app.core.config import settings

class VehicleBase(SQLModel):
    make: str = Field()
    model: str = Field()
    production_year: int | None = Field(default=None)
    horsepower: int | None = Field(default=None)
    torque: int | None = Field(default=None)
    mileage: int | None = Field(default=None)
    max_speed: int | None = Field(default=None)

class Vehicle(VehicleBase, Table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field()
    public_visible: bool = Field(default=True)
    public_usable: bool = Field(default=False)
    creation_date: datetime.datetime = Field()

class VehicleCreate(VehicleBase):
    public_visible: bool | None = Field(default=True)
    public_usable: bool | None = Field(default=False)

class VehiclePublic(VehicleBase):
    user_id: uuid.UUID = Field()


class VehiclePrivate(Vehicle):
    user_id: uuid.UUID = Field()


class VehicleUpdate(VehicleBase):
    public_visible: bool | None = Field(default=True)
    public_usable: bool | None = Field(default=False)

class Vehicles(SQLModel):
    data: list[VehiclePublic]
    count:int
