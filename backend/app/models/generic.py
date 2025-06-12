from sqlmodel import Field, Relationship, SQLModel

# generic message
class Message(SQLModel):
    message: str