import uuid
from datetime import datetime, date
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel
from app.core.config import settings

class VehicleBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field()
    make: str = Field()
    model: str = Field()
    production_year: date = Field()
    horsepower: int = Field()
    torque: int = Field()
    mileage: int = Field()
    max_speed: int = Field()
    creation_date: datetime = Field()

class Vehicle(VehicleBase, Table=True):
    test: bool
