import uuid
from datetime import datetime
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel
from app.core.config import settings

class VehicleBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    make: str = Field()
    model: str = Field()

class Vehicle(VehicleBase):
    user_id: uuid.UUID