from sqlmodel import Field, Relationship, SQLModel
from app.core.config import settings

# generic message
class Message(SQLModel):
    message: str

class APIInfo(SQLModel):
    version: str
    name: str = settings.PROJECT_NAME
    open_api: str = f"{settings.API_V1_STR}/openapi.json"